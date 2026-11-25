#!/usr/bin/env python3
# vim: set filetype=python fileencoding=utf-8:
# -*- coding: utf-8 -*-

''' Stdio MCP shim: answer server/discover with -32601 for rmcp 1.x. '''


import contextlib
import json
import signal
import subprocess
import sys
import threading


_MIN_ARGV = 2
_METHOD_NOT_FOUND = -32601


def _build_not_found_reply( request_id ) -> bytes:
    reply = {
        'jsonrpc': '2.0',
        'id': request_id,
        'error': {
            'code': _METHOD_NOT_FOUND,
            'message': 'Method not found',
        },
    }
    return (
        json.dumps( reply, separators = ( ',', ':' ) ) + '\n'
    ).encode( 'utf-8' )


def _forward_stdin( child_stdin, stdout_lock ) -> None:
    for raw_line in sys.stdin.buffer:
        try:
            message = json.loads( raw_line )
        except ( UnicodeDecodeError, json.JSONDecodeError ):
            message = None

        if (
            isinstance( message, dict )
            and message.get( 'method' ) == 'server/discover'
        ):
            if 'id' in message:
                payload = _build_not_found_reply( message[ 'id' ] )
                with stdout_lock:
                    sys.stdout.buffer.write( payload )
                    sys.stdout.buffer.flush( )
            continue

        try:
            child_stdin.write( raw_line )
            child_stdin.flush( )
        except BrokenPipeError:
            break


def _forward_stdout( child_stdout, stdout_lock ) -> None:
    with contextlib.suppress( BrokenPipeError ):
        while True:
            line = child_stdout.readline( )
            if not line:
                break
            with stdout_lock:
                sys.stdout.buffer.write( line )
                sys.stdout.buffer.flush( )


def main( ) -> int:
    if len( sys.argv ) < _MIN_ARGV:
        sys.stderr.write(
            'usage: mcp-discover-shim.py <command> [args...]\n'
        )
        return 2

    child = subprocess.Popen(  # noqa: S603
        sys.argv[ 1: ],
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = None,
    )
    if child.stdin is None or child.stdout is None:
        return 1

    def _forward_signal( signum, _frame ):
        if child.poll( ) is None:
            child.send_signal( signum )

    signal.signal( signal.SIGTERM, _forward_signal )
    signal.signal( signal.SIGINT, _forward_signal )

    stdout_lock = threading.Lock( )
    reader = threading.Thread(
        target = _forward_stdout,
        args = ( child.stdout, stdout_lock ),
        daemon = True,
    )
    reader.start( )

    try:
        _forward_stdin( child.stdin, stdout_lock )
    finally:
        with contextlib.suppress( OSError ):
            child.stdin.close( )

    reader.join( timeout = 5.0 )
    return child.wait( )


if __name__ == '__main__':
    raise SystemExit( main( ) )
