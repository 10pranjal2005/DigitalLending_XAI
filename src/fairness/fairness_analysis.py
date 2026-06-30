"""
Fairness Analysis
"""

import pandas as pd


def load_dataset():

    df = pd.read_csv(
        "data/synthetic/digital_lending_dataset.csv"
    )

    return df


if __name__ == "__main__":

    print("\nLoading dataset...\n")

    df = load_dataset()

    print(
        "\nDATASET SHAPE:"
    )

    print(
        df.shape
    )

    print(
        "\nOVERALL APPROVAL RATE:"
    )

    print(
        round(
            df["loan_approved"].mean()*100,
            2
        ),
        "%"
    )

    print(
        "\nAPPROVAL RATE BY GENDER:"
    )

    gender_analysis = (
        df
        .groupby("gender")
        ["loan_approved"]
        .mean()*100
    )

    print(
        gender_analysis
    )
    
    print(
    "\nAPPROVAL RATE BY EMPLOYMENT TYPE:"
)

    employment_analysis = (
        df
        .groupby("employment_type")
        ["loan_approved"]
        .mean()*100
    )

    print(
        employment_analysis
    )


    print(
        "\nAPPROVAL RATE BY EDUCATION:"
    )

    education_analysis = (
        df
        .groupby("education")
        ["loan_approved"]
        .mean()*100
    )

    print(
        education_analysis
    )


    print(
    "\nAPPROVAL RATE BY STATE:"
    )

    state_analysis = (
        (
            df
            .groupby("state")
            ["loan_approved"]
            .mean()
            * 100
        )
        .sort_values(
            ascending=False
        )
    )

    print(
        state_analysis
    )