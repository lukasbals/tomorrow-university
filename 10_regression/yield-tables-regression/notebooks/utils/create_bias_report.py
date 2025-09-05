from sklearn.metrics import mean_squared_error
import numpy as np


def create_bias_report(y_pred, y_test, groups, group_names):
    """Create stakeholder-friendly bias report"""

    report = {"executive_summary": {}, "technical_details": {}, "recommendations": []}

    # Executive summary
    overall_accuracy = 1 - mean_squared_error(y_test, y_pred) / np.var(y_test)
    report["executive_summary"]["overall_performance"] = f"{overall_accuracy:.1%}"

    # Group-specific analysis
    group_performance = {}
    for i, group in enumerate(np.unique(groups)):
        mask = groups == group
        group_acc = 1 - mean_squared_error(y_test[mask], y_pred[mask]) / np.var(
            y_test[mask]
        )
        group_performance[group_names[i]] = f"{group_acc:.1%}"

    report["executive_summary"]["group_performance"] = group_performance

    # Recommendations
    # Ensure values are floats (e.g., 87.5 not '87.5%') before computing differences

    # Convert percentage strings to floats for comparison
    group_perf_floats = [
        float(val.strip("%")) / 100 for val in group_performance.values()
    ]
    max_diff = max(group_perf_floats) - min(group_perf_floats)
    if max_diff > 0.1:  # 10% difference threshold
        report["recommendations"].append("Consider bias mitigation techniques")

    return report
