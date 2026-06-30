"""
SHAP Explainability Analysis
Explainable Digital Lending Framework (XDLF)
"""

import pandas as pd
import joblib
import shap

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
# PREPROCESS
# =====================================================

def preprocess(df):

    # remove target leakage
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

    print("Loading Random Forest model...\n")

    model = joblib.load(
        "outputs/models/random_forest.pkl"
    )

    print("Creating SHAP explainer...\n")

    explainer = shap.TreeExplainer(model)

    print("Selecting 1000 samples for SHAP analysis...\n")

    sample_data = X_test.sample(
        n=1000,
        random_state=42
    )

    print("Generating SHAP values...\n")

    shap_values = explainer.shap_values(
        sample_data
    )
    
    print("\nSHAP VERSION:")
    print(shap.__version__)

    print("\nTYPE:")
    print(type(shap_values))

    try:
        print("\nSHAPE:")
        print(shap_values.shape)
    except:
        print("\nNo direct shape.")

    if isinstance(shap_values, list):
        print("\nLIST LENGTH:")
        print(len(shap_values))

        for i in range(len(shap_values)):
            print(
                f"Class {i}:",
                shap_values[i].shape
            )

    import matplotlib.pyplot as plt

    print("\nGenerating SHAP summary plot...\n")

    plt.figure(figsize=(10, 8))

    # SHAP 0.51 binary classifier format
    shap.summary_plot(
        shap_values[:, :, 1],
        sample_data,
        show=False
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/figures/shap_summary_plot.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print("\nSHAP summary plot saved.")

    # =====================================================
    # LOCAL SHAP EXPLANATION
    # =====================================================

    print("\nGenerating local borrower explanation...\n")

    borrower_index = 0

    shap.plots.waterfall(
        shap.Explanation(
            values=shap_values[borrower_index, :, 1],
            base_values=explainer.expected_value[1],
            data=sample_data.iloc[borrower_index],
            feature_names=sample_data.columns
        ),
        show=False
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/figures/shap_waterfall_plot.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print("Waterfall plot saved.")

    print("\nSHAP analysis completed.")

    print("\nNumber of test samples:")
    print(sample_data.shape[0])

    print("\nNumber of features:")
    print(sample_data.shape[1])