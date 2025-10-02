# Room Upgrade Data Science Challenge

A data science project for analyzing and predicting room upgrades.

## Project Structure

```
room_upgrade/
├── src/                    # Source code
│   ├── __init__.py
│   └── data_processing.py  # Data processing utilities
├── data/
│   ├── raw/               # Raw data files
│   └── processed/         # Processed data files
├── notebooks/             # Jupyter notebooks for analysis
├── requirements.txt       # Project dependencies
└── README.md
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Place your raw data in the `data/raw/` directory

3. Run data processing:
```python
from src.data_processing import load_data, preprocess_data, save_processed_data

# Load and process data
df = load_data('data/raw/your_data.csv')
df_processed = preprocess_data(df)
save_processed_data(df_processed, 'data/processed/processed_data.csv')
```

## Usage

See the notebooks directory for example analyses and workflows.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
