
import requests


def get_order_status(order_id: str):
    response = requests.get(
        "https://example.com/api/orders/" + order_id,
        timeout=10
    )

    response.raise_for_status()

    return response.json()
MAX_ITERATIONS = 5

for iteration in range(MAX_ITERATIONS):
    print(f"Agent iteration: {iteration + 1}")

    # Decide what to do.
    # Execute a tool if needed.
    # Check whether the task is complete.