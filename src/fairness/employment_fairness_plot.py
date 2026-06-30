import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(
    "data/synthetic/digital_lending_dataset.csv"
)

employment = (
    df
    .groupby("employment_type")
    ["loan_approved"]
    .mean()
    * 100
)

plt.figure(figsize=(8,5))

plt.bar(
    employment.index,
    employment.values
)

plt.title(
    "Employment-wise Loan Approval Rate"
)

plt.xlabel(
    "Employment Type"
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
    "outputs/figures/Figure10_EmploymentFairness.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(
    "Employment fairness figure saved."
)