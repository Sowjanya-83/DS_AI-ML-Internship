import pandas as pd
products = pd.Series(
    data=[700, 150, 300],
    index=['Laptop', 'Mouse', 'Keyboard']
)
laptop_price = products['Laptop']
first_two = products.iloc[0:2]

print("Full Products Series:")
print(products)

print("\nPrice of Laptop:")
print(laptop_price)

print("\nFirst Two Products (Positional Slicing):")
print(first_two)
