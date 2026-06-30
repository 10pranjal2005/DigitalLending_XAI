import matplotlib.pyplot as plt


# ==========================================
# COUNTERFACTUAL DATA
# ==========================================

table_data = [

    ["CIBIL Score",
     "305",
     "700",
     "+395"],

    ["Existing Loans",
     "5",
     "2",
     "-3"],

    ["Previous Default",
     "Yes",
     "No",
     "Cleared"],

    ["Prediction",
     "Rejected",
     "Approved",
     "✓"]
]


columns = [
    "Feature",
    "Original",
    "Counterfactual",
    "Required Change"
]


# ==========================================
# CREATE FIGURE
# ==========================================

fig, ax = plt.subplots(
    figsize=(10,4)
)

ax.axis('off')


table = ax.table(
    cellText=table_data,
    colLabels=columns,
    cellLoc='center',
    loc='center'
)


# ==========================================
# STYLING
# ==========================================

table.auto_set_font_size(
    False
)

table.set_fontsize(
    12
)

table.scale(
    1.2,
    2
)


# Header row
for i in range(len(columns)):

    table[(0,i)].set_facecolor(
        "#2E86C1"
    )

    table[(0,i)].set_text_props(
        color='white',
        weight='bold'
    )


# Original column
for i in range(1,5):

    table[(i,1)].set_facecolor(
        "#FADBD8"
    )


# Counterfactual column
for i in range(1,5):

    table[(i,2)].set_facecolor(
        "#D5F5E3"
    )


# Change column
for i in range(1,5):

    table[(i,3)].set_facecolor(
        "#FCF3CF"
    )


plt.title(
    "Counterfactual Explanation for Loan Approval",
    fontsize=16,
    weight='bold',
    pad=20
)

plt.savefig(
    "outputs/figures/Figure14_Counterfactual_Table.png",
    dpi=300,
    bbox_inches='tight'
)

plt.show()

print(
    "\nCounterfactual table figure saved."
)