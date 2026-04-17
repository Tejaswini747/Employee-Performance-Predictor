import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/employee_data.csv')

print(df.head())
print(df.info())
print(df.describe())

# Plot distribution
sns.countplot(x='performance', data=df)
plt.savefig('images/performance_distribution.png')
plt.show()

# Correlation
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.savefig('images/correlation.png')
plt.show()