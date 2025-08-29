# About this project

## Problem

Emissions of the agricultural sector contribute significantly to climate change, impacting global temperatures and weather patterns.

## Variables

- Dependent Variable (Target): Average Temperature °C: The average increasing of temperature (by year) in degrees Celsius
- Independent Variables (Features):
  - Savanna fires: Emissions from fires in savanna ecosystems.
  - Forest fires: Emissions from fires in forested areas.
  - Crop Residues: Emissions from burning or decomposing leftover plant material after crop harvesting.
  - Rice Cultivation: Emissions from methane released during rice cultivation.
  - Drained organic soils (CO2): Emissions from carbon dioxide released when draining organic soils.
  - Pesticides Manufacturing: Emissions from the production of pesticides.
  - Food Transport: Emissions from transporting food products.
  - Forestland: Land covered by forests.
  - Net Forest conversion: Change in forest area due to deforestation and afforestation.
  - Food Household Consumption: Emissions from food consumption at the household level.
  - Food Retail: Emissions from the operation of retail establishments selling food.
  - On-farm Electricity Use: Electricity consumption on farms.
  - Food Packaging: Emissions from the production and disposal of food packaging materials.
  - Agrifood Systems Waste Disposal: Emissions from waste disposal in the agrifood system.
  - Food Processing: Emissions from processing food products.
  - Fertilizers Manufacturing: Emissions from the production of fertilizers.
  - IPPU: Emissions from industrial processes and product use.
  - Manure applied to Soils: Emissions from applying animal manure to agricultural soils.
  - Manure left on Pasture: Emissions from animal manure on pasture or grazing land.
  - Manure Management: Emissions from managing and treating animal manure.
  - Fires in organic soils: Emissions from fires in organic soils.
  - Fires in humid tropical forests: Emissions from fires in humid tropical forests.
  - On-farm energy use: Energy consumption on farms.
  - Rural population: Number of people living in rural areas.
  - Urban population: Number of people living in urban areas.
  - Total Population - Male: Total number of male individuals in the population.
  - Total Population - Female: Total number of female individuals in the population.
  - total_emission: Total greenhouse gas emissions from various sources.

## Datasets

Source: [Agri-food CO2 emission dataset - Forecasting ML](https://www.kaggle.com/datasets/alessandrolobello/agri-food-co2-emission-dataset-forecasting-ml)

Description: A comprehensive dataset on agricultural CO2 emissions, merging data from the FAO and IPCC, was constructed. The dataset, analysed in a notebook, highlights the agri-food sector’s significant contribution to global emissions, emphasising the importance of addressing its environmental impact for climate change mitigation.

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

The data for this project is sourced from the [Agri-food CO2 emission dataset - Forecasting ML](https://www.kaggle.com/datasets/alessandrolobello/agri-food-co2-emission-dataset-forecasting-ml) dataset on Kaggle. This dataset contains information on CO2 emissions associated with different types of land use and meat consumption.

### License

This project is licensed under the CC0: Public Domain - see the [LICENSE](https://creativecommons.org/publicdomain/zero/1.0/).

### Known Biases

The dataset may reflect biases inherent in the data collection process, such as regional differences in reporting standards or agricultural practices. Additionally, the focus on CO2 emissions may overlook other significant environmental impacts, such as biodiversity loss or water usage.

### Consent/Privacy

The dataset does not contain personally identifiable information (PII) and is considered safe for use in research and analysis. However, users should be aware of the potential for re-identification in aggregated data.

### Limitations

- The dataset may not capture all factors influencing methane and carbon emissions, such as agricultural practices or technological advancements.
- The analysis is limited to the available data and may not generalize to other contexts or regions.
- Potential inaccuracies in the data could affect the model's predictions and insights.
