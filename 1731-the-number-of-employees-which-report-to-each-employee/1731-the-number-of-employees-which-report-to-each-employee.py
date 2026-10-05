import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    by_manager = employees.groupby("reports_to",as_index=False).agg(reports_count=("reports_to","size"),average_age=("age","mean"))
    by_manager["average_age"]=(by_manager["average_age"]+1e-12).round(0)
    by_manager=by_manager.merge(employees,left_on="reports_to",right_on="employee_id",how = "left").rename(columns={"reports_to":"employee_id"})
    return by_manager[["employee_id","name","reports_count","average_age"]]