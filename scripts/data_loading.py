import pandas as pd
import os

def load_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Data paths
    orders_path = os.path.join(os.path.join(script_dir, "..", "data", "raw", "olist_orders_dataset.csv"))
    order_items_path = os.path.join(os.path.join(script_dir, "..", "data", "raw", "olist_order_items_dataset.csv"))
    order_payments_path = os.path.join(os.path.join(script_dir, "..", "data", "raw", "olist_order_payments_dataset.csv"))
    order_reviews_path = os.path.join(os.path.join(script_dir, "..", "data", "raw", "olist_order_reviews_dataset.csv"))
    products_path = os.path.join(os.path.join(script_dir, "..", "data", "raw", "olist_products_dataset.csv"))
    customers_path = os.path.join(os.path.join(script_dir, "..", "data", "raw", "olist_customers_dataset.csv"))
    sellers_path = os.path.join(os.path.join(script_dir, "..", "data", "raw", "olist_sellers_dataset.csv"))
    geo_location_path = os.path.join(os.path.join(script_dir, "..", "data", "raw", "olist_geolocation_dataset.csv"))

    try:
        # Load the data
        orders = pd.read_csv(orders_path)
        order_items = pd.read_csv(order_items_path)
        order_payments = pd.read_csv(order_payments_path)
        order_reviews = pd.read_csv(order_reviews_path)
        products = pd.read_csv(products_path)
        customers = pd.read_csv(customers_path)
        sellers = pd.read_csv(sellers_path)
        geo_location = pd.read_csv(geo_location_path)

    except FileNotFoundError as e:
        print(f"Error: One of the files was not found. Check the file paths and retry.")
        print(f"Details: {e}")
        return None, None, None, None

    except pd.errors.EmptyDataError as e:
        print(f"Error: One of  the files is empty.")
        print(f"Details: {e}")
        return None, None, None, None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None, None, None

    return orders, order_items, order_payments, order_reviews, products, customers, sellers, geo_location

