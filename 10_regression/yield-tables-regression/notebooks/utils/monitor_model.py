def monitor_model(model, new_X, new_y):
    """Monitor model performance on new data"""
    predictions = model.predict(new_X)
    current_r2 = model.score(new_X, new_y)
    residuals = new_y - predictions

    print("MODEL MONITORING REPORT")
    print("=" * 30)
    print(f"Current R²: {current_r2:.3f}")
    print(f"Average error: {abs(residuals).mean():.3f}")
    print(f"Max error: {abs(residuals).max():.3f}")

    if current_r2 < 0.5:
        print("🚨 ALERT: Model performance degraded")
    elif current_r2 < 0.7:
        print("⚠️ WARNING: Monitor closely")
    else:
        print("✅ Model performing well")

    return current_r2, residuals.mean()
