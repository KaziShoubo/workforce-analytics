import pandas as pd
import numpy as np
from pathlib import Path

"""
Select a column--> df["column"]
Filter rows--> df[df["column"] > 85 ]
Group data--> df.groupby("column")["column"].mean()
Analyze filtered data--> filtered_data["column"].mean()
"""

# load dataset
data_path = Path(__file__).resolve().parent.parent / 'data'/ "employees.csv"

df = pd.read_csv(data_path)

# number of rows and columns (row,column)
print("\ndataset shape: ")
print(df.shape)

# first 5 employees
print("\nFirst 10 employees: ")
# print(df.head())  # by default head() provides 5 rows
print(df.head(10))

# Columns name
print("\nColumns name: ")
print(df.columns)

# data types
print("\nData types:")
print(df.dtypes)

# Missing data
print("\nMissing values:")
print(df.isnull().sum())

# How much information do we have about each column?
print("\nDataset information:")
df.info()


# ==========================================
# Business Questions
# ==========================================
print("\n======Business Questions======")

#
print("\n1. Average salary")
print(df["salary"].mean())

# 2. Employees per department
print("\n2. Employees per department")
print(df["department"].value_counts())


# 3. Average age
print("\n3. Average age")
print(df["age"].mean())

# 4. Employees who left
print("\n4. Employees who left")
var = df[df["left_company"] == "Yes"]
print(var.shape[0])


# 5. Average performance score
print("\n5. Average performance score")
print(df["performance_score"].mean())

# How does salary differ between departments?
print("\nAverage salary by departments: ")
var = df.groupby("department")["salary"].mean()
print(var)


# ==========================================
# Department Analysis
# ==========================================

print("\n====== Department Analysis ======")

# 1. Number of employees per department
print("\n1. Number of employees per department")
var = df.groupby("department")["employee_id"].count()
print(var)

# 2. Average performance by department
print("\n2. Average performance by department")
var = df.groupby("department")["performance_score"].mean()
print(var)

# 3. Average satisfaction by department
print("\n3. Average satisfaction by department")
var = df.groupby("department")["satisfaction_score"].mean()
print(var)

# 4. Average salary and performance by department
print("\n4. Average salary and performance by department")
var = df.groupby("department")[["salary", "performance_score"]].mean()
print(var)

# Which employees have a performance score above 85
print("\nEmployees have a performance score above 85: ")
high_performers = df[df["performance_score"] > 85]
print(high_performers)

# 1. How many high-performing employees are there
print("\n1. How many high-performing employees are there? ")
print(high_performers.shape[0])

# 2. Which departments do the high performers belong to?
print("\n2. Which departments do the high performers belong to? ")
departments_count = high_performers["department"].value_counts()
print(departments_count)

# 3. What is their average salary?
print("\n3. What is their average salary?")
average_salary = high_performers["salary"].mean()
print(average_salary)

# Find employees who have a performance score above 85 AND earn less than €70,000.
print("\nemployees who have a performance score above 85 AND earn less than €70,000: ")
high_performers_low_salary = df[
    (df["performance_score"] > 85)
    &
    (df["salary"] < 70000)
]
print(high_performers_low_salary)
print(high_performers_low_salary.shape[0])
print(high_performers_low_salary["department"].value_counts())
print(high_performers_low_salary["salary"].mean())


# Find the 5 employees with the highest performance scores
print("\nFind the 5 employees with the highest performance scores:" )
sorted_highest_performers = (df.sort_values(
    by="performance_score",
    ascending=False
).head(5))

print(sorted_highest_performers)

# Find the 5 highest-paid employees
print("\nFind the 5 highest-paid employees:" )
sorted_highest_paid = (df.sort_values(
    by="salary",
    ascending=False
).head(5))

print("\nlist of highest paid employee: ")
print(sorted_highest_paid)

print("\nAverage performance score of the top 5 highest paid employees: ")
print(sorted_highest_paid["performance_score"].mean())

# Find the highest-paid employee in each department
print("\nFind the highest-paid employee in each department:")
highest_paid_indices = df.groupby("department")["salary"].idxmax()
highest_paid_employees = df.loc[highest_paid_indices]   # .loc retrieve the full row
print(highest_paid_employees)

# Among the highest-paid employees in each department, which one has the highest performance score
print("\nAmong the highest-paid employees in each department, which one has the highest performance score: ")
highest_performer =highest_paid_employees.sort_values(by="performance_score", ascending=False).head(1)
print(highest_performer)

# What percentage of all employees have left the company?
print("\nPercentage of employees have left the company: ")
left_company = df[df["left_company"] == "Yes"]
left_company_count = left_company.shape[0]

total_employees_count = df.shape[0]

percentage_of_left_employee = (left_company_count / total_employees_count)* 100
print(f"{percentage_of_left_employee}%")

# Number of employees who left by department
print("\nNumber of employees who left by department: ")
employee_left = df[df["left_company"] == "Yes"]
turnover_by_department = employee_left["department"].value_counts()
print(turnover_by_department)

# What is the turnover rate for each department?
print("\nthe turnover rate for each department: ")
total_employees_in_department = df.groupby("department").size()
# print(total_employees_in_department)
department_turnover_rate = (turnover_by_department/total_employees_in_department) * 100
department_turnover_rate.sort_values(ascending=False)
print(f"{department_turnover_rate}%")

# Calculate the average satisfaction score for each department and sort it from lowest to highest.
print("\nThe average satisfaction score for each department: ")
satisfaction_score_in_department = df.groupby("department")["satisfaction_score"].mean()
satisfaction_score_in_department = satisfaction_score_in_department.sort_values(ascending=True)
print(satisfaction_score_in_department)

#----------Data Cleaning---------------

# Finding missing value
print("\nMissing value in each column: ")
print(df.isnull().sum())

# Check duplicates
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

