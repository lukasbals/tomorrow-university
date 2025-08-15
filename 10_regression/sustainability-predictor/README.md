# About this project

## Problem

How does land use change and meat consumption influence the pollution of methane and carbon?

## Variables

- Dependent Variable (Target): Methane and carbon emissions in tons per year
- Independent Variables (Features): Land use change in square kilometers, meat consumption in tons

## Datasets

Source: [EDGAR Food Emissions](https://www.kaggle.com/datasets/amandaroseknudsen/edgarfoodemissions?resource=download)

Description: This dataset contains information on food-related greenhouse gas emissions, including methane and carbon emissions associated with different types of land use and meat consumption.

Why this dataset: It's well known and structured. Free and easy to use as it's already cleaned up, structured, and a time series dataset - ideal for regression analysis.

## How to run

Create a virtual environment:

```shell
python -m venv .venv
```

Activate the Python environment:

```shell
source .venv/bin/activate
```

Install dependencies:

```shell
pip install -r requirements.txt
```

## Ethics

### Data source

The data for this project is sourced from the [EDGAR Food Emissions](https://www.kaggle.com/datasets/amandaroseknudsen/edgarfoodemissions?resource=download) dataset on Kaggle. This dataset contains information on food-related greenhouse gas emissions, including methane and carbon emissions associated with different types of land use and meat consumption.

### License

This project is licensed under the Open Data Commons - see the [LICENSE](https://opendatacommons.org/licenses/dbcl/1-0/) file for details.

### Known Biases

The dataset may reflect existing biases in food production and consumption patterns, which could influence the analysis and model outcomes.

### Consent/Privacy

The dataset does not contain personally identifiable information (PII) and is considered safe for use in research and analysis. However, users should be aware of the potential for re-identification in aggregated data.

### Limitations

- The dataset may not capture all factors influencing methane and carbon emissions, such as agricultural practices or technological advancements.
- The analysis is limited to the available data and may not generalize to other contexts or regions.
- Potential inaccuracies in the data could affect the model's predictions and insights.
