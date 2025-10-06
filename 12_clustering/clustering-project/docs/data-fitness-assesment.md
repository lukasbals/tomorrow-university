# Data Fitness Assessment

## 1) Scope & Objective Alignment

- **Problem focus:** Identify countries/regions beyond DACH where the current forest carbon project methodology is climate-suitable, credible, and commercially viable for local credit buyers.
- **Decision use:** Prioritize regions for expansion; de‑risk accusations of greenwashing; support sales of high‑quality, locally resonant credits.

## 2) Dataset Overview

- **File:** `GlobalWeatherRepository.csv`
- **Records / Features:** 98214 rows / 41 columns
- **Approx. memory:** 91.06 MB in-memory
- **Inferred granularity:** national, temporal series
- **Temporal field:** `last_updated_epoch` | parsed values: 98214
- **Temporal span:** 2024-05-16 08:45:00+00:00 → 2025-10-03 06:45:00+00:00 (NA: 0.00%)
- **Geographic field (country):** `country`
- **Coordinates:** `latitude`, `longitude`

## 3) Data–Objective Alignment

- **Relevance:** Weather/climate features are directly relevant to evaluating biophysical suitability of forest projects (e.g., growth rates, risk from drought/fire, seasonality).
- **What’s missing for full decision:** Socio‑economic/forest‑management context (ownership, legal constraints, biodiversity priorities), disturbance history (fire, pests), and policy alignment (standards acceptance).

## 4) Fitness Checklist & Diagnostics

### 4.1 Feature Completeness

- Climate variables present (see numeric summary). Map each to drivers: temperature/precip for growth & stress; extremes for risk; seasonality for phenology.
- Gaps indicate need to augment with: disturbance layers, forest cover/biome mapping, and regulatory acceptance indicators.

### 4.2 Sample Representativeness (Coverage)

- Country representation (top 15 by records):

| Country     | Records |
| ----------- | ------: |
| Bulgaria    |    1081 |
| Indonesia   |    1011 |
| Sudan       |    1008 |
| Iran        |    1008 |
| Turkey      |    1007 |
| Thailand    |    1007 |
| Bolivia     |    1001 |
| Belgium     |     989 |
| Madagascar  |     963 |
| Vietnam     |     916 |
| Switzerland |     522 |
| Russia      |     518 |
| Hungary     |     509 |
| Kenya       |     506 |
| Mauritania  |     505 |

### 4.3 Temporal Alignment

- Data time span: **1970-01-01 00:00:01.715849100+00:00 → 1970-01-01 00:00:01.759473900+00:00**. Validate that this window reflects current climate conditions for decision‑making; consider using last 10 years as baseline for suitability and risk trends.

### 4.4 Quality Indicators

- **Missingness (top 15 columns):**

| Column                       | Missing % |
| ---------------------------- | --------: |
| country                      |      0.00 |
| feels_like_fahrenheit        |      0.00 |
| visibility_miles             |      0.00 |
| uv_index                     |      0.00 |
| gust_mph                     |      0.00 |
| gust_kph                     |      0.00 |
| air_quality_Carbon_Monoxide  |      0.00 |
| air_quality_Ozone            |      0.00 |
| air_quality_Nitrogen_dioxide |      0.00 |
| air_quality_Sulphur_dioxide  |      0.00 |
| air_quality_PM2.5            |      0.00 |
| air_quality_PM10             |      0.00 |
| air_quality_us-epa-index     |      0.00 |
| air_quality_gb-defra-index   |      0.00 |
| sunrise                      |      0.00 |

- **Duplicate rows:** 0.00%
- **Numeric summary (first 10 features):**

| Feature                |    count |     mean |      std |      min |      25% |      50% |      75% |      max |
| ---------------------- | -------: | -------: | -------: | -------: | -------: | -------: | -------: | -------: |
| latitude               | 9.82e+04 |     19.1 |     24.5 |    -41.3 |     3.75 |     17.2 |     40.4 |     64.2 |
| longitude              | 9.82e+04 |     22.1 |     65.8 |     -175 |    -6.84 |     23.3 |     50.6 |      179 |
| last_updated_epoch     | 9.82e+04 | 1.74e+09 | 1.26e+07 | 1.72e+09 | 1.73e+09 | 1.74e+09 | 1.75e+09 | 1.76e+09 |
| temperature_celsius    | 9.82e+04 |     22.8 |     8.89 |    -24.9 |     18.1 |       25 |     28.3 |     49.2 |
| temperature_fahrenheit | 9.82e+04 |       73 |       16 |    -12.8 |     64.6 |     76.9 |     82.9 |      121 |
| wind_mph               | 9.82e+04 |     8.23 |     7.86 |      2.2 |        4 |      6.9 |     11.4 | 1.84e+03 |
| wind_kph               | 9.82e+04 |     13.3 |     12.6 |      3.6 |      6.5 |     11.2 |     18.4 | 2.96e+03 |
| wind_degree            | 9.82e+04 |      171 |      103 |        1 |       83 |      165 |      256 |      360 |
| pressure_mb            | 9.82e+04 | 1.01e+03 |     11.4 |      947 | 1.01e+03 | 1.01e+03 | 1.02e+03 | 3.01e+03 |
| pressure_in            | 9.82e+04 |     29.9 |    0.335 |       28 |     29.8 |     29.9 |     30.1 |     88.8 |

## 5) Limitations & Bias Considerations

