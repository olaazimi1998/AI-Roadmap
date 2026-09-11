class Bank:

    def __init__(self):

        self.costumers = []


    def add_costumer(self, costumer):
        self.costumers.append(costumer)


        def show_costumers(self):
            for costumer in self.costumers:
                print(costumer.name)
