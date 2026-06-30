import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(
    "data/synthetic/digital_lending_dataset.csv"
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

plt.figure(
    figsize=(10,6)
)

plt.bar(
    state_analysis.index,
    state_analysis.values
)

plt.xticks(
    rotation=45
)

plt.title(
    "State-wise Loan Approval Rate"
)

plt.xlabel(
    "State"
)

plt.ylabel(
    "Approval Rate (%)"
)

plt.ylim(
    0,
    40
)

plt.tight_layout()

plt.savefig(
    "outputs/figures/Figure8_StateFairness.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(
    "State fairness figure saved."
)