- **Geographic bias:** Uneven country coverage can overweight certain climates; suitability conclusions may not generalize.
- **Recency risk:** Older records may not reflect current extremes; climate trends can shift risk classes within a decade.
- **Measurement heterogeneity:** If merged from multiple networks, differences in station calibration or QA/QC can introduce inconsistency.
- **Context gap:** Purely climatic suitability ignores policy, ownership, biodiversity, and market acceptance needed for credible projects.

## 6) Mitigation Strategies

- **Augment datasets:** Join with forest/land‑cover maps (e.g., Copernicus), disturbance history (fire, pests), and governance layers (protected areas, ownership proxies).
- **Recency filter & reweight:** Emphasize last **10 years**; compute rolling normals and extreme indices to reflect current risk.
- **Spatial harmonization:** Aggregate to analysis grids (e.g., 10×10 km) to align with project siting and reduce station density bias.
- **Imputation with transparency:** Use **RobustScaler** for outlier‑resistant scaling; apply **KNN/iterative imputation** where missingness <15%; otherwise flag and exclude features from clustering, with rationale documented.
- **Representativeness weighting:** If some countries are over‑represented, weight samples by area or population of forested land during clustering.
- **Validation with domain experts:** Review preliminary clusters with local foresters to catch spurious groupings.
- **Fairness review:** Check that recommended regions don’t systematically exclude communities without monitoring infrastructure; document trade‑offs.

## 7) Decision Readiness

- The file provides **climate suitability signals**, adequate for a **first‑pass clustering** of regions by biophysical fit.
- It is **insufficient alone** for go/no‑go decisions; use it as **Tier‑1 screening**, then layer policy/market/management data before committing to projects or sales narratives.

## 8) Reproducibility & Next Steps

- Store schema, data source provenance, and refresh cadence. Re‑run this assessment at each refresh.
- Implement a data quality dashboard tracking missingness, recency, and coverage by country over time.
- Define a **feature mapping matrix** linking each clustering driver to dataset columns; maintain it in version control.

## Appendix A: Full Missingness (top 50)

| Column                       | Missing % |
| ---------------------------- | --------: |
| country                      |      0.00 |
| feels_like_fahrenheit        |      0.00 |
| visibility_miles             |      0.00 |
| uv_index                     |      0.00 |
| gust_mph                     |      0.00 |
| gust_kph                     |      0.00 |
| air_quality_Carbon_Monoxide  |      0.00 |
| air_quality_Ozone            |      0.00 |
| air_quality_Nitrogen_dioxide |      0.00 |
| air_quality_Sulphur_dioxide  |      0.00 |
| air_quality_PM2.5            |      0.00 |
| air_quality_PM10             |      0.00 |
| air_quality_us-epa-index     |      0.00 |
| air_quality_gb-defra-index   |      0.00 |
| sunrise                      |      0.00 |
| sunset                       |      0.00 |
| moonrise                     |      0.00 |
| moonset                      |      0.00 |
| moon_phase                   |      0.00 |
| visibility_km                |      0.00 |
| feels_like_celsius           |      0.00 |
| location_name                |      0.00 |
| cloud                        |      0.00 |
| latitude                     |      0.00 |
| longitude                    |      0.00 |
| timezone                     |      0.00 |
| last_updated_epoch           |      0.00 |
| last_updated                 |      0.00 |
| temperature_celsius          |      0.00 |
| temperature_fahrenheit       |      0.00 |
| condition_text               |      0.00 |
| wind_mph                     |      0.00 |
| wind_kph                     |      0.00 |
| wind_degree                  |      0.00 |
| wind_direction               |      0.00 |
| pressure_mb                  |      0.00 |
| pressure_in                  |      0.00 |
| precip_mm                    |      0.00 |
| precip_in                    |      0.00 |
| humidity                     |      0.00 |
| moon_illumination            |      0.00 |

## Appendix B: Country Coverage (top 50)

| Country                | Records |
| ---------------------- | ------: |
| Bulgaria               |    1081 |
| Indonesia              |    1011 |
| Sudan                  |    1008 |
| Iran                   |    1008 |
| Turkey                 |    1007 |
| Thailand               |    1007 |
| Bolivia                |    1001 |
| Belgium                |     989 |
| Madagascar             |     963 |
| Vietnam                |     916 |
| Switzerland            |     522 |
| Russia                 |     518 |
| Hungary                |     509 |
| Kenya                  |     506 |
| Mauritania             |     505 |
| Singapore              |     505 |
| Mauritius              |     505 |
| Senegal                |     505 |
| Poland                 |     505 |
| Oman                   |     505 |
| New Zealand            |     505 |
| Myanmar                |     505 |
| Equatorial Guinea      |     505 |
| Mozambique             |     505 |
| Eritrea                |     505 |
| Botswana               |     505 |
| Cape Verde             |     505 |
| Angola                 |     505 |
| Chad                   |     505 |
| Andorra                |     505 |
| Burundi                |     505 |
| Armenia                |     505 |
| South Africa           |     505 |
| Bosnia and Herzegovina |     505 |
| Australia              |     505 |
| Belarus                |     505 |
| Bahrain                |     505 |
| Solomon Islands        |     505 |
| Nigeria                |     505 |
| Tanzania               |     505 |
| Malaysia               |     505 |
| Marshall Islands       |     505 |
| Tuvalu                 |     505 |
| Japan                  |     505 |
| Germany                |     505 |
| Ghana                  |     505 |
| Jordan                 |     505 |
| Vatican City           |     505 |
| Kuwait                 |     505 |
| Guinea-Bissau          |     505 |
