import pandas as pd

# Load dataset
df = pd.read_csv("customer_orders.csv")

# Step 1: Check initial data types
print("Data Types Before Conversion:\n")
print(df.dtypes)

# Step 2: If order_amount contains '$', remove it and convert to float
# (This will work even if there is no '$' — it won’t break)

df["order_amount"] = df["order_amount"].astype(str).str.replace("$", "", regex=False)
df["order_amount"] = df["order_amount"].astype(float)

# Step 3: Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Step 4: Check updated data types
print("\nData Types After Conversion:\n")
print(df.dtypes)
