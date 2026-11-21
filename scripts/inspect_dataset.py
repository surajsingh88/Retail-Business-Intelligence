
# 1. Libraries import karna
import pandas as pd 
import os
# 2. Dataset ka path
path = "data/raw"

# 3. Files ki list
files = [
    "customers.csv",
    "products.csv",
    "orders.csv",
    "sales.csv",
    "payments.csv"
]
# 4. Loop aur CSV read
for file in files:
    df = pd.read_csv(os.path.join(path, file))

# 5. Data inspection
    print("Shape:", df.shape)

    print("Columns:", df.columns.tolist())

    print(df.isnull().sum())

    print("Duplicate Rows:", df.duplicated().sum())