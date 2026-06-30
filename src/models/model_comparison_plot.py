import matplotlib.pyplot as plt


models = [
    "Logistic\nRegression",
    "Decision\nTree",
    "Random\nForest"
]

accuracy = [
    72.61,
    94.69,
    96.30
]


plt.figure(figsize=(8,6))

plt.bar(
    models,
    accuracy
)

plt.ylabel("Accuracy (%)")
plt.xlabel("Models")
plt.title(
    "Performance Comparison of Digital Lending Models"
)

plt.ylim(0,100)

plt.savefig(
    "outputs/figures/model_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(
    "Model comparison figure saved."
)