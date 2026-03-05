# Testing Strategy for Quick-Calc

This document outlines the testing strategy for the Quick-Calc project. It covers what has been tested (and what has not), the overall approach, and how the suite relates to key testing concepts from Lecture 3.

## What Was Tested

- **Core Calculation Logic**: Every arithmetic operation (addition, subtraction, multiplication, division) including edge cases (division by zero, negative values, decimals, large numbers) was tested with unit tests in `test_calculator.py`.
- **Input Validation and State Management**: Prevention of multiple decimal points, operator replacement, clear functionality, error recovery, and continuation after results were all covered in unit tests.
- **GUI–Logic Interaction**: Integration tests in `test_integration.py` simulate button clicks and verify that the display updates correctly and that the underlying logic produces the correct results.

## What Was Not Tested

- **GUI Rendering and Layout**: We intentionally did not write automated tests for the visual appearance or layout of the Tkinter interface; such tests are usually brittle and fall under manual or specialized UI testing tools.
- **Performance/Load**: The calculator is simple and not intended for high throughput, so no performance or stress tests were written.
- **Non-functional Requirements**: Accessibility, internationalization, or security properties were not evaluated.

## Overall Approach

The project follows a **separation of concerns**: calculation logic is encapsulated in a separate module (`calculator.py`), allowing the bulk of tests to run without the GUI. Pytest is used for both unit and integration tests, enabling expressive and concise test definitions. Integration tests exercise the public interface of the GUI class (`on_button_click`) to ensure components work together.

### The Testing Pyramid

- **Unit tests** form the broad base. We wrote 16 unit tests covering nearly all code paths in `Calculator`. This reflects the pyramid’s recommendation to have many fast, isolated tests.
- **Integration tests** sit above the base. Eight integration tests exercise interactions between the UI and logic but are fewer in number because they are slightly slower and more complex.
- There are no end-to-end or UI automation tests (the top of the pyramid) since the project scope is small.

### Black-box vs White-box Testing

- **Unit tests** are largely *white-box*. They are aware of internal methods (`add_digit`, `add_operator`, etc.) and test specific code paths and state transitions.
- **Integration tests** behave as *black-box* tests from the GUI perspective: they only interact with public methods (`on_button_click`) and inspect the display without knowledge of internal state.

### Functional vs Non-Functional Testing

The suite focuses exclusively on **functional testing**: verifying that the calculator produces correct results and handles user input properly. We did not cover non-functional aspects such as performance, accessibility, or UI appearance.

### Regression Testing

The pytest suite serves as a regression guard. Any modification to `calculator.py` or GUI logic can be validated by rerunning all tests. A failing test pinpoints exactly which functionality regressed, enabling quick fixes. New features should come with new tests to maintain this safety net.

## Test Results Summary

All 24 automated tests (16 unit and 8 integration) execute with `pytest` and currently pass.

- **Unit tests** exercise every piece of calculation logic and state management.
- **Integration tests** validate real user interactions via the GUI class.

Re-running `python -m pytest -v` after any code change ensures regressions are caught.