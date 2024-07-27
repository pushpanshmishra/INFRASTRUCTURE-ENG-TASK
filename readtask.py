import pandas as pd

def read_csv(file_path):
    """Reads CSV data from the given file path."""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def compute_total_revenue_per_month(df):
    """Computes the total revenue generated by the online store for each month."""
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')
    df['revenue'] = df['product_price'] * df['quantity']
    monthly_revenue = df.groupby('month')['revenue'].sum()
    return monthly_revenue

def compute_total_revenue_per_product(df):
    """Computes the total revenue generated by each product."""
    df['revenue'] = df['product_price'] * df['quantity']
    product_revenue = df.groupby('product_name')['revenue'].sum()
    return product_revenue

def compute_total_revenue_per_customer(df):
    """Computes the total revenue generated by each customer."""
    df['revenue'] = df['product_price'] * df['quantity']
    customer_revenue = df.groupby('customer_id')['revenue'].sum()
    return customer_revenue

def top_customers_by_revenue(df, top_n=10):
    """Identifies the top N customers by revenue generated."""
    customer_revenue = compute_total_revenue_per_customer(df)
    top_customers = customer_revenue.nlargest(top_n)
    return top_customers

if __name__ == "__main__":
    file_path = 'orders.csv'
    df = read_csv(file_path)

    if df is not None:
        print("Total Revenue Per Month:")
        print(compute_total_revenue_per_month(df))

        print("\nTotal Revenue Per Product:")
        print(compute_total_revenue_per_product(df))

        print("\nTotal Revenue Per Customer:")
        print(compute_total_revenue_per_customer(df))

        print("\nTop 10 Customers by Revenue:")
        print(top_customers_by_revenue(df))
