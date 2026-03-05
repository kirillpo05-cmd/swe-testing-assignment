# Quick-Calc

Quick-Calc is a simple, cross-platform GUI calculator built with Python and Tkinter. It supports basic arithmetic operations and includes a clean, responsive interface. The application separates the calculation logic from the user interface so that the core functionality can be unit-tested independently and integrated with the GUI in a predictable way.

## Features

- Basic arithmetic: addition, subtraction, multiplication, division
- Decimal point support and prevention of invalid input
- Error handling for invalid expressions and division by zero
- Read-only display to avoid manual entry
- Modular design with clear separation between UI and logic

## Setup Instructions

1. Install Python 3.x if it's not already available (https://www.python.org/downloads/).
2. Clone or download the repository and change into its directory:
   ```bash
   cd "c:\JAVA Script\swe-testing-assignment"
   ```
3. (Optional) create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate    # Windows PowerShell
   ```
4. Install dependencies:
   ```bash
   pip install pytest
   ```
   Tkinter is bundled with most Python distributions and typically requires no additional installation.
5. Launch the calculator:
   ```bash
   python Main.py
   ```

## How to Run Tests

You can execute both unit and integration tests using **pytest**, which was selected as the testing framework for this project.

To run the full suite:
```bash
python -m pytest -v
```

To run only a specific file:
```bash
python -m pytest test_calculator.py -v     # unit tests
python -m pytest test_integration.py -v    # integration tests
```

## Testing Framework Research

Python provides several testing tools, with **unittest** bundled in the standard library and **pytest** available as a third-party package. Unittest uses a class-based structure and mirrors JUnit’s style, requiring boilerplate such as `TestCase` subclasses, `setUp`/`tearDown` methods, and assertion methods (`self.assertEqual`, etc.). It is stable, widely recognized, and always available without installation, making it suitable for simple projects or environments where external dependencies are frowned upon. However, its verbosity and rigid structure can make test code longer and harder to read.

Pytest, by contrast, encourages a more concise and expressive syntax. Tests are written as plain functions; fixtures provide setup/teardown without inheritance; and assert statements are used directly, with built-in introspective failure reporting. Pytest also offers powerful features like parameterization, plugins, and easy test selection via markers. The trade-off is that it introduces an external dependency and a learning curve for developers coming from the standard library’s style.

For Quick-Calc, pytest was chosen because its readability and rich feature set accelerate writing both unit and integration tests. The ability to keep test code minimal and expressive helps maintain clarity in a small educational project, while the plugin ecosystem allows future expansion (e.g. GUI automation) without refactoring. Although unittest could have accomplished the same functionality, pytest’s advantages in developer experience made it the preferred option.

## Project Structure

```
swe-testing-assignment/
├── Main.py              # Main GUI application
├── calculator.py        # Core calculator logic (testable)
├── test_calculator.py   # Unit tests for calculator logic
├── test_integration.py  # Integration tests for GUI and logic
├── README.md            # This file
└── .gitignore           # Git ignore file
```