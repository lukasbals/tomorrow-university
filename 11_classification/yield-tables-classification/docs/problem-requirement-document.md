# Problem Requirement Document (PRD)

## Problem Statement

The decision being automated is the annual Measurement, Reporting, and Verification (MRV) of forest carbon storage for Improved Forest Management (IFM) projects. The unit of prediction is the tree species present per hectare of forest. The outcome event is the validated species composition within the last annual MRV cycle, which—combined with biomass estimates—enables calculation of carbon stocks. The prediction horizon is retrospective (one year), reflecting ex-post credit issuance. In practice: Predict whether a given hectare of forest contained specific tree species within the last annual MRV cycle using LiDAR and remote sensing data, so that we can generate accurate, cost-effective carbon stock estimates to support certification and climate finance.

## Success Metrics (~50 words + table)

Success will be measured by classification performance, cost efficiency, and stakeholder validation. The model should meet baseline accuracy standards, aim for aspirational performance, and reduce MRV costs compared to manual surveys, while ensuring compliance with carbon certification requirements.

|        Criterion        |     Baseline Target     |     Aspirational Target     |         Validation Method         |
| :---------------------: | :---------------------: | :-------------------------: | :-------------------------------: |
|    Overall Accuracy     |          ≥ 75%          |            ≥ 90%            |        Test set evaluation        |
|  F1-Score (macro avg.)  |         ≥ 0.70          |           ≥ 0.85            | Cross-validation + species review |
|  Per-Species F1-Score   | ≥ 0.65 (all major spp.) |   ≥ 0.80 (all major spp.)   |     Class-specific reporting      |
|     Cost Reduction      |  ≥ 30% vs. manual MRV   |    ≥ 50% vs. manual MRV     |       Cost-benefit analysis       |
| Certification Readiness |  Meets Verra/Gold Std.  | Exceeds certification norms |      Expert & auditor review      |

## Stakeholders & Impact (~100 words + quadrant visual)

Automating annual MRV impacts a diverse set of stakeholders. Forest owners directly benefit from more accurate and cost-effective assessments, supporting long-term forest management. Project developers gain operational efficiency and higher credibility in carbon credit markets. Third-party auditors (e.g., TÜV) benefit from standardized, verifiable outputs but may face challenges in adapting oversight practices. Indirectly, carbon buyers gain greater confidence in offsets, while communities and ecosystems benefit from improved monitoring of sustainable practices. Risks include potential over-reliance on automated outputs, reduced demand for manual surveys, and the need for stakeholder training to ensure consistent interpretation of model results.

|                       |                                                           Beneficiaries                                                           |                                  Potential Harms                                   |
| :-------------------: | :-------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------: |
|  Direct Stakeholders  | - Forest owners: reliable MRV, lower costs - Project developers: efficiency, credibility - Auditors (TÜV): standardized processes | - Auditors: adaptation burden - Developers: reputational risk if accuracy disputed |
| Indirect Stakeholders |               - Carbon credit buyers: stronger confidence - Local communities & ecosystems: improved sustainability               |                 - Field surveyors: reduced demand for manual work                  |

## Data Overview (~120 words)

List anticipated sources (e.g., "TrashNet images from Kaggle")
Estimate the 5 V’s: Volume, Variety, Velocity, Veracity, Value
Flag uncertainties for validation later

## Model Scope (~60 words)

Propose one baseline model (e.g., logistic regression)
Add a stretch model for higher performance (e.g., ensemble, fine-tuned CNN)

## Ethics & Compliance (~80 words)

The primary sensitive attribute in this project is geographic location, as yield tables are limited to Central Europe (Austria, Czechia, Hungary, Italy, Germany). This introduces potential bias, since model outputs may not generalize globally. No personal or demographic data is used, minimizing privacy concerns. Under the EU AI Act, this system qualifies as low-risk, supporting environmental monitoring. Mitigation includes clear disclosure of geographic scope, disclaimers in reporting, and a roadmap to incorporate broader datasets to improve representativeness and reduce bias.

## Deployment Context (~60 words)

Define runtime setting: real-time or batch
Note latency budget and whether predictions will be human-reviewed
All based on intended use, not dataset
