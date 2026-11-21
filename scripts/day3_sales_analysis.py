import pandas as pd 
# load cleaned sales data 
sales = pd.read_csv("data/processed/sales_clean.csv")

print("Sales Dataset Loaded Successfully")

print("total Rows :",len(sales))

print("Total Revenue :",sales["Revenue"].sum())

print("Total Profit :",sales["Profit"].sum())

print("Total Quantity Sold:", sales["Quantity"].sum())

total_orders = sales["Order_ID"].nunique()

aov = sales["Revenue"].sum() / total_orders

print("Total Orders:", total_orders)
print("Average Order Value:", aov)

# Top 10 Highest Revenue Sales

top_10_sales = sales.nlargest(10, "Revenue")

print("\nTop 10 Highest Revenue Sales:")
print(top_10_sales[["Sale_ID", "Order_ID", "Revenue", "Profit"]])

# Top 10 Highest Profit Sales

top_profit = sales.nlargest(10, "Profit")

print("\nTop 10 Highest Profit Sales:")
print(top_profit[["Sale_ID", "Revenue", "Profit"]])

# Average Profit
avg_profit = sales["Profit"].mean()

# Profit Margin
profit_margin = (
    sales["Profit"].sum() / sales["Revenue"].sum()
) * 100

print("Average Profit:", avg_profit)
print("Profit Margin:", profit_margin)