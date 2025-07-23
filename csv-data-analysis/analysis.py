import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("D:/python/csv-data-analysis/sales_data.csv")

# Show first 5 rows
print("First 5 rows of the data:")
print(df.head())

# Show shape of the dataset
print("\nShape of the DataFrame (rows, columns):", df.shape)

# Create a new column for total sales
df["Sales"] = df["Quantity"] * df["Price"]

# Group by Category and show total sales
category_sales = df.groupby("Category")["Sales"].sum()
print("\nTotal Sales by Category:")
print(category_sales)

# Group by Product and show total sales
product_sales = df.groupby("Product")["Sales"].sum()
print("\nTotal Sales by Product:")
print(product_sales)

# Plot category-wise sales
category_sales.plot(kind="bar", title="Sales by Category", ylabel="Total Sales", xlabel="Category", color="skyblue")
plt.tight_layout()
plt.show()
