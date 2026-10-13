def calculate_prediction(x: float, weight: float) -> float:
    return x * weight

def calculate_loss(prediction, target): # type: ignore
    return(prediction - target) ** 2


def calculate_gradient(x, prediction, target):
    return 2 * (prediction - target) * x


def update_weight(weight, learning_rate, gradient):
    return weight - learning_rate * gradient



