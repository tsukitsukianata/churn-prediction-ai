from sklearn.svm import SVC
from sklearn.metrics import classification_report
from ml_prep import X_train, X_test, y_train, y_test

svm = SVC(class_weight="balanced")

svm.fit(X_train, y_train)

y_pred = svm.predict(X_test)

print(classification_report(
    y_test,
    y_pred,
    target_names=["Stayed", "Churned"]
))