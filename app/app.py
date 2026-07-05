from flask import Flask, render_template, request
from pathlib import Path
import joblib

from app.preprocessing import preprocess_customer

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

    # Temporary output
    return f"""
    <h2>Prediction Result</h2>

    <p><strong>{prediction_text}</strong></p>

    <p>Probability of Staying: {stay_probability:.2%}</p>

    <p>Probability of Churning: {churn_probability:.2%}</p>

    <br>

    <a href="/">Predict Another Customer</a>
    """


# -----------------------------
# Run Flask app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)