# Milestone 4 — Model Comparison

## Objective

The objective of this milestone was to compare the performance of multiple machine learning algorithms for customer churn prediction. Rather than relying on a single model, several classification algorithms were evaluated to determine which provided the best balance between overall accuracy and the ability to correctly identify customers likely to churn.

---

## Models Evaluated

The following supervised learning algorithms were trained and evaluated using the same preprocessed training and testing datasets:

* Logistic Regression
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)
* Support Vector Machine (Balanced)

Each model was evaluated using the following metrics:

* Accuracy
* Precision
* Recall
* F1-score

Using multiple evaluation metrics provided a more complete understanding of each model's strengths and weaknesses, particularly because the Telco Customer Churn dataset is moderately imbalanced.

---

## Model Performance Comparison

| Model               |   Accuracy | Churn Precision | Churn Recall | Churn F1 |
| ------------------- | ---------: | --------------: | -----------: | -------: |
| Logistic Regression | **80.45%** |            0.65 |         0.57 | **0.61** |
| Decision Tree       |        78% |            0.58 |         0.60 |     0.59 |
| Random Forest       |        79% |            0.62 |         0.51 |     0.56 |
| SVM                 |        79% |            0.65 |         0.48 |     0.55 |
| SVM (Balanced)      |        73% |            0.49 |     **0.78** |     0.60 |

---

## Results Analysis

Several important observations were made during the comparison:

* **Logistic Regression** achieved the highest overall accuracy while also producing the strongest F1-score, making it the most balanced model overall.
* **Decision Tree** produced the highest recall among the standard models but sacrificed some overall accuracy.
* **Random Forest** improved prediction stability but did not outperform Logistic Regression on this dataset.
* **Support Vector Machine** achieved competitive accuracy but struggled to correctly identify churning customers, resulting in lower recall.
* **Balanced SVM** significantly increased recall by identifying a much larger proportion of churning customers. However, this came at the expense of both accuracy and precision, producing many more false positive predictions.

---

## Model Selection

Considering all evaluation metrics, **Logistic Regression** was selected as the strongest baseline model.

Although Balanced SVM achieved the highest recall, its lower overall accuracy and precision made it less suitable as the primary model. Logistic Regression provided the best overall trade-off between identifying churning customers and maintaining reliable predictions across both classes.

---

## Conclusion

This milestone demonstrated that different machine learning algorithms exhibit different strengths depending on the evaluation metric being considered. Rather than selecting a model based solely on accuracy, multiple metrics were analyzed to better understand each model's predictive behavior.

Based on the comparison, Logistic Regression was chosen as the leading candidate for further optimization. The next milestone focuses on improving model performance through hyperparameter tuning using GridSearchCV and cross-validation.
