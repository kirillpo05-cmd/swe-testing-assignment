# Simple Calculator

A simple GUI calculator application built with Python and Tkinter.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Decimal point support
- Error handling for invalid operations
- Clean, user-friendly interface
- Read-only display to prevent direct input

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

## How to Run

1. Make sure you have Python 3.x installed
2. Run the application:
   ```bash
   python Main.py
   ```

## Usage

- Use the number buttons (0-9) to input numbers
- Use the operator buttons (+, -, *, /) for arithmetic operations
- Press "=" to calculate the result
- Press "C" to clear the display
- The decimal point (.) can be used for floating-point numbers

## Error Handling

- Division by zero displays "Error"
- Invalid expressions display "Error"
- After an error, only the clear button (C) or number buttons work to start fresh

## Project Structure

```
swe-testing-assignment/
├── Main.py          # Main calculator application
├── README.md        # This file
└── .gitignore       # Git ignore file
```