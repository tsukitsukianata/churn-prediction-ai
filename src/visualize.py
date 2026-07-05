import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from etl_sql import churn_by


def plot_churn(df, category_col, rate_col="churn_rate"):
    plt.figure(figsize=(8, 5))
    plt.bar(df[category_col], df[rate_col])
    plt.title(f"Churn Rate by {category_col}")
    plt.ylabel("Churn Rate")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



contract_df = churn_by("tenure")
plot_churn(contract_df, "tenure")