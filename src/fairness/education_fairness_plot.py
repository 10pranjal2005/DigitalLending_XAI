import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(
    "data/synthetic/digital_lending_dataset.csv"
)

education = (
    df
    .groupby("education")
    ["loan_approved"]
    .mean()
    * 100
)

plt.figure(figsize=(8,5))

plt.bar(
    education.index,
    education.values
)

plt.title(
    "Education-wise Loan Approval Rate"
)

plt.xlabel(
    "Education"
)

plt.ylabel(
    "Approval Rate (%)"
)

plt.ylim(
    0,
    40
)

plt.xticks(
    rotation=20
)

plt.tight_layout()

plt.savefig(
    "outputs/figures/Figure11_EducationFairness.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(
    "Education fairness figure saved."
)