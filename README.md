# pnai

A minimal REPL for executing shell commands with structured results.

## Overview

pnai provides a simple Read-Eval-Print Loop interface for running shell commands. It wraps command execution in Pydantic models, giving you structured access to subprocess results.

## Installation

```bash
pip install pnai
```

Or with Poetry:

```bash
poetry add pnai
```

## Usage

Start the REPL:

```bash
pnai
```

Then enter any shell command at the prompt:

```
pnai> ls -la
pnai> echo "Hello, World!"
pnai> pwd
```

Exit with `Ctrl+C` or `Ctrl+D`.

## Requirements

- Python 3.11+
- Pydantic 2.3+

## License

Apache-2.0
