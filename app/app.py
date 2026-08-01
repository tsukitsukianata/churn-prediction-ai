from flask import Flask, render_template, request
from pathlib import Path
import joblib

from app.preprocessing import preprocess_customer
from app.recommendations import get_recommendations

# -----------------------------
# Load model artifacts
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "logistic_model.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"
FEATURE_NAMES_PATH = BASE_DIR / "models" / "feature_names.pkl"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
feature_names = joblib.load(FEATURE_NAMES_PATH)

# -----------------------------
# Create Flask app
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Home page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Prediction route
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    # Get raw form data
    form_data = request.form.to_dict()

    # Preprocess customer information
    processed_data = preprocess_customer(
        form_data,
        feature_names,
        scaler
    )

    # Make prediction
    prediction = model.predict(processed_data)[0]

    # Get probabilities
    probabilities = model.predict_proba(processed_data)[0]

    stay_probability = probabilities[0]
    churn_probability = probabilities[1]

    # Convert prediction to text
    if prediction == 1:
        prediction_text = "Customer is likely to churn."
    else:
        prediction_text = "Customer is likely to stay."

    # Generate recommendations
    recommendations = get_recommendations(
        form_data,
        churn_probability
    )

    # Build recommendation HTML
    recommendation_html = ""

    if recommendations:
        recommendation_html += "<h3>Recommended Retention Actions</h3><ul>"

        for recommendation in recommendations:
            recommendation_html += f"<li>{recommendation}</li>"

        recommendation_html += "</ul>"
    else:
        recommendation_html = (
            "<h3>Recommended Retention Actions</h3>"
            "<p>No immediate retention action is required.</p>"
        )

    # Temporary output
    return render_template(
    "result.html",
    prediction_text=prediction_text,
    stay_probability=stay_probability,
    churn_probability=churn_probability,
    recommendations=recommendations
   )


# -----------------------------
# Run Flask app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)