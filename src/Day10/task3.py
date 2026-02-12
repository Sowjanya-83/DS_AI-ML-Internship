import pandas as pd
df = pd.read_csv("customer_orders.csv")
df["Location"] = [" New York", "new york", "NEW YORK ",
                  " Los Angeles", "los angeles ", "LOS ANGELES",
                  " New York", "new york", "NEW YORK ",
                  " Los Angeles", "los angeles "]
print("Unique values BEFORE cleaning:")
print(df["Location"].unique())
df["Location"] = df["Location"].str.strip()
df["Location"] = df["Location"].str.title()
print("\nUnique values AFTER cleaning:")
print(df["Location"].unique())
