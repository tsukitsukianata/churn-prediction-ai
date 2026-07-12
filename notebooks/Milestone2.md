# Milestone 2: Feature Engineering & Machine Learning Preparation

## Objective

The objective of this milestone was to transform the cleaned customer dataset into a machine-learning-ready format. This included encoding categorical variables, splitting the dataset into training and testing sets, and scaling numerical features to prepare for model training.

---

## Completed

* Loaded the cleaned dataset from SQLite.
* Removed the `customerID` column since it does not provide predictive value.
* Encoded the target variable (`Churn`) into binary values (0 = No, 1 = Yes).
* Applied one-hot encoding to categorical features using `pd.get_dummies()`.
* Split the dataset into training and testing sets using an 80/20 ratio.
* Preserved the class distribution using stratified sampling.
* Standardized numerical features using `StandardScaler`.

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* SQLite

---

# Machine Learning Pipeline

> **Insert pipeline diagram here**

`images/ml_preprocessing_pipeline.png`

The preprocessing pipeline converts the raw customer dataset into a numerical format suitable for machine learning. Categorical variables are encoded, numerical features are standardized, and the dataset is divided into training and testing sets for unbiased model evaluation.

---

# Feature Engineering

### Target Encoding

The target variable (`Churn`) was converted into binary values:

| Original | Encoded |
| -------- | ------- |
| No       | 0       |
| Yes      | 1       |

---

### One-Hot Encoding

Categorical variables such as Contract, Internet Service, Payment Method, and Tech Support were transformed into binary indicator columns using one-hot encoding.

This prevents machine learning algorithms from incorrectly assuming an order between categorical values.

---

### Train/Test Split

The dataset was divided into:

* **80% Training Data**
* **20% Testing Data**

A stratified split was used to preserve the original churn distribution in both datasets.

---

### Feature Scaling

The following numerical features were standardized:

* tenure
* MonthlyCharges
* TotalCharges

Standardization ensures that features with larger numerical ranges do not dominate the learning process.

---

# Output

The preprocessing stage produced four datasets ready for model training:

* X_train
* X_test
* y_train
* y_test

These datasets will be used to train and evaluate customer churn prediction models.

---

# Next Steps

The next milestone focuses on:

* Training a Logistic Regression model.
* Evaluating model performance using Accuracy, Precision, Recall, F1-score, and ROC-AUC.
* Interpreting feature importance.
* Building the first predictive churn model.
