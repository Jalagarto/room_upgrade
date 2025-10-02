# Room Upgrade - Skibookers Challenge
Data Science Challenge Project

## Project Structure

```
skibookers-challenge/
│── data/                 # CSVs (or instructions to download)
│── notebooks/            # Exploratory & final analysis
│── src/                  # Optional reusable scripts (preprocessing, ML pipeline)
│── reports/
│   └── challenge_report.pdf   # Your 5–7 page final report
│── tests/                # (Optional) Unit tests if you modularize code
│── requirements.txt      # Python dependencies
│── README.md             # This file - How to run notebooks, reproduce results
```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Jalagarto/room_upgrade.git
cd room_upgrade
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Data

Place your CSV data files in the `data/` directory. If the data needs to be downloaded, add instructions or a script in the `data/` folder.

## Running the Analysis

### Jupyter Notebooks

1. Start Jupyter:
```bash
jupyter notebook
```

2. Navigate to the `notebooks/` directory and open the analysis notebooks.

### Running Scripts

If you've modularized your code in the `src/` directory:
```bash
python src/your_script.py
```

## Testing

Run unit tests (if implemented):
```bash
python -m pytest tests/
```

## Project Components

- **data/**: Contains the datasets used for analysis
- **notebooks/**: Jupyter notebooks for exploratory data analysis and final analysis
- **src/**: Reusable Python modules and scripts
  - Preprocessing utilities
  - Machine learning pipeline
  - Helper functions
- **reports/**: Final deliverables and documentation
  - `challenge_report.pdf`: Main 5-7 page report
- **tests/**: Unit tests for code validation

## Reproducing Results

1. Follow the setup instructions above
2. Ensure all data files are in the `data/` directory
3. Run notebooks in order (check notebook names for sequence)
4. Generated outputs and visualizations will be saved automatically

## Dependencies

Key libraries used:
- pandas: Data manipulation and analysis
- numpy: Numerical computing
- scikit-learn: Machine learning algorithms
- matplotlib/seaborn: Data visualization
- jupyter: Interactive notebooks

See `requirements.txt` for the complete list.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
