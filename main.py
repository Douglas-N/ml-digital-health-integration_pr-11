import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# ----------------------------------------------------------------
# Load synthetic dataset (simulating Medic Senegal exports)
# ----------------------------------------------------------------

df = pd.read_csv("data/synthetic_medic_senegal.csv")

X = df.drop("risk_label", axis=1)
y = df["risk_label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# ----------------------------------------------------------------
# Evaluation
# ----------------------------------------------------------------
print("\nModel Performance:\n")
print(classification_report(y_test, y_pred := model.predict(X_test)))

# ----------------------------------------------------------------
# Feature importance plot
# ----------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.bar(X.columns, model.feature_importances_)
plt.title("Feature Importance (Random Forest)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("feature_importance.png")

print("Feature importance plot saved as feature_importance.png")

# ----------------------------------------------------------------
# Example inference
# ----------------------------------------------------------------
sample = X_test.iloc[0:1]
prediction = model.predict(sample)[0]
print(f"\nSample Patient Prediction: {prediction}")
