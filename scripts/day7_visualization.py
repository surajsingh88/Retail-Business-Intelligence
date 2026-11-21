# Step 1: Monthly Revenue Line Chart
import pandas as pd
import matplotlib.pyplot as plt

# Sales data load karo
sales = pd.read_csv("data/processed/sales_clean.csv")

# Orders data load karo
orders = pd.read_csv("data/raw/orders.csv")

# Dono datasets merge karo
monthly_sales = sales.merge(
    orders,
    on="Order_ID",
    how="left"
)

# Date convert karo
monthly_sales["Order_Date"] = pd.to_datetime(
    monthly_sales["Order_Date"]
)

# Month-wise Revenue calculate karo
monthly_sales["Month"] = monthly_sales["Order_Date"].dt.to_period("M")

monthly_revenue = monthly_sales.groupby("Month")["Revenue"].sum()

# Line chart
plt.figure(figsize=(10, 5))

plt.plot(
    monthly_revenue.index.astype(str),
    monthly_revenue.values,
    marker="o"
)

plt.title("Monthly Revenue Analysis")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.ticklabel_format(axis="y", style="plain")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Step 2: Chart ko professional banao
plt.plot(
    monthly_revenue.index.astype(str),
    monthly_revenue.values,
    marker="o",
    linewidth=2,
    markersize=7,
    label="Monthly Revenue"
)

plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()

# Monthly Profit Bar Chart

monthly_profit = monthly_sales.groupby("Month")["Profit"].sum()

plt.figure(figsize=(10, 5))

plt.bar(
    monthly_profit.index.astype(str),
    monthly_profit.values,
    label="Monthly Profit"
)

plt.title("Monthly Profit Analysis")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.ticklabel_format(axis="y", style="plain")

plt.xticks(rotation=45)
plt.ticklabel_format(axis="y", style="plain")

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.show()

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_revenue.index.astype(str),
    monthly_revenue.values,
    marker="o",
    label="Revenue"
)

plt.plot(
    monthly_profit.index.astype(str),
    monthly_profit.values,
    marker="s",
    label="Profit"
)

plt.title("Monthly Revenue vs Profit")
plt.xlabel("Month")
plt.ylabel("Amount (₹)")
plt.xticks(rotation=45)
plt.ticklabel_format(axis="y", style="plain")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.show()