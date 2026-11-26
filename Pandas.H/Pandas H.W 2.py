import pandas as pd
import numpy as np
sales = pd.DataFrame({
    "day":      ["Пн", "Пн",
"Пн", "Вт", "Вт", "Вт"],

    "product":  ["Вода", "Сок",
"Печенье", "Вода", "Сок",
"Печенье"],
    "price":    [40, 70, 30, 40,
70, 30],
    "quantity": [12, 8, 15, 8,
9, 14],
})

print(f"Первые 3 строчки: {sales.head(3)}")
print(sales.shape)                          #1


print()
print(f"Неповторяющиеся элементы: {sales['product'].unique()}")     #2
print(sales[sales['day'] == 'Вт'])      #3


print()
water_sales = sales[sales["product"] == "Вода"]     #4
print(water_sales)

print()
goods = sales[(sales["price"] < 50) & (sales["quantity"] > 12)]
print(f"цена ниже 50 и продано меньше 12:")
print(goods)            # 5


print()
sales["revenue"] = sales['price'] * sales['quantity']
print(f"выручка:")
print(sales)        #6


print()
print(sales.sort_values(by="revenue", ascending=False))     #7

print()

summary = sales.groupby("product")[["quantity", "revenue"]].sum()
print(summary)          #8

print()
print(summary.sort_values(by=['quantity', 'revenue'], ascending=False ))    #9

print()
monday = sales[sales['day'] == 'Пн']['revenue'].sum()
tuesday = sales[sales['day'] == 'Вт']['revenue'].sum()
print("За понедельник")
print(monday)
print("За вторник:")
print(tuesday)      #10



print()
juice_revenue = summary.loc["Сок", "revenue"]
total_revenue = sales["revenue"].sum()
juice_percent = juice_revenue / total_revenue * 100
print(round(juice_percent))         #11

print()
print(f"самый популярный товар: {summary['quantity'].idxmax()}")
print(f"принес наибольшее кол-во денег: {summary['revenue'].idxmax()}")     #12