// ==============================
// Demo Customers
// ==============================

const lowRiskCustomer = {
    gender: "Female",
    SeniorCitizen: "0",
    Partner: "Yes",
    Dependents: "Yes",
    tenure: 65,
    PhoneService: "Yes",
    MultipleLines: "Yes",
    InternetService: "DSL",
    OnlineSecurity: "Yes",
    OnlineBackup: "Yes",
    DeviceProtection: "Yes",
    TechSupport: "Yes",
    StreamingTV: "Yes",
    StreamingMovies: "Yes",
    Contract: "Two year",
    PaperlessBilling: "No",
    PaymentMethod: "Credit card (automatic)",
    MonthlyCharges: 72.50,
    TotalCharges: 4700.00
};

const mediumRiskCustomer = {
    gender: "Male",
    SeniorCitizen: "0",
    Partner: "Yes",
    Dependents: "No",
    tenure: 15,
    PhoneService: "Yes",
    MultipleLines: "No",
    InternetService: "Fiber optic",
    OnlineSecurity: "Yes",
    OnlineBackup: "No",
    DeviceProtection: "No",
    TechSupport: "No",
    StreamingTV: "Yes",
    StreamingMovies: "No",
    Contract: "One year",
    PaperlessBilling: "Yes",
    PaymentMethod: "Bank transfer (automatic)",
    MonthlyCharges: 85.25,
    TotalCharges: 1278.75
};

const highRiskCustomer = {
    gender: "Male",
    SeniorCitizen: "0",
    Partner: "No",
    Dependents: "No",
    tenure: 2,
    PhoneService: "Yes",
    MultipleLines: "No",
    InternetService: "Fiber optic",
    OnlineSecurity: "No",
    OnlineBackup: "No",
    DeviceProtection: "No",
    TechSupport: "No",
    StreamingTV: "Yes",
    StreamingMovies: "Yes",
    Contract: "Month-to-month",
    PaperlessBilling: "Yes",
    PaymentMethod: "Electronic check",
    MonthlyCharges: 95.50,
    TotalCharges: 191.00
};


// ==============================
// Fill Form Function
// ==============================

function fillForm(customer) {

    for (const key in customer) {

        const element = document.getElementById(key);

        if (element) {
            element.value = customer[key];
        }

    }

}


// ==============================
// Button Functions
// ==============================

function loadLowRisk() {
    fillForm(lowRiskCustomer);
}

function loadMediumRisk() {
    fillForm(mediumRiskCustomer);
}

function loadHighRisk() {
    fillForm(highRiskCustomer);
}