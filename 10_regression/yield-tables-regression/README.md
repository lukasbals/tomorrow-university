# About this project

## Problem

Yield tables are essential tools in forestry and agriculture, providing critical data on tree growth and productivity. They help in understanding the potential yield of different tree species under various environmental conditions. In this data science case, we aim to predict the volume of biomass per hectare for different tree species. The use case for this is that for improved forest management projects it's essential to know the biomass of forests to assess their carbon storage potential and inform sustainable management practices. From aerial laser scans (ALS) using LiDAR technology, it's possible to gain information like the average tree height, the number of trees per hectare, and other features used as feature variables in this project.

## Variables on the dataset

- `id`: The unique identifier of the yield table - refers to the tree species.
- `yield_class`: The yield class.
- `age`: The age in years.
- `dominant_height`: The dominant height in meters.
- `average_height`: The average height in meters.
- `dbh`: The diameter at breast height in centimeters.
- `taper`: The tree taper.
- `trees_per_ha`: The number of trees per hectare.
- `basal_area`: The basal area in square meters.
- `volume_per_ha`: The volume per hectare in vfm.
- `average_annual_age_increment`: The average annual increment up to a certain age in volume per hectare (vfm).
- `total_growth_performance`: The total growth performance in volume per hectare (vfm).
- `current_annual_increment`: The current annual increment in volume per hectare (vfm).
- `mean_annual_increment`: The mean annual increment in volume per hectare (vfm).

### Target and features

- Dependent Variable (Target): `volume_per_ha`
- Independent Variables (Features):
  - `id`
  - `yield_class`
  - `age`
  - `average_height`
  - `dbh`
  - `taper`
  - `trees_per_ha`
  - `volume_per_ha`

## Datasets

Open source yield table project: [https://yieldtables.org/](https://yieldtables.org/)
Link to the CSV used for the predictor: [https://github.com/treely/openyieldtables/blob/main/src/openyieldtables/data/yield_tables.csv](https://github.com/treely/openyieldtables/blob/main/src/openyieldtables/data/yield_tables.csv)

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

Format code using Black:

```shell
black notebooks
```

## Ethics

### Data source

The data source is an open source project: [https://yieldtables.org/](https://yieldtables.org/).

### License

This project is licensed under the MIT License.

### Known Biases

No known biases documented.

### Consent/Privacy

The dataset does not contain personally identifiable information (PII) and is considered safe for use in research and analysis. However, users should be aware of the potential for re-identification in aggregated data.

### Limitations

The dataset consists of yield tables, which reflect the average state of forests and may not account for local variations or specific management practices.
