from langchain_core.tools import tool
@tool
def calculator(expression: str) -> str:
    """Calculate a basic aritmic expression."""

    allowed_characters = set("0123456789+-*/().")

    if not expression:
        return "error: please provide a calculation."

    if any(char not in allowed_characters for char in expression):
        return "Error: Only basic arithmetic is supported."

    try:
        result = eval(
                expression,
                {"__builtins__": {}},
                {},
            )
        return str(result)
    except (SyntaxError, ZeroDivisionError, TypeError):
            return "Error: Invalid mathematical expression."    

        