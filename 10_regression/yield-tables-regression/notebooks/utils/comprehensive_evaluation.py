from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import cross_val_score
import numpy as np


def comprehensive_evaluation(model, X_train, X_test, y_train, y_test):
    """Generate comprehensive model evaluation report"""

    # Fit model and make predictions
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Calculate all metrics
    metrics = {
        "R²": r2_score(y_test, y_pred),
        "RMSE": mean_squared_error(y_test, y_pred) ** 0.5,
        "MAE": mean_absolute_error(y_test, y_pred),
        "MAPE": np.mean(np.abs((y_test - y_pred) / y_test)) * 100,
    }

    # Cross-validation for stability
    cv_scores = cross_val_score(model, X_train, y_train, cv=5)

    # Performance summary
    print("=== MODEL EVALUATION REPORT ===")
    print(f"Model Type: {type(model).__name__}")
    print(f"Training Samples: {len(X_train)}")
    print(f"Test Samples: {len(X_test)}")
    print()

    print("Performance Metrics:")
    for metric, value in metrics.items():
        print(f"  {metric}: {value:.3f}")
    print(f"  CV R²: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")
    print()

    # Model diagnostics
    residuals = y_test - y_pred
    print("Model Diagnostics:")
    print(f"  Residual mean: {residuals.mean():.6f}")
    print(f"  Residual std: {residuals.std():.3f}")

    # Simple recommendation
    if metrics["R²"] > 0.8:
        print("✅ RECOMMENDATION: Model ready for deployment")
    elif metrics["R²"] > 0.6:
        print("⚠️  RECOMMENDATION: Model acceptable, monitor performance")
    else:
        print("❌ RECOMMENDATION: Model needs improvement")

    return metrics
