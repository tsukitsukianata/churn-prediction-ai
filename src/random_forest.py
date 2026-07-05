from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from ml_prep import X_train, X_test, y_train, y_test

forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

forest.fit(X_train, y_train)

y_pred = forest.predict(X_test)

print(classification_report(
    y_test,
    y_pred,
    target_names=["Stayed", "Churned"]
))