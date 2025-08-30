import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error


def tree_model_diagnostics(model, X_train, X_test, y_train, y_test):
    # Fit model
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Basic performance
    r2 = r2_score(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred) ** 0.5

    print(f"Model Performance:")
    print(f"  R²: {r2:.3f}")
    print(f"  RMSE: {rmse:.3f}")

    # Feature importance
    if hasattr(model, "feature_importances_"):
        importance = pd.Series(model.feature_importances_, index=X_train.columns)
        print(f"\nTop 5 features: {importance.nlargest(5).index.tolist()}")

    # Out-of-bag score (if available)
    if hasattr(model, "oob_score_") and model.oob_score_:
        print(f"  OOB Score: {model.oob_score_:.3f}")

    # Residual analysis
    residuals = y_test - y_pred
    print(f"\nResidual Analysis:")
    print(f"  Mean residual: {residuals.mean():.6f}")
    print(f"  Residual std: {residuals.std():.3f}")

    return r2, rmse
