"""
DAY 6
RBI Compliance Assessment
"""

def calculate_compliance():

    compliance = {

        "Model Explainability" : 100,
        "Fairness Assessment"  : 100,
        "Bias Detection"       : 100,
        "Transparency"         : 95,
        "Auditability"         : 90,
        "Accountability"       : 95,
        "Data Governance"      : 90,
        "Consumer Protection"  : 100

    }

    return compliance


if __name__ == "__main__":

    compliance = calculate_compliance()

    print(
        "\nRBI DIGITAL LENDING COMPLIANCE\n"
    )

    total = 0

    for item, score in compliance.items():

        print(
            f"{item:<25} : {score}"
        )

        total += score

    final_score = total / len(compliance)

    print(
        "\nOVERALL COMPLIANCE SCORE:"
    )

    print(
        round(final_score,2)
    )