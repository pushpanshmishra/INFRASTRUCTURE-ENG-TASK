import unittest
import pandas as pd
from readtask import compute_total_revenue_per_month, compute_total_revenue_per_product, compute_total_revenue_per_customer, top_customers_by_revenue

class TestTask(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        data = {
            'order_id': [1, 2, 3],
            'customer_id': [101, 102, 101],
            'order_date': ['2023-01-15', '2023-01-17', '2023-02-05'],
            'product_id': [1001, 1002, 1001],
            'product_name': ['Widget A', 'Gadget B', 'Widget A'],
            'product_price': [25.50, 15.75, 25.50],
            'quantity': [2, 1, 3]
        }
        self.df = pd.DataFrame(data)
    
    def test_compute_total_revenue_per_month(self):
        result = compute_total_revenue_per_month(self.df)
        expected = pd.Series([92.25, 76.50], index=pd.period_range('2023-01', '2023-02', freq='M'), name='revenue').sort_index()
        pd.testing.assert_series_equal(result.sort_index(), expected)

    def test_compute_total_revenue_per_product(self):
        result = compute_total_revenue_per_product(self.df)
        expected = pd.Series([76.50, 15.75], index=['Widget A', 'Gadget B'], name='revenue').sort_index()
        pd.testing.assert_series_equal(result.sort_index(), expected)

    def test_compute_total_revenue_per_customer(self):
        result = compute_total_revenue_per_customer(self.df)
        expected = pd.Series([102.00, 15.75], index=[101, 102], name='revenue').sort_index()
        pd.testing.assert_series_equal(result.sort_index(), expected)

    def test_top_customers_by_revenue(self):
        result = top_customers_by_revenue(self.df)
        expected = pd.Series([102.00, 15.75], index=[101, 102], name='revenue').sort_values(ascending=False)
        pd.testing.assert_series_equal(result.sort_values(ascending=False), expected)

if __name__ == "__main__":
    unittest.main()
