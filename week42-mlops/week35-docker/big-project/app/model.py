class SimpleModel:
    def predict(self, value: float) -> str:
        if value >= 50:
            return "positive"
        else:
            return "negative"


model = SimpleModel()