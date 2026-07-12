# Milestone 5 — Hyperparameter Tuning & Model Optimization

## Objective

The objective of this milestone was to improve the performance of the machine learning models by optimizing their hyperparameters. Instead of relying on the default settings provided by scikit-learn, each model was systematically tuned using **GridSearchCV** and **5-fold cross-validation**.

The goal was to identify the hyperparameter configuration that produced the best generalization performance while minimizing the risk of overfitting.

---

## Hyperparameter Tuning Approach

Hyperparameter tuning was performed using **GridSearchCV**, which evaluates multiple combinations of hyperparameters through exhaustive search.

For every hyperparameter combination:

* The training dataset was divided into five folds.
* Five training and validation cycles were performed.
* The average validation score across all folds was calculated.
* The best-performing hyperparameter combination was selected.

Initially, **accuracy** was used as the optimization metric to provide a consistent comparison across all models. Additional experiments were later conducted using **recall** to investigate how different optimization objectives influence model selection for customer churn prediction.

---

## Models Tuned

The following machine learning models were optimized:

* Logistic Regression
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)

---

## Best Hyperparameters (Accuracy Optimization)

### Logistic Regression

| Hyperparameter | Best Value |
| -------------- | ---------- |
| C              | 0.1        |
| Penalty        | L2         |
| Solver         | lbfgs      |
| Max Iterations | 1000       |

**Best Cross-Validation Accuracy:** **80.30%**

---

### Decision Tree

| Hyperparameter        | Best Value |
| --------------------- | ---------- |
| Criterion             | Gini       |
| Maximum Depth         | 3          |
| Minimum Samples Split | 2          |

**Best Cross-Validation Accuracy:** **79.06%**

---

### Random Forest

| Hyperparameter        | Best Value |
| --------------------- | ---------- |
| Number of Trees       | 100        |
| Maximum Depth         | 10         |
| Maximum Features      | sqrt       |
| Minimum Samples Split | 2          |

**Best Cross-Validation Accuracy:** **80.32%**

---

### Support Vector Machine

| Hyperparameter | Best Value |
| -------------- | ---------- |
| C              | 1          |
| Kernel         | RBF        |
| Gamma          | scale      |

**Best Cross-Validation Accuracy:** **80.20%**

---

## Tuned Model Comparison

| Model                  | Cross-Validation Accuracy |
| ---------------------- | ------------------------: |
| Random Forest          |                **80.32%** |
| Logistic Regression    |                **80.30%** |
| Support Vector Machine |                **80.20%** |
| Decision Tree          |                **79.06%** |

The difference between the top-performing models was extremely small. Random Forest achieved the highest average cross-validation accuracy, but its advantage over Logistic Regression was only **0.02%**, indicating nearly identical predictive performance.

---

## Additional Experiment: Recall Optimization

To better understand the impact of the optimization metric, GridSearchCV was also performed using **recall** instead of accuracy.

This experiment demonstrated that changing the scoring metric resulted in different hyperparameter selections and altered model behavior. Models optimized for recall identified a greater proportion of customers likely to churn but generally sacrificed overall accuracy and precision.

This highlighted an important machine learning concept: **the choice of evaluation metric should align with the business objective rather than relying solely on overall accuracy.**

---

## Final Model Selection

Although Random Forest achieved the highest cross-validation accuracy, **Logistic Regression** was selected as the final model for deployment.

The decision was based on several factors:

* Nearly identical predictive performance compared to Random Forest.
* Simpler model architecture.
* Faster training and inference.
* Easier interpretation of model predictions.
* Well suited for estimating churn probabilities, which will be used in the deployment phase.

---

## Final Test Performance

After selecting the optimal hyperparameters, the Logistic Regression model was retrained on the training dataset and evaluated on the unseen test set.

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **80.67%** |
| Precision | **65.74%** |
| Recall    | **56.95%** |
| F1-score  | **61.03%** |

The tuned model produced only a slight improvement over the baseline model, indicating that the default Logistic Regression configuration was already close to optimal for this dataset.

---

## Conclusion

This milestone introduced hyperparameter tuning using GridSearchCV and cross-validation to optimize multiple machine learning models. The experiments demonstrated how different hyperparameter combinations and evaluation metrics influence model performance.

Although tuning produced only modest performance improvements, it reinforced the importance of systematic model optimization and selecting evaluation metrics that align with the underlying business problem.

The optimized Logistic Regression model will serve as the final predictive model for deployment in the next milestone, where it will be integrated into a web application capable of generating churn predictions and customer retention recommendations.
