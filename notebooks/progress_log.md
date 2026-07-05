# Project Progress Log

## Milestone 1: Data Ingestion & Exploratory SQL Analysis

### Completed

* Loaded Telco Customer Churn dataset using Pandas.
* Cleaned data by converting `TotalCharges` to numeric and removing invalid rows.
* Stored cleaned data in a SQLite database (`churn.db`).
* Built reusable SQL queries for churn analysis.

### Key Findings

* Month-to-month customers have a churn rate of 42.7%.
* Customers with two-year contracts have a churn rate of only 2.8%.
* New customers (0-12 months tenure) churn at 47.7%.
* Customers without Tech Support churn at 41.6%.
* Customers without Online Security churn at 41.8%.
* Electronic check users have the highest churn rate among payment methods (45.3%).

### Next Steps

* Create visualizations for major findings.
* Engineer features for machine learning.
* Train and evaluate churn prediction models.
* Build an AI assistant that explains churn risks and recommends retention actions.



### Model tuning

# using accuracy as scoring metric 
## Logistical Regression
Best Parameters: {'C': 0.1, 'max_iter': 1000, 'penalty': 'l2', 'solver': 'lbfgs'}
Best CV Accuracy: 0.8030222222222223
Best Model: LogisticRegression(C=0.1, max_iter=1000, penalty='l2', random_state=42)

## Decision Tree
Best Parameters: {'criterion': 'gini', 'max_depth': 3, 'min_samples_split': 2}
Best CV Accuracy: 0.7905777777777778
Best Model: DecisionTreeClassifier(max_depth=3, random_state=42)

## Random Forest
Best Parameters: {'max_depth': 10, 'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 100}
Best CV Accuracy: 0.8032
Best Model: RandomForestClassifier(max_depth=10, random_state=42)

## SVM 
Best Parameters: {'C': 1, 'gamma': 'scale', 'kernel': 'rbf'}
Best CV Accuracy: 0.8019555555555555
Best Model: SVC(C=1, random_state=42)

# using recall as scoring metric
## Logistical Regression
Best Parameters: {'C': 100, 'max_iter': 1000, 'penalty': 'l2', 'solver': 'lbfgs'}
Best CV recall: 0.5505016722408026
Best Model: LogisticRegression(C=100, max_iter=1000, penalty='l2', random_state=42)

## Decision Tree
Best Parameters: {'criterion': 'entropy', 'max_depth': 3, 'min_samples_split': 2}
Best CV recall: 0.6240802675585284
Best Model: DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)

## Random Forest
Best Parameters: {'max_depth': 10, 'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 100}
Best CV recall: 0.5117056856187292
Best Model: RandomForestClassifier(max_depth=10, random_state=42)

## SVM
Best Parameters: {'C': 10, 'gamma': 'scale', 'kernel': 'linear'}
Best CV recall: 0.5331103678929765
Best Model: SVC(C=10, kernel='linear', random_state=42)