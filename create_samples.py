import pandas as pd

# Create sample sales data for 3 months
data_january = {
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Quantity": [2, 10, 5],
    "Price": [999.99, 25.50, 75.00]
}

data_february = {
    "Product": ["Monitor", "Laptop", "Mouse"],
    "Quantity": [3, 1, 8],
    "Price": [300.00, 999.99, 25.50]
}

data_march = {
    "Product": ["Keyboard", "Monitor", "Webcam"],
    "Quantity": [4, 2, 6],
    "Price": [75.00, 300.00, 50.00]
}

# Save each to an Excel file
pd.DataFrame(data_january).to_excel("sales_january.xlsx", index=False)
pd.DataFrame(data_february).to_excel("sales_february.xlsx", index=False)
pd.DataFrame(data_march).to_excel("sales_march.xlsx", index=False)

print("3 sample Excel files created!")