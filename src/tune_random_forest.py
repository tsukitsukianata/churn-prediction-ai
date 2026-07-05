from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from ml_prep import X_train, y_train

model = RandomForestClassifier(random_state=42)

param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [5, 10, None],
    "min_samples_split": [2, 5],
    "max_features": ["sqrt", "log2"]
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