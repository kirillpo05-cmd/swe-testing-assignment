"""
Integration tests for the Calculator application.
These tests verify the interaction between the GUI layer and the calculation logic.
Run with: python -m pytest test_integration.py -v
"""


import tkinter as tk
from unittest.mock import Mock, patch
from Main import CalculatorApp


class TestCalculatorIntegration:
    """Integration tests for CalculatorApp GUI and Calculator logic interaction."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        # Create a mock root window to avoid actually displaying GUI
        with patch('tkinter.Tk'):
            self.app = CalculatorApp(Mock())

    def test_full_calculation_workflow(self):
        """Integration test: Simulate full user interaction 5 + 3 = 8."""
        # Simulate user pressing: 5, +, 3, =
        self.app.on_button_click("5")
        assert self.app.display_var.get() == "5"

        self.app.on_button_click("+")
        assert self.app.display_var.get() == "5+"

        self.app.on_button_click("3")
        assert self.app.display_var.get() == "5+3"

        self.app.on_button_click("=")
        assert self.app.display_var.get() == "8"

    def test_clear_after_calculation(self):
        """Integration test: Verify Clear button resets display after calculation."""
        # Perform a calculation first
        self.app.on_button_click("7")
        self.app.on_button_click("*")
        self.app.on_button_click("6")
        self.app.on_button_click("=")
        assert self.app.display_var.get() == "42"

        # Now press Clear
        self.app.on_button_click("C")
        assert self.app.display_var.get() == "0"

    def test_decimal_calculation_workflow(self):
        """Integration test: Simulate decimal calculation 3.5 * 2 = 7.0."""
        # Simulate user pressing: 3, ., 5, *, 2, =
        self.app.on_button_click("3")
        assert self.app.display_var.get() == "3"

        self.app.on_button_click(".")
        assert self.app.display_var.get() == "3."

        self.app.on_button_click("5")
        assert self.app.display_var.get() == "3.5"

        self.app.on_button_click("*")
        assert self.app.display_var.get() == "3.5*"

        self.app.on_button_click("2")
        assert self.app.display_var.get() == "3.5*2"

        self.app.on_button_click("=")
        assert self.app.display_var.get() == "7.0"

    def test_error_handling_workflow(self):
        """Integration test: Verify error handling and recovery."""
        # Cause a division by zero error
        self.app.on_button_click("1")
        self.app.on_button_click("0")
        self.app.on_button_click("/")
        self.app.on_button_click("0")
        self.app.on_button_click("=")
        assert self.app.display_var.get() == "Error"

        # After error, only numbers should work to start new calculation
        self.app.on_button_click("5")
        assert self.app.display_var.get() == "5"

        # Continue with a valid calculation
        self.app.on_button_click("+")
        self.app.on_button_click("3")
        self.app.on_button_click("=")
        assert self.app.display_var.get() == "8"

    def test_operator_replacement_workflow(self):
        """Integration test: Verify operator replacement works in full workflow."""
        # Start with 5, then try different operators
        self.app.on_button_click("5")
        self.app.on_button_click("+")
        assert self.app.display_var.get() == "5+"

        # Replace + with -
        self.app.on_button_click("-")
        assert self.app.display_var.get() == "5-"

        self.app.on_button_click("3")
        self.app.on_button_click("=")
        assert self.app.display_var.get() == "2"

    def test_continuation_after_result(self):
        """Integration test: Verify calculations can continue after showing a result."""
        # First calculation: 5 + 3 = 8
        self.app.on_button_click("5")
        self.app.on_button_click("+")
        self.app.on_button_click("3")
        self.app.on_button_click("=")
        assert self.app.display_var.get() == "8"

        # Continue with * 2 = 16
        self.app.on_button_click("*")
        assert self.app.display_var.get() == "8*"

        self.app.on_button_click("2")
        self.app.on_button_click("=")
        assert self.app.display_var.get() == "16"

    def test_multiple_operations_workflow(self):
        """Integration test: Complex calculation with multiple operations."""
        # Calculate: 2 + 3 * 4 = 14 (following order of operations)
        self.app.on_button_click("2")
        self.app.on_button_click("+")
        self.app.on_button_click("3")
        self.app.on_button_click("*")
        self.app.on_button_click("4")
        self.app.on_button_click("=")
        assert self.app.display_var.get() == "14"

    def test_negative_number_workflow(self):
        """Integration test: Negative number calculation."""
        # Calculate: -5 + 10 = 5
        self.app.on_button_click("-")
        self.app.on_button_click("5")
        self.app.on_button_click("+")
        self.app.on_button_click("1")
        self.app.on_button_click("0")
        self.app.on_button_click("=")
        assert self.app.display_var.get() == "5"