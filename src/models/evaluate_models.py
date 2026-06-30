"""
Evaluate Machine Learning Models
Explainable Digital Lending Framework (XDLF)
"""

import joblib
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)


# =====================================================
# LOAD DATA
# =====================================================

def load_dataset():

    df = pd.read_csv(
        "data/synthetic/digital_lending_dataset.csv"
    )

    return df


# =====================================================
# PREPROCESS
# =====================================================

def preprocess(df):

    df = df.drop(columns=["risk_score"])

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
# EVALUATE
# =====================================================

def evaluate_model(name, model, X_test, y_test):

    predictions = model.predict(X_test)

    print("\n")
    print("="*60)
    print(name)
    print("="*60)

    print(
        "Accuracy :",
        round(
            accuracy_score(
                y_test,
                predictions
            ),
            4
        )
    )

    print(
        "Precision:",
        round(
            precision_score(
                y_test,
                predictions
            ),
            4
        )
    )

    print(
        "Recall   :",
        round(
            recall_score(
                y_test,
                predictions
            ),
            4
        )
    )

    print(
        "F1 Score :",
        round(
            f1_score(
                y_test,
                predictions
            ),
            4
        )
    )

    print(
        "ROC AUC  :",
        round(
            roc_auc_score(
                y_test,
                predictions
            ),
            4
        )
    )

    print("\nConfusion Matrix:")

    print(
        confusion_matrix(
            y_test,
            predictions
        )
    )


# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    df = load_dataset()

    X_train, X_test, y_train, y_test = preprocess(df)

    logistic = joblib.load(
        "outputs/models/logistic.pkl"
    )

    tree = joblib.load(
        "outputs/models/decision_tree.pkl"
    )

    forest = joblib.load(
        "outputs/models/random_forest.pkl"
    )

    evaluate_model(
        "LOGISTIC REGRESSION",
        logistic,
        X_test,
        y_test
    )

    evaluate_model(
        "DECISION TREE",
        tree,
        X_test,
        y_test
    )

    evaluate_model(
        "RANDOM FOREST",
        forest,
        X_test,
        y_test
    )