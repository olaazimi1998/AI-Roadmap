
from models import Book, Math # type: ignore

m = Math()
m.study()


from mlmodel import MLModel, LinearRegression, DecisionTree
models = [ # type: ignore
    LinearRegression(),
    DecisionTree()
]


for model in models: # type: ignore
    model.train() # type: ignore
    model.predict() # type: ignore




from payment import Payment, Paypal, Creditcard # type: ignore

paypal = Paypal()

card = Creditcard()

paypal.pay(100) # type: ignore\

card.pay(700)



paypal.pay(900)
card.pay(600)
paypal.pay(700)
card.pay(800)










