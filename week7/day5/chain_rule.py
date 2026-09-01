#The Chain Rule helps us calculate how a change in one variable affects another variable through multiple steps.
#
#فارسی
#قانون زنجیره به ما کمک می‌کند بفهمیم:
#
#اگر یک مقدار تغییر کند، این تغییر از چند مرحله عبور کرده و در نهایت چه تأثیری روی نتیجه گذاشته است؟
#
#
#Backpropagation = calculating gradients by moving backward through the network.
#
#فارسی
#Backpropagation یعنی محاسبه گرادیان‌ها با حرکت به سمت عقب در شبکه عصبی.
#
#به این شکل:
#
#Forward:
#
#Input
# ↓
#Layer 1
# ↓
#Layer 2
# ↓
#Prediction
# ↓
#Loss
#
#Backward:
#
#Loss
# ↓
#Gradient
# ↓
#Layer 2
# ↓
#Gradient
# ↓
#Layer 1
# ↓
#Gradients




#Neural network
#             FORWARD
#Input ───────────────────→ Prediction
#                              ↓
#                             Loss
#                              ↓
#             BACKWARD         ↓
#Weights ←────────────────── Gradients
#   ↓
#Update
#   ↓
#Better weights



#How does a neural network learn?

#می‌توانی بگویی:

#The network performs a forward pass to 
# make a prediction, calculates a
#  loss, uses backpropagation and
#  the chain rule to calculate gradients, 
# and then updates its weights using an
#  optimization algorithm such as gradient descent.

x = 2.0
target = 10.0
w = 1
learning_rate = 0.1

for step in range(10):
    prediction = w * x

    loss = (prediction - target) ** 2
    gradient = 2 * (prediction - target) * x
    w = w - learning_rate * gradient

    print(f"Step {step + 1}: "
          f"prediction={prediction:.2f}, "
          f"loss={loss:.4f}"
          f"w={w:.2f}")
    ## Chain Rule

## Forward Pass

## Backward Pass

## Backpropagation

## Gradient Descent

## Python Example

## My Explanation