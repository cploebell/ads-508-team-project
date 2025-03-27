# split_data.py

import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-data", type=str)
    parser.add_argument("--output-train", type=str)
    parser.add_argument("--output-val", type=str)
    parser.add_argument("--output-test", type=str)
    args = parser.parse_args()

    # Load the cleaned dataset
    df = pd.read_csv("/opt/ml/processing/input/combined_agg.csv")

    # Split: 90% train, 10% holdout
    train, holdout = train_test_split(df, test_size=0.10, random_state=42)

    # Split holdout into 50% val, 50% test (each 5% of total)
    val, test = train_test_split(holdout, test_size=0.5, random_state=42)

    # Save outputs
    train.to_csv("/opt/ml/processing/output_train/train.csv", index=False)
    val.to_csv("/opt/ml/processing/output_val/val.csv", index=False)
    test.to_csv("/opt/ml/processing/output_test/test.csv", index=False)