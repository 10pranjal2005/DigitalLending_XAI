import pandas as pd


metrics = {
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest"
    ],

    "Accuracy": [
        0.7261,
        0.9469,
        0.9630
    ],

    "Precision": [
        0.5834,
        0.9200,
        0.9548
    ],

    "Recall": [
        0.4309,
        0.9091,
        0.9254
    ],

    "F1_Score": [
        0.4957,
        0.9145,
        0.9399
    ],

    "ROC_AUC": [
        0.6455,
        0.9366,
        0.9527
    ]
}


df = pd.DataFrame(metrics)

df.to_csv(
    "outputs/metrics/model_metrics.csv",
    index=False
)

print(df)

print(
    "\nMetrics saved successfully."
)