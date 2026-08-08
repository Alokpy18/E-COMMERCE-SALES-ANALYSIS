import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("e-commerce sales.csv")
print(df)
print(df.isnull().sum())
print(df.duplicated().sum())

# total revenue
print(df["Revenue"].sum())
# total profit
print(df["Profit"].sum())
# average revenue
print(df["Revenue"].mean())

# top 10 products
top10 = (df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(10))
plt.figure(figsize=(10, 5))
plt.bar(top10.index, top10.values)

plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Category wise sales 
category_sales = (df.groupby("Category")["Revenue"].sum().sort_values(ascending=False))
plt.figure(figsize=(10,5))
plt.bar(category_sales.index, category_sales.values)

plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# city wise sales 
city_sales = (df.groupby("City")["Revenue"].sum().sort_values(ascending = False))
plt.figure(figsize=(10,5))
plt.bar(city_sales.index, city_sales.values)

plt.title("City Wise Sales")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# month wise sales
df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month

monthly_sales = (df.groupby("Month")["Revenue"].sum())
plt.figure(figsize=(12,6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='b')

plt.title("Month Wise Sales")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# highest profit product
highest_profit = (df.groupby("Product")["Profit"].sum().sort_values(ascending=False).head(10))
plt.figure(figsize=(10,5))
plt.bar(highest_profit.index, highest_profit.values)

plt.title("Top 10 Products by Profit")
plt.xlabel("Product")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()