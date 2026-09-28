import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv('indian_employee_data.csv')
print(df.head())
print(df.shape)

# Check missing values
print(df.isnull().sum())

# Fill missing values
df['Salary (INR)'] = df['Salary (INR)'].fillna(df['Salary (INR)'].mean())
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Performance Rating'] = df['Performance Rating'].fillna(
    df['Performance Rating'].mean()
)
print(df.isnull().sum())

# Check infinite values
print(np.isinf(df.select_dtypes(include='number')).sum())

# Replace infinite values
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.select_dtypes(include='number').mean(), inplace=True)
print(np.isinf(df.select_dtypes(include='number')).sum())

# Check duplicate rows
print(df.duplicated().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())

# Check negative values
print((df.select_dtypes(include='number') < 0).sum())

# Replace negative values
df['Salary (INR)'] = np.where(
    df['Salary (INR)'] < 0,
    df['Salary (INR)'].mean(),
    df['Salary (INR)']
)
print((df.select_dtypes(include='number') < 0).sum())

# Calculate IQR
Q1 = df['Salary (INR)'].quantile(0.25)
Q3 = df['Salary (INR)'].quantile(0.75)
IQR = Q3 - Q1

# Calculate bounds
LB = Q1 - 1.5 * IQR
UB = Q3 + 1.5 * IQR

# Check outliers
print(((df['Salary (INR)'] < LB) | (df['Salary (INR)'] > UB)).sum())

# Fix outliers by capping
df['Salary (INR)'] = df['Salary (INR)'].clip(lower=LB, upper=UB)
print(((df['Salary (INR)'] < LB) | (df['Salary (INR)'] > UB)).sum())

# Save cleaned dataset
df.to_csv('indian_employee_data_cleaned', index=False)
print('Data cleaning completed')