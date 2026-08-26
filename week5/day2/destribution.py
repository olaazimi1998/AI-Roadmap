#Today we move from “where is the center?” to:
#
#“How are the data values distributed?”
#«داده‌ها چگونه در اطراف مرکز پخش شده‌اند؟»
#
#This is important for Machine Learning because the shape of your data can affect preprocessing, model assumptions, outliers, and how you interpret features.
#
# Normal Distribution — توزیع نرمال
#
#
# Poisson Distribution — توزیع پواسون
#
#
# این مفاهیم بعداً در Machine Learning و Statistics خیلی مهم می‌شوند. 

import numpy as np
data = np.random.normal(
    loc=100,
    scale=10,
    size=1000

)

print(data[0:10])

print("Mean:" , np.mean(data))
print("Std:" , np.std(data))

#1SD 68 % off the data is between 90 and 110
#2SD 95 % of  data is between 80 and 120
#3SD 99 % of data is between 70 and 130

#possion distrubution
# برای موقعیت ‌هایی مناسب است که می‌خواهیم بدانیم:
#
#ق چند بار در یک بازه مشخص اتفاق می‌افتد؟
#
#
#
#ری در یک ساعت وارد فروشگاه می‌شوند؟
#
#س در یک ساعت دریافت می‌کنیم؟
#
# در یک سیستم در یک روز اتفاق می‌افتد؟
#
#واست به یک API در یک دقیقه می‌رسد؟


request =  np.random.poisson(
    lam=10,
    size=10
)

print(request[0:10])



#Distribution
#     ↓
#داده‌ها چگونه پخش شده‌اند؟
#     ↓
#-----------------------------
#Normal              Poisson
#↓                   ↓
#داده‌های             تعداد
#پیوسته               اتفاق‌ها
#↓                   ↓
#Height              API requests
#Weight              Customers
#Scores              Errors

request = np.random.poisson(
    lam=10,
    size=20
)

print(request[0:10])
print("mean:", np.mean(request))


