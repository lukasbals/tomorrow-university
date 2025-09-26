# Exploratory Data Analysis (EDA) and Preprocessing Report

## Executive Summary

The dataset contains **4,025 records across 6 columns** (5 numerical features, 1 categorical target).

- **No missing values** were detected after cleaning.
- **Target variable `tree_type` is nearly balanced**: 54.7% coniferous vs. 45.3% deciduous.
- **Feature relevance:** `basal_area` and `age` are the most informative predictors of class membership, while `trees_per_ha` and `dbh` contribute less.
- **Correlations:** Only one feature pair (`dbh`–`average_height`) shows high correlation; the rest provide unique information.
- **Modeling choice:** All features are retained to maximize accuracy, the most important metric for both practical and ethical reasons.  
  The dataset is well-prepared for modeling following a robust clean-up and preprocessing pipeline.

---

## Data Provenance

- **Source:** [OpenYieldTables project](https://github.com/treely/openyieldtables)
- **Volume:** 4,025 rows × 6 columns.
- **Versioning:** Single dataset snapshot.
- **License/Access:** MIT License (open source, free reuse with attribution).
- **Restrictions:** None; dataset may be used and modified freely under MIT terms.

---

## Class Distribution

- **Target variable:** `tree_type`
- **Values:**
  - Coniferous: **54.7%**
  - Deciduous: **45.3%**
- **Assessment:** The dataset is nearly balanced. No oversampling or undersampling is required.
- **Recommendation:** Use stratified k-fold cross-validation to preserve proportions during evaluation.

---

## Variable Summaries

- **Numerical features:**

  - `age`: Continuous, broad range across forest maturity.
  - `average_height`: Continuous, strongly correlated with `dbh`.
  - `dbh`: Important structural measure, correlated with `average_height`.
  - `trees_per_ha`: Right-skewed, with outliers at high densities.
  - `basal_area`: Informative feature, skewed but strongly predictive.

- **Categorical target:**
  - `tree_type` – binary (`coniferous`, `deciduous`).

---

## Key Correlations & Feature Insights

- **Mutual Information (MI) scores:**

  - `basal_area` and `age` emerge as the most informative features for predicting `tree_type`.
  - `trees_per_ha` and `dbh` show comparatively weaker relevance, while `average_height` is moderately predictive.
  - This ranking can guide feature selection and engineering, focusing model complexity on the most meaningful predictors.

- **Correlation analysis:**

  - The only highly correlated pair is `dbh` and `average_height` (correlation > 0.8). This is expected, since trees with larger diameters typically grow taller. To reduce redundancy, one of these features could be dropped in certain models.
  - All other feature pairs show only low-to-moderate correlation, suggesting they provide complementary information valuable for classification.

- **Chi-square results:** All five numerical features are statistically significant in relation to the target variable (p < 1e-50).

---

## Missing Values & Outliers

- **Missing values:** Addressed during preprocessing. Rows with missing values were dropped, and remaining empty fields were imputed.
- **Outliers:**
  - Many features contain outliers, but they reflect real forestry conditions rather than data errors.
  - Instead of dropping them, scaling strategies were applied to reduce their influence.
  - This ensures the dataset retains valuable variability while avoiding distortion in model training.

---

## Data Cleaning

- **Duplicate removal:** All duplicated rows were dropped.
- **Missing values:**
  - Rows with missing values were dropped.
  - Remaining empty fields were filled using **`SimpleImputer`** (default strategies applied depending on data type).
- **Consistency checks:** Data types were standardized (`int`/`float` for numerical features, categorical encoding for target).
- **Final dataset shape:** 4,025 rows × 6 columns after cleaning.

---

## Data Splitting

- The dataset was divided into **training (80%) and test (20%) sets**.
- **Stratified sampling** was applied to preserve the coniferous/deciduous ratio in both sets.
- **Cross-validation setup:** Stratified k-fold (k=5) was prepared for model evaluation to ensure robust performance estimates.

---

## Encoding & Scaling

- **Target encoding:**

  - `tree_type` was converted into binary values (`0 = coniferous`, `1 = deciduous`).

- **Scaling:**

  - Numerical features were scaled using **`RobustScaler`** from scikit-learn.
  - Unlike `StandardScaler`, which relies on mean and standard deviation, `RobustScaler` uses the median and interquartile range.
  - This approach is more resistant to outliers, ensuring extreme values do not dominate the learning process while still being retained in the dataset.

- **Modeling choice:**
  - All five features (`age`, `average_height`, `dbh`, `trees_per_ha`, `basal_area`) were included in the final dataset.
  - While removing correlated or weaker features could improve computational performance, accuracy — the most important metric in this forestry context — benefits from retaining all features.
  - From both a practical and ethical standpoint, maximizing accuracy reduces the risk of misclassifying a stand’s **carbon storage potential**, thereby minimizing harmful under- or over-predictions.

---
