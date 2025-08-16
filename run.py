import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")
cursor.executemany("""
INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)
""", [
    ("Laptop", 2, 75000),
    ("Laptop", 1, 75000),
    ("Smartphone", 3, 35000),
    ("Smartphone", 2, 35000),
    ("Headphones", 5, 2500),
    ("Headphones", 3, 2500),
    ("Office Chair", 2, 12000),
    ("Desk Lamp", 4, 1500),
    ("Desk Lamp", 2, 1500)
])

conn.commit()

query = """
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

print("Sales Summary:")
print(df)

plt.figure(figsize=(8,5))
df.plot(kind="bar", x="product", y="revenue", legend=False, color="skyblue")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("sales_chart.png")
plt.show()


conn.close()
