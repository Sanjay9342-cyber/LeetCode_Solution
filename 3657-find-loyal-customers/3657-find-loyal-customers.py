import pandas as pd

def find_loyal_customers(customer_transactions: pd.DataFrame) -> pd.DataFrame:
    customer_transactions["transaction_date"]=pd.to_datetime(customer_transactions["transaction_date"])
    customer_transactions=customer_transactions.groupby("customer_id").agg(refund_count=("transaction_type",lambda x: (x=="refund").sum()),transaction_count=("transaction_id","count"),max_date=("transaction_date","max"),min_date=("transaction_date","min")).reset_index()
    return customer_transactions[(customer_transactions["transaction_count"]>=3)&((customer_transactions["max_date"]-customer_transactions["min_date"]).dt.days>=30)&(customer_transactions["transaction_count"]>5*customer_transactions["refund_count"])].sort_values("customer_id").iloc[:,[0]]