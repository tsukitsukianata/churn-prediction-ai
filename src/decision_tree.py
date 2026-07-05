from sklearn.tree import DecisionTreeClassifier
from ml_prep import X_train, X_test, y_train, y_test
from sklearn.metrics import classification_report

tree = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

tree.fit(X_train, y_train)

y_pred = tree.predict(X_test)

report = classification_report(
    y_test,
    y_pred,
    target_names=["Stayed", "Churned"]
)

print(report)