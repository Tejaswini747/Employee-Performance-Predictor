import pandas as pd
import numpy as np

np.random.seed(42)
n = 500

data = pd.DataFrame({
    'age': np.random.randint(22, 60, n),
    'experience': np.random.randint(1, 30, n),
    'department': np.random.choice(['HR','IT','Sales'], n),
    'training_hours': np.random.randint(10, 100, n),
    'projects': np.random.randint(1, 10, n),
    'attendance': np.random.uniform(0.7, 1.0, n)
})

# Create target
data['performance'] = np.where(
    (data['training_hours'] > 60) & (data['attendance'] > 0.9),
    'High',
    np.where(data['attendance'] > 0.8, 'Medium', 'Low')
)

data.to_csv('data/employee_data.csv', index=False)
print("Dataset created successfully!")
print(data.head())