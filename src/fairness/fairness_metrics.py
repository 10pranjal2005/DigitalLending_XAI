"""
Fairness Metrics
"""

import pandas as pd


def load_dataset():

    return pd.read_csv(
        "data/synthetic/digital_lending_dataset.csv"
    )


def statistical_parity_difference(
        privileged,
        unprivileged):

    return (
        privileged
        -
        unprivileged
    )


def disparate_impact_ratio(
        privileged,
        unprivileged):

    return (
        unprivileged
        /
        privileged
    )


if __name__ == "__main__":

    print(
        "\nLoading dataset...\n"
    )

    df = load_dataset()

    male = (
        df[
            df["gender"]=="Male"
        ]
        ["loan_approved"]
        .mean()
    )

    female = (
        df[
            df["gender"]=="Female"
        ]
        ["loan_approved"]
        .mean()
    )

    spd = statistical_parity_difference(
        male,
        female
    )

    dir_score = disparate_impact_ratio(
        male,
        female
    )

    print(
        "\nGENDER FAIRNESS ANALYSIS"
    )

    print(
        "\nMale Approval Rate:"
    )

    print(
        round(
            male*100,
            2
        ),
        "%"
    )

    print(
        "\nFemale Approval Rate:"
    )

    print(
        round(
            female*100,
            2
        ),
        "%"
    )

    print(
        "\nStatistical Parity Difference:"
    )

    print(
        round(
            spd,
            4
        )
    )

    print(
        "\nDisparate Impact Ratio:"
    )

    print(
        round(
            dir_score,
            4
        )
    )