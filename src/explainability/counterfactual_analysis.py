"""
Counterfactual Explainability
Explainable Digital Lending Framework
"""

import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder


# ==========================================
# LOAD DATA
# ==========================================

def load_dataset():

    df = pd.read_csv(
        "data/synthetic/digital_lending_dataset.csv"
    )

    return df


# ==========================================
# PREPROCESS
# ==========================================

def preprocess(df):

    df = df.drop(
        columns=["risk_score"]
    )

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

    return df


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    print(
        "\nLoading dataset...\n"
    )

    df = load_dataset()

    df = preprocess(df)

    print(
        "Loading Random Forest...\n"
    )

    model = joblib.load(
        "outputs/models/random_forest.pkl"
    )

    rejected = df[
        df["loan_approved"] == 0
    ]

    applicant = rejected.iloc[0].copy()

    X = applicant.drop(
        labels=[
            "loan_approved",
            "applicant_id"
        ]
    )

    prediction = model.predict(
        [X]
    )[0]

    print(
        "\nORIGINAL APPLICANT"
    )

    print(
        "\nPrediction:"
    )

    print(
        "APPROVED"
        if prediction == 1
        else "REJECTED"
    )

    print(
        "\nCIBIL:"
    )

    print(
        applicant["cibil_score"]
    )

    print(
        "\nEMI Ratio:"
    )

    print(
        applicant["emi_ratio"]
    )

    print(
        "\nExisting Loans:"
    )

    print(
        applicant["existing_loans"]
    )
    
        # ==========================================
    # COUNTERFACTUAL GENERATION
    # ==========================================

    counterfactual = applicant.copy()

    print(
        "\nGenerating counterfactual explanation...\n"
    )

    # improve credit score
    if counterfactual["cibil_score"] < 700:
        counterfactual["cibil_score"] = 700

    # reduce EMI burden
    if counterfactual["emi_ratio"] > 0.45:
        counterfactual["emi_ratio"] = 0.40

    # reduce number of loans
    if counterfactual["existing_loans"] > 2:
        counterfactual["existing_loans"] = 2

    # improve repayment history
    if counterfactual["repayment_history"] < 2:
        counterfactual["repayment_history"] = 2

    # remove defaults
    counterfactual["previous_default"] = 0

    X_cf = counterfactual.drop(
        labels=[
            "loan_approved",
            "applicant_id"
        ]
    )

    cf_prediction = model.predict(
        pd.DataFrame([X_cf])
    )[0]

    print(
        "\nCOUNTERFACTUAL APPLICANT"
    )

    print(
        "\nPrediction:"
    )

    print(
        "APPROVED"
        if cf_prediction == 1
        else "REJECTED"
    )

    print(
        "\nCIBIL:"
    )

    print(
        counterfactual["cibil_score"]
    )

    print(
        "\nEMI Ratio:"
    )

    print(
        counterfactual["emi_ratio"]
    )

    print(
        "\nExisting Loans:"
    )

    print(
        counterfactual["existing_loans"]
    )

    print(
        "\nPrevious Default:"
    )

    print(
        counterfactual["previous_default"]
    )