# Project Specification: libravore

## Overview

`libravore` is a Python package designed to handle the common misspelling of the package `librovore`. It serves as a redirection and warning mechanism for users who accidentally install or import `libravore` instead of `librovore`.

- **Purpose**: To issue warnings upon import and redirect to the correct `librovore` package, preventing confusion.
- **Status**: Active, serving as a misspelling redirect.

## Tech Stack

The project utilizes a modern Python development stack:

- **Language**: Python
- **Build System**: Hatch
- **Linting & Formatting**: Ruff
- **Type Checking**: Pyright
- **Documentation**: Sphinx
- **Templating**: Copier
- **Testing**: Pytest
- **CI/CD**: GitHub Actions

## Project Conventions

### Filesystem Organization

The project follows a specific filesystem organization as detailed in the architectural documentation.

- See [Filesystem Organization](../filesystem.rst) for a detailed breakdown of the directory structure, including source code organization and root directory layout.

### Architecture Documentation

For more architectural details, refer to:

- [Architecture Index](../index.rst): The entry point for all architectural documentation.
- [Architecture Summary](../summary.rst): Summary of the architecture.
- [Decisions](../decisions/index.rst): Records of architectural decisions.
- [Designs](../designs/index.rst): Detailed design documents.
- [Test Plans](../testplans/index.rst): Strategies and plans for testing.
