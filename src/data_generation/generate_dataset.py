"""
Synthetic Indian Digital Lending Dataset Generator
Explainable Digital Lending Framework (XDLF)
"""

import random
import pandas as pd
import numpy as np

from config import (
    NUM_RECORDS,
    STATES,
    EDUCATION,
    EMPLOYMENT,
    REPAYMENT,
    LOAN_PURPOSE,
    GENDER,
    LOAN_TENURE
)


# =====================================================
# GENERATE ONE APPLICANT
# =====================================================

def generate_applicant(applicant_id):

    applicant = {

        "applicant_id": applicant_id,

        "age": random.randint(21, 60),

        "gender": random.choice(GENDER),

        "state": random.choice(STATES),

        "education": random.choice(EDUCATION),

        "employment_type": random.choice(EMPLOYMENT),

        "annual_income":
            random.randint(200000, 3000000),

        "work_experience":
            random.randint(0, 35),

        "cibil_score":
            random.randint(300, 900),

        "existing_loans":
            random.randint(0, 5),

        "emi_ratio":
            round(random.uniform(0.10, 0.80), 2),

        "bank_balance":
            random.randint(1000, 1000000),

        "repayment_history":
            random.choice(REPAYMENT),

        "previous_default":
            random.choice([0, 1]),

        "digital_transactions":
            random.randint(10, 1000),

        "kyc_verified":
            random.choice([0, 1]),

        "fraud_risk_score":
            random.randint(1, 100),

        "loan_amount":
            random.randint(50000, 5000000),

        "loan_tenure":
            random.choice(LOAN_TENURE),

        "loan_purpose":
            random.choice(LOAN_PURPOSE)
    }

    return applicant

# =====================================================
# DIGITAL LENDING DECISION ENGINE
# =====================================================

def loan_decision_engine(applicant):

    score = 0

    # -----------------------------------
    # CIBIL SCORE
    # -----------------------------------

    if applicant["cibil_score"] >= 750:
        score += 30
    elif applicant["cibil_score"] >= 650:
        score += 15
    elif applicant["cibil_score"] >= 550:
        score += 5
    else:
        score -= 20

    # -----------------------------------
    # ANNUAL INCOME
    # -----------------------------------

    if applicant["annual_income"] >= 1000000:
        score += 20
    elif applicant["annual_income"] >= 500000:
        score += 10
    else:
        score -= 10

    # -----------------------------------
    # PREVIOUS DEFAULT
    # -----------------------------------

    if applicant["previous_default"] == 0:
        score += 20
    else:
        score -= 25

    # -----------------------------------
    # REPAYMENT HISTORY
    # -----------------------------------

    if applicant["repayment_history"] == "Excellent":
        score += 15
    elif applicant["repayment_history"] == "Good":
        score += 10
    elif applicant["repayment_history"] == "Average":
        score += 0
    else:
        score -= 20

    # -----------------------------------
    # EMI BURDEN
    # -----------------------------------

    if applicant["emi_ratio"] <= 0.40:
        score += 10
    elif applicant["emi_ratio"] <= 0.60:
        score += 0
    else:
        score -= 20

    # -----------------------------------
    # KYC
    # -----------------------------------

    if applicant["kyc_verified"] == 1:
        score += 10
    else:
        score -= 10

    # -----------------------------------
    # FRAUD SCORE
    # -----------------------------------

    if applicant["fraud_risk_score"] <= 30:
        score += 15
    elif applicant["fraud_risk_score"] <= 70:
        score += 0
    else:
        score -= 15

    # -----------------------------------
    # EXISTING LOANS
    # -----------------------------------

    if applicant["existing_loans"] <= 2:
        score += 5
    else:
        score -= 15

    # -----------------------------------
    # BANK BALANCE
    # -----------------------------------

    if applicant["bank_balance"] >= 500000:
        score += 10
    elif applicant["bank_balance"] >= 100000:
        score += 5
    else:
        score -= 5

    return score


# =====================================================
# GENERATE COMPLETE DATASET
# =====================================================

def generate_dataset():

    applicants = []

    for i in range(1, NUM_RECORDS + 1):

        applicant = generate_applicant(i)

        risk_score = loan_decision_engine(applicant)

        applicant["risk_score"] = risk_score

        applicant["loan_approved"] = (
            1 if risk_score >= 40 else 0
        )

        applicants.append(applicant)

    df = pd.DataFrame(applicants)

    return df


# =====================================================
# MAIN
# =====================================================


if __name__ == "__main__":

    print("\nGenerating synthetic dataset...\n")

    df = generate_dataset()

    print("\nFIRST 5 RECORDS:\n")
    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    print("\nLoan Approval Distribution:")
    print(df["loan_approved"].value_counts())

    print("\nApproval Percentage:")
    print(
        round(
            df["loan_approved"].mean() * 100,
            2
        ),
        "%"
    )
    
# ==========================================
# SAVE DATASET
# ==========================================

df.to_csv(
    "data/synthetic/digital_lending_dataset.csv",
    index=False
)

print("\nDataset saved successfully.")