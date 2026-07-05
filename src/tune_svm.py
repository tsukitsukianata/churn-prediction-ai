from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from ml_prep import X_train, y_train

model = SVC(random_state=42)

param_grid = {
    "C": [0.1, 1, 10],
    "kernel": ["linear", "rbf"],
    "gamma": ["scale", "auto"]
}

grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    scoring="recall",
    cv=5,
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print("Best Parameters:", grid_search.best_params_)
print("Best CV recall:", grid_search.best_score_)
print("Best Model:", grid_search.best_estimator_)