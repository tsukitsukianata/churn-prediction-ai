import pandas as pd
import sqlite3
from pathlib import Path

# Path of the csv file and reading it
csv_path = Path(__file__).parent.parent / 'data' / 'Telco-Customer-Churn.csv'
df = pd.read_csv(csv_path)

# Converts TotalCharges column to numeric and also replaces non-numeric with NaN (errors="coerce")
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna()

conn = sqlite3.connect("churn.db")
df.to_sql("customers", conn, if_exists="replace", index=False)

# Functions

# produces churn rate agains a specific column
def churn_by(column):
    
    if column == "tenure":
        query = """
        SELECT
        CASE
            WHEN tenure <= 12 THEN '0-12'
            WHEN tenure <= 24 THEN '13-24'
            WHEN tenure <= 48 THEN '25-48'
            ELSE '49+'
        END as tenure_group,
        AVG(CASE WHEN Churn='Yes' THEN 1.0 ELSE 0.0 END) as churn_rate
        FROM customers
        GROUP BY tenure_group;
        """
    elif column == "MonthlyCharges":
        query = """
            SELECT
        CASE
            WHEN MonthlyCharges <= 30 THEN '0-30'
            WHEN MonthlyCharges <= 60 THEN '31-60'
            WHEN MonthlyCharges <= 48 THEN '61-90'
            ELSE '91+'
        END as MonthlyCharges_group,
        AVG(CASE WHEN Churn='Yes' THEN 1.0 ELSE 0.0 END) as churn_rate
        FROM customers
        GROUP BY MonthlyCharges_group;
        """
    else:
        query = f"""
    SELECT {column},
           AVG(CASE WHEN Churn='Yes' THEN 1.0 ELSE 0.0 END) as churn_rate
    FROM customers
    GROUP BY {column};
    """
    return pd.read_sql(query, conn)

churn_by_list = ["Contract", "PaymentMethod", "InternetService", "SeniorCitizen", "PaperlessBilling", "tenure", "MonthlyCharges", "TechSupport", "OnlineSecurity", "Dependents", "Partner"]

for i in churn_by_list:
    print(churn_by(i))





