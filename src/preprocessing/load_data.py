"""
Load and Analyze Digital Lending Dataset
Explainable Digital Lending Framework (XDLF)
"""

import pandas as pd


# =====================================================
# LOAD DATASET
# =====================================================

def load_dataset():

    df = pd.read_csv(
        "data/synthetic/digital_lending_dataset.csv"
    )

    return df


# =====================================================
# DATASET ANALYSIS
# =====================================================

def analyze_dataset(df):

    print("\n" + "="*60)
    print("DATASET SHAPE")
    print("="*60)

    print(df.shape)

    print("\n" + "="*60)
    print("COLUMN NAMES")
    print("="*60)

    print(df.columns.tolist())

    print("\n" + "="*60)
    print("DATA TYPES")
    print("="*60)

    print(df.dtypes)

    print("\n" + "="*60)
    print("MISSING VALUES")
    print("="*60)

    print(df.isnull().sum())

    print("\n" + "="*60)
    print("LOAN APPROVAL DISTRIBUTION")
    print("="*60)

    print(df["loan_approved"].value_counts())

    print("\n" + "="*60)
    print("NUMERICAL SUMMARY")
    print("="*60)

    print(df.describe())


# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    print("\nLoading dataset...\n")

    df = load_dataset()

    analyze_dataset(df)