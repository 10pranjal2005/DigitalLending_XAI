"""
DAY 6
AI Governance Dashboard
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(
    "outputs/reports/audit_log.csv"
)

metrics = [
    "accuracy",
    "roc_auc",
    "fairness_dir"
]

values = [
    df["accuracy"][0],
    df["roc_auc"][0],
    df["fairness_dir"][0] * 100
]


plt.figure(
    figsize=(8,5)
)

bars = plt.bar(
    metrics,
    values
)

plt.title(
    "AI Governance Audit Dashboard"
)

plt.ylabel(
    "Score"
)

plt.ylim(
    0,
    110
)

for bar in bars:

    height = bar.get_height()

    plt.text(
        bar.get_x()+bar.get_width()/2,
        height+1,
        round(height,2),
        ha='center'
    )

plt.tight_layout()

plt.savefig(
    "outputs/figures/Figure13_Governance_Dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(
    "\nGovernance dashboard saved."
)