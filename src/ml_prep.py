import sqlite3
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

numeric_cols = [
"tenure",
"MonthlyCharges",
"TotalCharges"
]

# Connect to database
conn = sqlite3.connect("churn.db")

# Load cleaned data
df = pd.read_sql_query(
    "SELECT * FROM customers",
    conn
)

conn.close()

# -----------------------------
# Explore categorical columns
# -----------------------------
"""for col in df.select_dtypes(include=["object", "string"]).columns:
    print(f"\n{col}")
    print(df[col].unique())

# -----------------------------
# Original X and y
# -----------------------------
y = df["Churn"]
X = df.drop(columns=["Churn"])

print("\nOriginal Dataset")
print("X shape:", X.shape)
print("y shape:", y.shape)

print("\nTarget distribution:")
print(y.value_counts())"""

# -----------------------------
# ML Preparation
# -----------------------------

# Remove customer ID
df = df.drop(columns=["customerID"])

# Encode target
df["Churn"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

# One-hot encode categorical features
df_encoded = pd.get_dummies(
    df,
    drop_first=True
)


#st.title("CSV Viewer")
# Show table
#st.dataframe(df_encoded, use_container_width = True)

X = df_encoded.drop(columns=["Churn"])
y = df_encoded["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)



X_train[numeric_cols] = scaler.fit_transform(
X_train[numeric_cols]
)

X_test[numeric_cols] = scaler.transform(
X_test[numeric_cols]
)

if __name__ == "main":
    print("X_train:", X_train.shape)
    print("X_test :", X_test.shape)
    print("y_train:", y_train.shape)
    print("y_test :", y_test.shape)
    print(X_train[numeric_cols].head())