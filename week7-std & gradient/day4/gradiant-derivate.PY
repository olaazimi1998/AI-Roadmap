#A derivative tells us:

#How quickly is something changing?

#Input
#  ↓
#Model
#  ↓
#Prediction
#  ↓
#Loss
w = 10.1
learning_rate = 0.1

for step in range(10):
    gardiant = 2 * w
    w = w - learning_rate * gardiant
    print(f"Step {step + 1}: w = {w:.4f}")


#English
#Prediction → Loss → Gradient → Weight Update → Better Prediction
#
#فارسی
#پیش‌بینی → محاسبه خطا → گرادیان → تغییر وزن‌ها → پیش‌بینی بهتر
#
#این یکی از پایه‌های اصلی Machine Learning و Deep
#

#w = 8.0
learning_rate = 0.1

for step in range(10):
    # calculate gradient
    gardiant = 2 * w

    # update w
    w = w - learning_rate * gardiant


    print(f"Step {step + 1}:w = {w:.2f}")

### Derivative

## Gradient

## Gradient Descent

## Learning Rate

## Weight Update

## Python Example

## My Explanation










