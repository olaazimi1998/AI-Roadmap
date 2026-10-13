#we have a model
x = 2
target = 10
w = 1

# prediction:
prediction = 1 * 2

#loss
# L = (predction - target)**2

# gradiant
# dl/dw = 2(prediction - target) x

#update
#laerning_rate = 0.1

#w 
#new
#​
# w = w − learning rate × gradient
#w 
#new
#​
# =1−(0.1)(−32)
#w 
#new
#​
# =4.2

#prediction
#prediction = 4.2 * 2 = 8.4

#Before:
#Prediction = 2
#Loss = 64
#
#After:
#Prediction = 8.4
#Loss = 2.56


#             ┌──────────────┐
#             │    Input     │
#             └──────┬───────┘
#                    ↓
#             ┌──────────────┐
#             │    Model     │
#             └──────┬───────┘
#                    ↓
#             ┌──────────────┐
#             │ Prediction   │
#             └──────┬───────┘
#                    ↓
#             ┌──────────────┐
#             │     Loss     │
#             └──────┬───────┘
#                    ↓
#             ┌──────────────┐
#             │ Backprop     │
#             └──────┬───────┘
#                    ↓
#             ┌──────────────┐
#             │  Gradients   │
#             └──────┬───────┘
#                    ↓
#             ┌──────────────┐
#             │ Update       │
#             │  Weights     │
#             └──────┬───────┘
#                    │
#                    └──────→ Repeat

#
#The model makes a prediction
#        ↓
#We calculate the loss
#        ↓
#We calculate gradients
#        ↓
#We update the weights
#        ↓
#The model makes a better prediction
#        ↓
#Repeat






















