"""
Train Machine Learning Models
Explainable Digital Lending Framework (XDLF)
"""

import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

import joblib


# =====================================================
# LOAD DATASET
# =====================================================

def load_dataset():

    df = pd.read_csv(
        "data/synthetic/digital_lending_dataset.csv"
    )

    return df


# =====================================================
# PREPROCESS DATA
# =====================================================

def preprocess(df):

    # remove leakage
    df = df.drop(columns=["risk_score"])

    # encode categorical columns
    categorical_columns = [
        "gender",
        "state",
        "education",
        "employment_type",
        "repayment_history",
        "loan_purpose"
    ]

    for column in categorical_columns:

        encoder = LabelEncoder()

        df[column] = encoder.fit_transform(
            df[column]
        )

    # create features and target
    X = df.drop(
        columns=[
            "loan_approved",
            "applicant_id"
        ]
    )

    y = df["loan_approved"]

    return train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )


# =====================================================
# TRAIN LOGISTIC REGRESSION
# =====================================================

def train_logistic(X_train, y_train):

    print("\nTraining Logistic Regression...")

    model = LogisticRegression(
        max_iter=2000
    )

    model.fit(X_train, y_train)

    return model


# =====================================================
# TRAIN DECISION TREE
# =====================================================

def train_decision_tree(X_train, y_train):

    print("\nTraining Decision Tree...")

    model = DecisionTreeClassifier(
        random_state=42,
        max_depth=10
    )

    model.fit(X_train, y_train)

    return model


# =====================================================
# TRAIN RANDOM FOREST
# =====================================================

def train_random_forest(X_train, y_train):

    print("\nTraining Random Forest...")

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    return model


# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    print("\nLoading dataset...\n")

    df = load_dataset()

    X_train, X_test, y_train, y_test = preprocess(df)

    logistic = train_logistic(
        X_train,
        y_train
    )

    tree = train_decision_tree(
        X_train,
        y_train
    )

    forest = train_random_forest(
        X_train,
        y_train
    )

    # save models
    joblib.dump(
        logistic,
        "outputs/models/logistic.pkl"
    )

    joblib.dump(
        tree,
        "outputs/models/decision_tree.pkl"
    )

    joblib.dump(
        forest,
        "outputs/models/random_forest.pkl"
    )

    print("\n")
    print("Models saved successfully.")