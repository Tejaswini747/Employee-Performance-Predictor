import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# Load data
df = pd.read_csv('data/employee_data.csv')

# Encode categorical columns
le = LabelEncoder()
df['department'] = le.fit_transform(df['department'])
df['performance'] = le.fit_transform(df['performance'])

# Split features and target
X = df.drop('performance', axis=1)
y = df['performance']

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)

# Classification Report
print("\nReport:\n", classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d')
plt.savefig("images/confusion_matrix.png")
plt.show()

# Save model
joblib.dump(model, 'models/model.pkl')

print("Model saved successfully!")
sample = X.iloc[0:1]
prediction = model.predict(sample)
print("Sample Prediction:", prediction)
# Accuracy
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)

# Classification Report
report = classification_report(y_test, y_pred)
print(report)

# Save Accuracy
with open("outputs/accuracy.txt", "w") as f:
    f.write(f"Accuracy: {acc}")

# Save Classification Report
with open("outputs/classification_report.txt", "w") as f:
    f.write(report)

# Save Predictions
results = X_test.copy()
results['Actual'] = y_test
results['Predicted'] = y_pred
results.to_csv("outputs/predictions.csv", index=False)

# Save Feature Importance
import pandas as pd

importance = model.feature_importances_
features = X.columns

feat_df = pd.DataFrame({
    'Feature': features,
    'Importance': importance
}).sort_values(by='Importance', ascending=False)

feat_df.to_csv("outputs/feature_importance.csv", index=False)

print("All outputs saved successfully!")