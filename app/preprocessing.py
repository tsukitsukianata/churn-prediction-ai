import pandas as pd


def preprocess_customer(form_data, feature_names, scaler):
    """
    Convert raw HTML form data into the processed feature vector
    expected by the trained Logistic Regression model.
    """

    # Initialize every feature to 0
    features = {feature: 0 for feature in feature_names}

    # -------------------------
    # Numerical Features
    # -------------------------
    features["SeniorCitizen"] = int(form_data["SeniorCitizen"])
    features["tenure"] = float(form_data["tenure"])
    features["MonthlyCharges"] = float(form_data["MonthlyCharges"])
    features["TotalCharges"] = float(form_data["TotalCharges"])

    # -------------------------
    # Binary Features
    # -------------------------
    if form_data["gender"] == "Male":
        features["gender_Male"] = 1

    if form_data["Partner"] == "Yes":
        features["Partner_Yes"] = 1

    if form_data["Dependents"] == "Yes":
        features["Dependents_Yes"] = 1

    if form_data["PhoneService"] == "Yes":
        features["PhoneService_Yes"] = 1

    if form_data["PaperlessBilling"] == "Yes":
        features["PaperlessBilling_Yes"] = 1

    # -------------------------
    # Multiple Lines
    # -------------------------
    if form_data["MultipleLines"] == "Yes":
        features["MultipleLines_Yes"] = 1
    elif form_data["MultipleLines"] == "No phone service":
        features["MultipleLines_No phone service"] = 1

    # -------------------------
    # Internet Service
    # -------------------------
    if form_data["InternetService"] == "Fiber optic":
        features["InternetService_Fiber optic"] = 1
    elif form_data["InternetService"] == "No":
        features["InternetService_No"] = 1

    # -------------------------
    # Online Security
    # -------------------------
    if form_data["OnlineSecurity"] == "Yes":
        features["OnlineSecurity_Yes"] = 1
    elif form_data["OnlineSecurity"] == "No internet service":
        features["OnlineSecurity_No internet service"] = 1

    # -------------------------
    # Online Backup
    # -------------------------
    if form_data["OnlineBackup"] == "Yes":
        features["OnlineBackup_Yes"] = 1
    elif form_data["OnlineBackup"] == "No internet service":
        features["OnlineBackup_No internet service"] = 1

    # -------------------------
    # Device Protection
    # -------------------------
    if form_data["DeviceProtection"] == "Yes":
        features["DeviceProtection_Yes"] = 1
    elif form_data["DeviceProtection"] == "No internet service":
        features["DeviceProtection_No internet service"] = 1

    # -------------------------
    # Tech Support
    # -------------------------
    if form_data["TechSupport"] == "Yes":
        features["TechSupport_Yes"] = 1
    elif form_data["TechSupport"] == "No internet service":
        features["TechSupport_No internet service"] = 1

    # -------------------------
    # Streaming TV
    # -------------------------
    if form_data["StreamingTV"] == "Yes":
        features["StreamingTV_Yes"] = 1
    elif form_data["StreamingTV"] == "No internet service":
        features["StreamingTV_No internet service"] = 1

    # -------------------------
    # Streaming Movies
    # -------------------------
    if form_data["StreamingMovies"] == "Yes":
        features["StreamingMovies_Yes"] = 1
    elif form_data["StreamingMovies"] == "No internet service":
        features["StreamingMovies_No internet service"] = 1

    # -------------------------
    # Contract
    # -------------------------
    if form_data["Contract"] == "One year":
        features["Contract_One year"] = 1
    elif form_data["Contract"] == "Two year":
        features["Contract_Two year"] = 1

    # -------------------------
    # Payment Method
    # -------------------------
    if form_data["PaymentMethod"] == "Credit card (automatic)":
        features["PaymentMethod_Credit card (automatic)"] = 1
    elif form_data["PaymentMethod"] == "Electronic check":
        features["PaymentMethod_Electronic check"] = 1
    elif form_data["PaymentMethod"] == "Mailed check":
        features["PaymentMethod_Mailed check"] = 1

    # -------------------------
    # Create DataFrame
    # -------------------------
    df = pd.DataFrame([features])

    # Ensure correct column order
    df = df[feature_names]

    # -------------------------
    # Scale numerical columns
    # -------------------------
    numeric_cols = [
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]

    df[numeric_cols] = scaler.transform(df[numeric_cols])

    return df