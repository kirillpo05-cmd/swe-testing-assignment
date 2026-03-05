"""
Unit tests for the Calculator class.
Run with: python -m pytest test_calculator.py -v
"""


from calculator import Calculator


class TestCalculator:
    """Test cases for Calculator class."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()

    def test_addition(self):
        """Test basic addition operation."""
        self.calc.add_digit("5")
        self.calc.add_operator("+")
        self.calc.add_digit("3")
        result = self.calc.calculate()
        assert result == "8"

    def test_subtraction(self):
        """Test basic subtraction operation."""
        self.calc.add_digit("10")
        self.calc.add_operator("-")
        self.calc.add_digit("4")
        result = self.calc.calculate()
        assert result == "6"

    def test_multiplication(self):
        """Test basic multiplication operation."""
        self.calc.add_digit("7")
        self.calc.add_operator("*")
        self.calc.add_digit("6")
        result = self.calc.calculate()
        assert result == "42"

    def test_division(self):
        """Test basic division operation."""
        self.calc.add_digit("15")
        self.calc.add_operator("/")
        self.calc.add_digit("3")
        result = self.calc.calculate()
        assert result == "5"

    def test_division_by_zero(self):
        """Test division by zero error handling."""
        self.calc.add_digit("10")
        self.calc.add_operator("/")
        self.calc.add_digit("0")
        result = self.calc.calculate()
        assert result == "Error"
        assert self.calc.error_displayed == True

    def test_negative_numbers(self):
        """Test operations with negative numbers."""
        self.calc.add_operator("-")
        self.calc.add_digit("5")
        self.calc.add_operator("+")
        self.calc.add_digit("3")
        result = self.calc.calculate()
        assert result == "-2"

    def test_decimal_numbers(self):
        """Test operations with decimal numbers."""
        self.calc.add_digit("3")
        self.calc.add_digit(".")
        self.calc.add_digit("5")
        self.calc.add_operator("*")
        self.calc.add_digit("2")
        result = self.calc.calculate()
        assert result == "7.0"

    def test_large_numbers(self):
        """Test operations with large numbers."""
        self.calc.add_digit("1000000")
        self.calc.add_operator("*")
        self.calc.add_digit("1000000")
        result = self.calc.calculate()
        assert result == "1000000000000"

    def test_multiple_decimal_points_prevented(self):
        """Test that multiple decimal points are prevented."""
        self.calc.add_digit("3")
        self.calc.add_digit(".")
        self.calc.add_digit("5")
        # Second decimal point should be ignored
        self.calc.add_digit(".")
        display = self.calc.get_display()
        assert display == "3.5"

    def test_operator_replacement(self):
        """Test that consecutive operators replace each other."""
        self.calc.add_digit("5")
        self.calc.add_operator("+")
        self.calc.add_operator("-")
        self.calc.add_digit("3")
        result = self.calc.calculate()
        assert result == "2"

    def test_clear_functionality(self):
        """Test clear functionality."""
        self.calc.add_digit("123")
        self.calc.add_operator("+")
        self.calc.add_digit("456")
        result = self.calc.clear()
        assert result == "0"
        assert self.calc.get_display() == "0"
        assert self.calc.result_displayed == False
        assert self.calc.error_displayed == False

    def test_error_recovery_with_numbers(self):
        """Test that after error, numbers start new calculation."""
        # Cause an error
        self.calc.add_digit("10")
        self.calc.add_operator("/")
        self.calc.add_digit("0")
        self.calc.calculate()  # This should set error_displayed = True

        # Now add a number - should start fresh
        self.calc.add_digit("5")
        display = self.calc.get_display()
        assert display == "5"
        assert self.calc.error_displayed == False

    def test_error_blocks_operators(self):
        """Test that operators are blocked when error is displayed."""
        # Cause an error
        self.calc.add_digit("10")
        self.calc.add_operator("/")
        self.calc.add_digit("0")
        self.calc.calculate()

        # Try to add operator - should be blocked
        result = self.calc.add_operator("+")
        assert result == "Error"
        assert self.calc.error_displayed == True

    def test_result_displayed_allows_continue_calculation(self):
        """Test that after calculation result, operators continue with the result."""
        self.calc.add_digit("5")
        self.calc.add_operator("+")
        self.calc.add_digit("3")
        self.calc.calculate()  # Result should be 8

        # Now add operator - should continue with 8
        self.calc.add_operator("*")
        self.calc.add_digit("2")
        result = self.calc.calculate()
        assert result == "16"

    def test_empty_expression_calculation(self):
        """Test calculation with empty expression."""
        result = self.calc.calculate()
        assert result == "0"

    def test_expression_ending_with_operator(self):
        """Test that expression ending with operator causes error."""
        self.calc.add_digit("5")
        self.calc.add_operator("+")
        result = self.calc.calculate()
        assert result == "Error"