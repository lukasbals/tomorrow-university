def complete_model_review(model, X_test, y_test, feature_names):
    """Run complete model review"""
    print("COMPLETE MODEL REVIEW")
    print("=" * 40)

    # Performance
    r2 = model.score(X_test, y_test)
    predictions = model.predict(X_test)
    residuals = y_test - predictions

    print(f"1. Performance: R² = {r2:.3f}")

    # Coefficients
    print("2. Coefficients:")
    for name, coef in zip(feature_names, model.coef_):
        print(f"   {name}: {coef:.3f}")

    # Residuals
    print(f"3. Residuals: Mean = {residuals.mean():.3f}")

    # Outliers
    outliers = sum(abs(residuals) > 2 * residuals.std())
    print(f"4. Outliers: {outliers} found")

    # Overall assessment
    print("\n5. OVERALL ASSESSMENT:")
    if r2 > 0.7 and abs(residuals.mean()) < 0.1:
        print("   ✅ Model ready for use")
    else:
        print("   ⚠️ Model needs improvement")
