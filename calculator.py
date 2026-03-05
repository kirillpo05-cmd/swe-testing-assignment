"""
Calculator logic module - Core calculation functionality without GUI dependencies.
"""

class Calculator:
    """Core calculator logic for arithmetic operations."""

    def __init__(self):
        """Initialize calculator state."""
        self.reset()

    def reset(self):
        """Reset calculator to initial state."""
        self.current_expression = ""
        self.result_displayed = False
        self.error_displayed = False

    def add_digit(self, digit):
        """
        Add a digit to the current expression.

        Args:
            digit (str): The digit to add (0-9 or '.')

        Returns:
            str: The updated display string
        """
        if self.error_displayed:
            if digit in "0123456789.":
                self.current_expression = digit
                self.error_displayed = False
                return digit
            return "Error"

        if self.result_displayed:
            self.current_expression = digit
            self.result_displayed = False
            return digit

        if digit == "." and "." in self.current_expression:
            return self.current_expression

        if self.current_expression == "0" and digit != ".":
            self.current_expression = digit
        else:
            self.current_expression += digit

        return self.current_expression

    def add_operator(self, operator):
        """
        Add an operator to the current expression.

        Args:
            operator (str): The operator to add (+, -, *, /)

        Returns:
            str: The updated display string
        """
        if self.error_displayed:
            return "Error"

        if self.result_displayed:
            self.result_displayed = False
            # Continue with the result as the start of new expression

        if not self.current_expression:
            if operator in "+-":
                self.current_expression = operator
            return self.current_expression

        if self.current_expression[-1] in "+-*/":
            self.current_expression = self.current_expression[:-1] + operator
        else:
            self.current_expression += operator

        return self.current_expression

    def calculate(self):
        """
        Evaluate the current expression.

        Returns:
            str: The result or "Error" if evaluation fails
        """
        if self.error_displayed:
            return "Error"

        if not self.current_expression:
            return "0"

        try:
            # Basic validation - ensure expression doesn't end with operator
            if self.current_expression[-1] in "+-*/":
                return "Error"

            result = eval(self.current_expression)

            # Convert to string, preserving decimal places if input had decimals
            if isinstance(result, float):
                # If the original expression contained decimals, keep the result as float
                if "." in self.current_expression:
                    result_str = str(result)
                else:
                    # If no decimals in input and result is whole number, convert to int
                    if result.is_integer():
                        result = int(result)
                    result_str = str(result)
            else:
                result_str = str(result)

            self.current_expression = result_str
            self.result_displayed = True
            return result_str

        except (SyntaxError, ZeroDivisionError, NameError, ValueError):
            self.error_displayed = True
            return "Error"

    def clear(self):
        """
        Clear the calculator.

        Returns:
            str: "0"
        """
        self.reset()
        return "0"

    def get_display(self):
        """
        Get the current display value.

        Returns:
            str: The current expression or "0" if empty
        """
        return self.current_expression if self.current_expression else "0"