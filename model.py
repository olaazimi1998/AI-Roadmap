class HousePriceModel:
    def predict(self, size):
        if size <= 0:
            raise ValueError("Size must be positive.")

        price = size * 1000

        return price


#git init, git add .,git commit -m "Build ML model with automated tests"