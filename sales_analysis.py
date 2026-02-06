import pandas as pd

# Data: Simulating real-world sales transactions
# Veri: Gerçek dünya satış işlemlerini simüle ediyoruz
data = {
    'Product_Name': ['iPhone 15', 'Samsung S23', 'iPhone 15', 'MacBook Air', 'Samsung S23', 'iPhone 15'],
    'Sales_Count': [10, 5, 8, 2, 7, 12]
}

# Create DataFrame / Veri Çerçevesi Oluşturma
df = pd.DataFrame(data)

# Grouping and Summing / Gruplama ve Toplama
# This merges duplicate product entries / Tekrar eden ürün girişlerini birleştirir
total_sales = df.groupby('Product_Name')['Sales_Count'].sum().reset_index()

# Finding the winner / Kazananı bulma
best_seller = total_sales.sort_values(by='Sales_Count', ascending=False).iloc[0]

print("--- Total Sales Table / Toplam Satış Tablosu ---")
print(total_sales)
print("-" * 30)
print(f"The Best Seller is: {best_seller['Product_Name']} with {best_seller['Sales_Count']} units.")
