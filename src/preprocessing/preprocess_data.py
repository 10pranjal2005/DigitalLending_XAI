"""
Preprocessing Digital Lending Dataset
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# =====================================================
# LOAD DATASET
# =====================================================

def load_dataset():

    df = pd.read_csv(
        "data/synthetic/digital_lending_dataset.csv"
    )

    return df


# =====================================================
# REMOVE DATA LEAKAGE
# =====================================================

def remove_leakage(df):

    print("\nRemoving target leakage...\n")

    df = df.drop(
        columns=[
            "risk_score"
        ]
    )

    return df

# =====================================================
# ENCODE CATEGORICAL VARIABLES
# =====================================================

def encode_features(df):

    print("\nEncoding categorical variables...\n")

    categorical_columns = [

        "gender",
        "state",
        "education",
        "employment_type",
        "repayment_history",
        "loan_purpose"
    ]

    encoders = {}

    for column in categorical_columns:

        encoder = LabelEncoder()

        df[column] = encoder.fit_transform(
            df[column]
        )

        encoders[column] = encoder

        print(
            f"{column}:",
            encoder.classes_
        )

    return df, encoders

# =====================================================
# TRAIN TEST SPLIT
# =====================================================

def split_dataset(df):

    print("\nCreating train-test split...\n")

    X = df.drop(
        columns=[
            "loan_approved",
            "applicant_id"
        ]
    )

    y = df["loan_approved"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("X_train:", X_train.shape)
    print("X_test :", X_test.shape)
    print("y_train:", y_train.shape)
    print("y_test :", y_test.shape)

    return X_train, X_test, y_train, y_test

# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    df = load_dataset()

    print("\nOriginal Shape:")
    print(df.shape)

    df = remove_leakage(df)

    print("\nAfter Leakage Removal:")
    print(df.shape)

    df, encoders = encode_features(df)

    print("\n")

    print(df.head())

    print("\n")

    print(df.dtypes)

    X_train, X_test, y_train, y_test = split_dataset(df)