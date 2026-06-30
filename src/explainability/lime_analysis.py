"""
LIME Explainability Analysis
Explainable Digital Lending Framework (XDLF)
"""

import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from lime.lime_tabular import LimeTabularExplainer


# =====================================================
# LOAD DATA
# =====================================================

def load_dataset():

    return pd.read_csv(
        "data/synthetic/digital_lending_dataset.csv"
    )


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
# MAIN
# =====================================================

if __name__ == "__main__":

    print("\nLoading dataset...\n")

    df = load_dataset()

    X_train, X_test, y_train, y_test = preprocess(df)

    print("Loading Random Forest...\n")

    model = joblib.load(
        "outputs/models/random_forest.pkl"
    )

    print("Creating LIME explainer...\n")

    explainer = LimeTabularExplainer(
        training_data=X_train.values,
        feature_names=X_train.columns,
        class_names=[
            "Rejected",
            "Approved"
        ],
        mode="classification"
    )

    borrower_index = 0

    print(
        "\nGenerating LIME explanation...\n"
    )

    explanation = explainer.explain_instance(
        X_test.iloc[borrower_index].values,
        model.predict_proba,
        num_features=10
    )

    print("\nLIME EXPLANATION:\n")

    for feature, weight in explanation.as_list():

        print(
            f"{feature:45} "
            f"{weight:.4f}"
        )

    explanation.save_to_file(
    "outputs/reports/lime_explanation.html"
    )

    import matplotlib.pyplot as plt

    fig = explanation.as_pyplot_figure()

    fig.savefig(
        "outputs/figures/Figure6_LIME.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(
        "\nLIME figure saved."
    )

    print(
        "\nLIME report saved."
    )