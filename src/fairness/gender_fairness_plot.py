import matplotlib.pyplot as plt


groups = [
    "Female",
    "Male"
]

approval_rates = [
    30.98,
    31.49
]


plt.figure(figsize=(7,5))

plt.bar(
    groups,
    approval_rates
)

plt.title(
    "Gender-wise Loan Approval Rate"
)

plt.xlabel(
    "Gender"
)

plt.ylabel(
    "Approval Rate (%)"
)

plt.ylim(
    0,
    40
)

plt.savefig(
    "outputs/figures/Figure7_GenderFairness.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(
    "Gender fairness figure saved."
)