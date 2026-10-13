#scikit learn is a python library for machine learning
# it give us ready made tools for 
#training mdels, splitting data, preprocessing data, making preditions, evaluating models.

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5], [6]]
y = [45, 50, 60, 70, 80, 90]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("X_train:", X_train)
print("X_test:", X_test)

print("y_train:", y_train)
print("y_test:", y_test)

model = LinearRegression()

model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Predictions:", predictions)

#Let's understand every part.
#
#X_train
#
#Features used for training.
#
#X_test
#
#Features used for testing.
#
#y_train
#
#Correct answers for training.
#
#y_test
#
#Correct answers for testing.


