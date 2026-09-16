import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from linear_regression import LinearRegressionScratch


sns.set_theme(style="whitegrid")

X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([3, 5, 7, 9, 11], dtype=float)

model = LinearRegressionScratch(learning_rate=0.01, epochs=1000)
model.fit(X, y)

print("\nFinal weight:", model.w)
print("Final bias:", model.b)

prediction = model.predict(np.array([6]))
print("Prediction for 6:", prediction)

# Visualize the raw data and fitted line
x_line = np.linspace(X.min(), X.max(), 100)
y_line = model.w * x_line + model.b

df = pd.DataFrame({"X": X, "y": y})

fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=df, x="X", y="y", s=100, color="royalblue", ax=ax, label="Training data")
ax.plot(x_line, y_line, color="darkorange", linewidth=2.5, label=f"Fitted line: y = {model.w:.2f}x + {model.b:.2f}")
ax.set_title("Linear Regression from Scratch")
ax.set_xlabel("X")
ax.set_ylabel("y")
ax.legend()
plt.tight_layout()
plt.savefig("linear_regression_plot.png")
plt.show()



#English
#Cost Function
#
#MSE
#
#Error
#
#Gradient
#
#Gradient Descent
#
#Learning Rate
#
#Epoch
#
#Weight update
#
#Bias update
#
#Training loop
#
#Linear Regression from scratch with NumPy
#
#اگر در مصاحبه از تو پرسیدند:
#
#How does Linear Regression learn?
#
#باید بتوانی تقریباً این‌طور توضیح بدهی:
#
#مدل ابتدا prediction می‌سازد. سپس prediction را با مقدار واقعی مقایسه می‌کند و Cost را محاسبه می‌کند. Gradient به مدل می‌گوید پارامترها را در چه جهتی تغییر دهد. سپس Gradient Descent، weight و bias را با استفاده از learning rate به‌روزرسانی می‌کند. این فرآیند چندین بار تکرار می‌شود تا Cost کاهش پیدا کند.
#

#             MACHINE LEARNING
#
#                 DATA
#                  ↓
#             MODEL
#                  ↓
#             PREDICTION
#                  ↓
#               ERROR
#                  ↓
#                COST
#                  ↓
#              GRADIENT
#                  ↓
#          GRADIENT DESCENT
#                  ↓
#          UPDATE w and b
#                  ↓
#             BETTER MODEL
#                  ↓
#             REPEAT 🔁





