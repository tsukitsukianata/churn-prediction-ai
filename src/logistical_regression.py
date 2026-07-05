from ml_prep import X_train, X_test, y_train, y_test
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

from sklearn.metrics import classification_report


import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt



model = LogisticRegression(
    C=0.1,
    penalty="l2",
    solver="lbfgs",
    max_iter=1000,
    random_state=42
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)


"""print("Accuracy:", accuracy)
print("Confusion Matrix:", cm)
print("Precision:", precision)
print("Recall:", recall)
print("F1:", f1)"""

report = classification_report(
    y_test,
    y_pred,
    target_names=["Stayed", "Churned"]
)

print(report)


#ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
#plt.show()

