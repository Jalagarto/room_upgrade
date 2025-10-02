"""
Data processing utilities for room upgrade analysis.
"""

import pandas as pd
import numpy as np
from pathlib import Path


def load_data(filepath):
    """
    Load data from a CSV file.
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        pandas.DataFrame: Loaded data
    """
    return pd.read_csv(filepath)


def preprocess_data(df):
    """
    Preprocess the room upgrade data.
    
    Args:
        df: Input DataFrame
        
    Returns:
        pandas.DataFrame: Preprocessed data
    """
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.dropna()
    
    return df


def save_processed_data(df, output_path):
    """
    Save processed data to a CSV file.
    
    Args:
        df: DataFrame to save
        output_path: Path to save the file
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
