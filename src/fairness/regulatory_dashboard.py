import matplotlib.pyplot as plt


metrics = [
    "Gender\nSPD",
    "Gender\nDIR",
    "State\nGap",
    "Employment\nGap",
    "Education\nGap"
]

scores = [
    0.0051,
    0.9839,
    2.25,
    0.74,
    1.15
]


plt.figure(figsize=(9,5))

plt.bar(
    metrics,
    scores
)

plt.title(
    "Regulatory Fairness Metrics Dashboard"
)

plt.ylabel(
    "Metric Value"
)

plt.xlabel(
    "Fairness Metrics"
)

plt.tight_layout()

plt.savefig(
    "outputs/figures/Figure9_RegulatoryDashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(
    "Regulatory dashboard saved."
)