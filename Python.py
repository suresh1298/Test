import pandas as pd

# Read the CSV file
df = pd.read_csv('orders.csv')

# Convert 'Order Date' to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract month from 'Order Date'
df['Month'] = df['Order Date'].dt.month

# Compute total revenue for each order
df['Total Revenue'] = df['Product Price'] * df['Quantity']

# Group by month and sum the total revenue
monthly_revenue = df.groupby('Month')['Total Revenue'].sum()

#####################

# Compute total revenue for each order
df['Total Revenue'] = df['Product Price'] * df['Quantity']

# Group by product and sum the total revenue
product_revenue = df.groupby('Product Name')['Total Revenue'].sum()

####################

# Compute total revenue for each order
df['Total Revenue'] = df['Product Price'] * df['Quantity']

# Group by customer and sum the total revenue
customer_revenue = df.groupby('Customer ID')['Total Revenue'].sum()

####################

# Compute total revenue for each order
df['Total Revenue'] = df['Product Price'] * df['Quantity']

# Group by customer and sum the total revenue
customer_revenue = df.groupby('Customer ID')['Total Revenue'].sum()

# Sort customers by total revenue in descending order
sorted_customers = customer_revenue.sort_values(ascending=False)

# Get the top 10 customers
top_10_customers = sorted_customers.head(10)

#######################

print(monthly_revenue, product_revenue, customer_revenue, top_10_customers)
