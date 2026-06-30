"""
DAY 6
RBI Compliance Scorecard
"""

import matplotlib.pyplot as plt


categories = [
    "Explainability",
    "Fairness",
    "Bias\nDetection",
    "Transparency",
    "Auditability",
    "Accountability",
    "Data\nGovernance",
    "Consumer\nProtection"
]

scores = [
    100,
    100,
    100,
    95,
    90,
    95,
    90,
    100
]


plt.figure(
    figsize=(12,6)
)

bars = plt.bar(
    categories,
    scores
)

plt.title(
    "RBI Digital Lending Compliance Scorecard"
)

plt.xlabel(
    "Compliance Dimensions"
)

plt.ylabel(
    "Compliance Score"
)

plt.ylim(
    0,
    110
)

for bar in bars:

    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 1,
        str(height),
        ha='center'
    )

plt.tight_layout()

plt.savefig(
    "outputs/figures/Figure12_RBI_Compliance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(
    "\nRBI Compliance Scorecard saved."
)