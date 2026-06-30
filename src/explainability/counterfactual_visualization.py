import matplotlib.pyplot as plt

features = [
    "CIBIL Score",
    "Existing Loans",
    "Previous Default"
]

before = [
    305,
    5,
    1
]

after = [
    700,
    2,
    0
]

fig, ax = plt.subplots(figsize=(9,5))

x = range(len(features))

ax.bar(
    [i-0.2 for i in x],
    before,
    width=0.4,
    label="Original"
)

ax.bar(
    [i+0.2 for i in x],
    after,
    width=0.4,
    label="Counterfactual"
)

ax.set_xticks(list(x))
ax.set_xticklabels(features)

ax.set_title(
    "Counterfactual Explanation: Required Changes for Loan Approval"
)

ax.legend()

for i,v in enumerate(before):
    ax.text(i-0.2,v+5,str(v),ha='center')

for i,v in enumerate(after):
    ax.text(i+0.2,v+5,str(v),ha='center')

plt.tight_layout()

plt.savefig(
    "outputs/figures/Figure14_Counterfactual.png",
    dpi=300
)

plt.show()