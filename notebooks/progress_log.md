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
