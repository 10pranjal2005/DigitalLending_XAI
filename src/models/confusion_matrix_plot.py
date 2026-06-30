import matplotlib.pyplot as plt
import numpy as np


cm = np.array([
    [6739,137],
    [233,2891]
])


plt.figure(figsize=(6,6))

plt.imshow(cm)

plt.xticks(
    [0,1],
    ["Rejected","Approved"]
)

plt.yticks(
    [0,1],
    ["Rejected","Approved"]
)

plt.xlabel(
    "Predicted Label"
)

plt.ylabel(
    "Actual Label"
)

plt.title(
    "Random Forest Confusion Matrix"
)

for i in range(2):
    for j in range(2):

        plt.text(
            j,
            i,
            str(cm[i,j]),
            ha='center',
            va='center'
        )

plt.colorbar()

plt.savefig(
    "outputs/figures/confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(
    "Confusion matrix figure saved."
)