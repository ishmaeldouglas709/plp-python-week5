# PLP Python Week 5

## Overview
This project practices organizing Python code into modules, importing helper functions, using the standard library, and generating random passwords.

## Files

- **`helpers.py`** — Provides reusable functions:
  - `tables_needed(people, seats)`: calculates the number of tables required, rounding up to a whole table.
  - `welcome(name)`: returns a welcome message for the supplied name.
  - Includes a small example guarded by `if __name__ == "__main__":`.
- **`main.py`** — Imports `helpers` and demonstrates calling its functions with sample values.
- **`password_generator.py`** — Generates random passwords using uppercase and lowercase letters and digits. It demonstrates the default length of 8 and a custom length of 12.

## Requirements
- Python 3.8 or later
- No third-party packages are required. The project uses Python standard-library modules `math`, `random`, and `string`.

## How to Run
Open a terminal in the project directory and run:

```bash
python main.py
python helpers.py
python password_generator.py
```

## Expected Behavior
- `main.py` prints a welcome message and table counts for the sample inputs.
- `helpers.py` prints the table count for 10 people with 4 seats per table.
- `password_generator.py` prints two randomly generated passwords and their lengths. The password values will differ each time it runs.

## Learning Objectives
- Split code into reusable Python modules.
- Import and call functions from another file.
- Use `math.ceil()` to round a calculation up.
- Work with Python's `random` and `string` modules.
- Use a main-module guard to control example execution.
