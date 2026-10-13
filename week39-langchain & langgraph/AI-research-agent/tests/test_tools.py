from tools import calculator


def test_calculator_handles_spaces_and_basic_math():
    assert calculator.invoke({"expression": "125 * 8"}) == "1000"
    assert calculator.invoke({"expression": "12 + 3 * 4"}) == "24"


def test_calculator_rejects_invalid_input():
    assert calculator.invoke({"expression": "import os"}) == "Error: Only basic arithmetic is supported."
    assert calculator.invoke({"expression": ""}) == "error: please provide a calculation."


def test_calculator_handles_division_by_zero():
    assert calculator.invoke({"expression": "10 / 0"}) == "Error: Invalid mathematical expression."
