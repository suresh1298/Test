import pandas as pd
import unittest

class TestOrdersAnalysis(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        data = {
            'Order ID': [1, 2, 3, 4, 5],
            'Customer ID': ['C1001', 'C1002', 'C1003', 'C1001', 'C1004'],
            'Order Date': ['2023-01-15', '2023-02-03', '2023-03-10', '2023-04-22', '2023-05-05'],
            'Product ID': ['P001', 'P002', 'P003', 'P001', 'P004'],
            'Product Name': ['Product A', 'Product B', 'Product C', 'Product A', 'Product D'],
            'Product Price': [20.00, 15.50, 30.00, 20.00, 25.00],
            'Quantity': [2, 1, 3, 1, 2]
        }
        self.df = pd.DataFrame(data)

    def test_monthly_revenue_calculation(self):
        self.df['Order Date'] = pd.to_datetime(self.df['Order Date'])
        self.df['Month'] = self.df['Order Date'].dt.month
        self.df['Total Revenue'] = self.df['Product Price'] * self.df['Quantity']
        monthly_revenue = self.df.groupby('Month')['Total Revenue'].sum()

        # Add your assertions here
        self.assertEqual(monthly_revenue[1], 40.00)
        self.assertEqual(monthly_revenue[2], 15.50)
        # Add assertions for other months

    def test_product_revenue_calculation(self):
        self.df['Total Revenue'] = self.df['Product Price'] * self.df['Quantity']
        product_revenue = self.df.groupby('Product Name')['Total Revenue'].sum()

        # Add your assertions here
        self.assertEqual(product_revenue['Product A'], 40.00)
        self.assertEqual(product_revenue['Product B'], 15.50)
        # Add assertions for other products

    def test_customer_revenue_calculation(self):
        self.df['Total Revenue'] = self.df['Product Price'] * self.df['Quantity']
        customer_revenue = self.df.groupby('Customer ID')['Total Revenue'].sum()

        # Add your assertions here
        self.assertEqual(customer_revenue['C1001'], 60.00)
        self.assertEqual(customer_revenue['C1002'], 15.50)
        # Add assertions for other customers

    def test_top_10_customers(self):
        self.df['Total Revenue'] = self.df['Product Price'] * self.df['Quantity']
        customer_revenue = self.df.groupby('Customer ID')['Total Revenue'].sum()
        sorted_customers = customer_revenue.sort_values(ascending=False)
        top_10_customers = sorted_customers.head(10)

        # Add your assertions here
        self.assertIn('C1001', top_10_customers.index)
        self.assertIn('C1004', top_10_customers.index)
        # Add assertions for other top customers

if __name__ == '__main__':
    unittest.main()
