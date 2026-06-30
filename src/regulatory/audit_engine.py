"""
DAY 6
AI Audit Engine
"""

from datetime import datetime
import pandas as pd


def create_audit_log():

    audit = {

        "timestamp":
            datetime.now(),

        "model":
            "Random Forest",

        "accuracy":
            96.30,

        "roc_auc":
            95.27,

        "explainability":
            "SHAP + LIME",

        "fairness_spd":
            0.0051,

        "fairness_dir":
            0.9839,

        "gender_gap":
            0.51,

        "state_gap":
            2.25,

        "status":
            "COMPLIANT"

    }

    return audit


if __name__ == "__main__":

    print(
        "\nGenerating audit report...\n"
    )

    audit = create_audit_log()

    audit_df = pd.DataFrame(
        [audit]
    )

    audit_df.to_csv(
        "outputs/reports/audit_log.csv",
        index=False
    )

    print(
        audit_df
    )

    print(
        "\nAudit report saved."
    )