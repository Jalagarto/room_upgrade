"""
Main script for running the room upgrade analysis pipeline.
"""

import argparse
from pathlib import Path
from src.data_processing import load_data, preprocess_data, save_processed_data


def main():
    parser = argparse.ArgumentParser(description='Process room upgrade data')
    parser.add_argument('--input', type=str, required=True,
                        help='Path to input CSV file')
    parser.add_argument('--output', type=str, default='data/processed/processed_data.csv',
                        help='Path to output CSV file')
    
    args = parser.parse_args()
    
    print(f"Loading data from {args.input}...")
    df = load_data(args.input)
    print(f"Loaded {len(df)} rows")
    
    print("Preprocessing data...")
    df_processed = preprocess_data(df)
    print(f"After preprocessing: {len(df_processed)} rows")
    
    print(f"Saving processed data to {args.output}...")
    save_processed_data(df_processed, args.output)
    print("Done!")


if __name__ == "__main__":
    main()
