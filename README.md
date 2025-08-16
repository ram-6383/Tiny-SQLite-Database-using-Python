🛒 Task 7: Basic Sales Summary Using SQLite & Python
🎯 Objective

Use SQLite inside Python to pull simple sales information (total quantity sold, total revenue) and visualize results with a bar chart.

🛠️ Tools & Technologies

SQLite (lightweight database built into Python)

Python Libraries:

sqlite3 → for database connection & queries

pandas → for reading query results

matplotlib → for visualization

📂 Dataset

Database file: sales_data.db
Table: sales

Column	Type	Description
id	INT PK	Auto-incremented ID
product	TEXT	Product name
quantity	INT	Quantity sold
price	REAL	Price per unit
Sample Data Inserted

Laptop – qty: 3, price: 75,000

Smartphone – qty: 5, price: 35,000

Headphones – qty: 8, price: 2,500

Office Chair – qty: 2, price: 12,000

Desk Lamp – qty: 6, price: 1,500

📜 SQL Query Used
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;

📊 Example Output
Product	Total Quantity	Revenue
Laptop	3	225000.0
Smartphone	5	175000.0
Headphones	8	20000.0
Office Chair	2	24000.0
Desk Lamp	6	9000.0
📈 Visualization

A simple bar chart of revenue by product was created using matplotlib.

plt.figure(figsize=(8,5))
df.plot(kind="bar", x="product", y="revenue", legend=False, color="skyblue")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()


✅ Output: sales_chart.png

🚀 Outcomes

Learned to create and query SQLite database inside Python

Generated sales summary reports using SQL

Visualized results with a bar chart

End-to-end workflow from data → query → insights → visualization