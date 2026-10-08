# Tip Splitter

A tiny Python CLI that splits a restaurant bill between people and adds a tip.

## Purpose

Work out how much each person pays when a group shares a bill, including a tip percentage (10% by default).

## Tech

- Python 3 (standard library only, no third-party dependencies)

## Contents

| File | Description |
| --- | --- |
| `tip.py` | `split(total, people, tip=0.1)` returns the per-person amount rounded to 2 decimals; running the file prints an example |
| `.gitignore` | Excludes `.env*`, `__pycache__/`, virtualenvs and build output |

## Usage

```bash
python tip.py
```

The example splits a 120 bill between 4 people with a 10% tip and prints `33.0`.

To use it from your own code:

```python
from tip import split

split(120, 4)             # 33.0
split(120, 4, tip=0.15)   # 34.5
```
