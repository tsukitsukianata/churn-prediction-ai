from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
import joblib
from ml_prep import scaler
from ml_prep import X_train, y_train
from pathlib import Path

feature_names = X_train.columns.tolist()
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "logistic_model.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"

model = LogisticRegression(random_state=42)

param_grid = {
    "C": [0.01, 0.1, 1, 10, 100],
    "penalty": ["l2"],
    "solver": ["lbfgs"],
    "max_iter": [1000]
}

grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    scoring="accuracy",
    cv=5,
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print("Best Parameters:", grid_search.best_params_)
print("Best CV accuracy:", grid_search.best_score_)
print("Best Model:", grid_search.best_estimator_)

joblib.dump(grid_search.best_estimator_, MODEL_PATH)
joblib.dump(scaler, SCALER_PATH)
joblib.dump(feature_names, BASE_DIR / "models" / "feature_names.pkl")

#print(X_train.columns.tolist())