import pandas as pd
import os

def load_data(base_path=None):
    if base_path is None:
        base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "raw")

        data_sets = {
            "orders": "orders.csv",
            "order_products_prior": "order_products__prior.csv",
            "order_products_train": "order_products__train.csv",
            "products": "products.csv",
            "aisles": "aisles.csv",
            "departments": "departments.csv"
        }

        data = {}
        for name, file in data_sets.items():
            path = os.path.join(base_path, file)
            data[name] = pd.read_csv(path)
            print(f"Loaded {name} ({data[name].shape[0]} rows), {data[name].shape[1]} columns")

        return data