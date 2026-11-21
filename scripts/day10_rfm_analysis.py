## RFM Analysis kya hai?
# Metric	Meaning
# Recency (R)	Customer ne last purchase kab kiya?
# Frequency (F)	Customer ne kitni baar purchase kiya?
# Monetary (M)	Customer ne total kitne paise spend kiye? 
import pandas as pd

# Sales data
sales = pd.read_csv("data/processed/sales_clean.csv")

# Orders data
orders = pd.read_csv("data/raw/orders.csv")

# Merge datasets
rfm_data = sales.merge(
    orders,
    on="Order_ID",
    how="left"
)

# Convert date
rfm_data["Order_Date"] = pd.to_datetime(
    rfm_data["Order_Date"]
)

print("RFM Data:")
print(rfm_data.head())

print("\nDate Range:")
print(rfm_data["Order_Date"].min())
print(rfm_data["Order_Date"].max())


# Step 2 – Recency, Frequency, Monetary calculate karo

# Reference date: dataset ki last date ke ek din baad
snapshot_date = rfm_data["Order_Date"].max() + pd.Timedelta(days=1)

# Customer-wise RFM Analysis
rfm = rfm_data.groupby("Customer_ID").agg(
    Recency=("Order_Date", lambda x: (snapshot_date - x.max()).days),
    Frequency=("Order_ID", "nunique"),
    Monetary=("Revenue", "sum")
)

print("\nCustomer RFM Analysis:")
print(rfm.head(10))

# Step 3 – RFM Scoring

# RFM Scores

rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    5,
    labels=[5, 4, 3, 2, 1]
)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
)

print("\nRFM Scores:")
print(rfm.head(10))

# Step 4 – RFM Customer Segments


# Combine RFM Scores
rfm["RFM_Total"] = (
    rfm["R_Score"].astype(int) +
    rfm["F_Score"].astype(int) +
    rfm["M_Score"].astype(int)
)

# Create Customer Segments
def customer_segment(row):
    if row["RFM_Total"] >= 12:
        return "High Value"
    elif row["RFM_Total"] >= 8:
        return "Regular"
    else:
        return "Low Value"

rfm["Customer_Segment"] = rfm.apply(
    customer_segment,
    axis=1
)

print("\nCustomer Segments:")
print(rfm[["RFM_Total", "Customer_Segment"]].head(20))

print("\nSegment Count:")
print(rfm["Customer_Segment"].value_counts())
