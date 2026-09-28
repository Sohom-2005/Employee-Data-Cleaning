# Employee Data Cleaning with NumPy & Pandas

## Overview
A Python mini-project focused on cleaning an employee dataset using NumPy and Pandas. The project covers common data quality issues, including missing values, infinite values, duplicates, negative salaries, and outliers.

## Technologies Used
- Python
- NumPy
- Pandas
- Jupyter Notebook

## Dataset
**File:** `indian_employee_data.csv`

The dataset contains employee information such as:
- Employee ID
- Name
- Age
- Salary (INR)
- Experience (Years)
- City
- Department
- Performance Rating

## Data Cleaning Process

### 1. Data Loading and Inspection
- Imported the dataset using Pandas.
- Displayed the first five rows.
- Checked the dataset dimensions.

### 2. Missing Value Handling
- Identified missing values using `isnull()`.
- Filled missing Salary, Age, and Performance Rating values using their respective column means.

### 3. Infinite Value Handling
- Detected infinite values using NumPy.
- Replaced positive and negative infinity with NaN.
- Filled remaining numeric missing values using column means.

### 4. Duplicate Removal
- Identified duplicate rows using `duplicated()`.
- Removed duplicates using `drop_duplicates()`.

### 5. Negative Value Handling
- Checked for negative numeric values.
- Replaced negative salaries with the mean salary using `np.where()`.

### 6. Outlier Detection and Treatment
- Calculated Q1, Q3, and IQR for Salary.
- Determined the lower and upper bounds using the 1.5 × IQR rule.
- Capped salary outliers using Pandas `clip()`.

### 7. Exporting the Cleaned Dataset
- Exported the cleaned data to a CSV file using `to_csv()`.

## Concepts Practiced
- Data inspection
- Missing value imputation
- Infinite value handling
- Duplicate detection and removal
- Conditional replacement with NumPy
- Quantiles and IQR
- Outlier detection and capping
- Data export

## Project Structure

    Employee-Data-Cleaning/
    │
    ├── indian_employee_data.csv
    ├── indian_employee_data_cleaned.csv
    ├── employee_data_cleaning.ipynb
    └── README.md

## Objective
To practice fundamental data cleaning and preprocessing techniques using NumPy and Pandas as part of learning Python for data analytics.

## Note
This is a practice project. Mean imputation and IQR-based capping are used to demonstrate data preprocessing techniques; they are not necessarily the appropriate treatment for every real-world dataset.
