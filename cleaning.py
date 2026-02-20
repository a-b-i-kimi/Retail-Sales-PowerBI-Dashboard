import pandas as pd

# Load CSV dataset
df = pd.read_csv("superstore.csv", encoding="latin1")

print("Original rows:", len(df))

# -----------------------------
# Basic Cleaning
# -----------------------------
df.drop_duplicates(inplace=True)

# Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Remove null rows
df = df.dropna(subset=['Sales','Profit','Customer ID'])

# -----------------------------
# Feature Engineering
# -----------------------------
df['order_year'] = df['Order Date'].dt.year
df['order_month'] = df['Order Date'].dt.month
df['order_day_name'] = df['Order Date'].dt.day_name()

df['profit_margin'] = (df['Profit'] / df['Sales']) * 100
df['is_loss_order'] = df['Profit'].apply(lambda x: 1 if x < 0 else 0)
df['order_value'] = df.groupby('Order ID')['Sales'].transform('sum')

# -----------------------------
# Save cleaned data
# -----------------------------
df.to_csv("cleaned_superstore.csv", index=False)

print("Cleaned rows:", len(df))
print("Cleaning completed — cleaned_superstore.csv created!")