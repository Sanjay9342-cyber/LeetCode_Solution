import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    condition = ((products["low_fats"]=="Y")&(products["recyclable"]=="Y"))
    result = products.loc[condition,["product_id"]]
    return result