import pandas as pd
from pathlib import Path

data_path = Path(__file__).resolve().parent.parent / "data" / "employees_clean.csv"

df = pd.read_csv(data_path)

print(df.head())
print(df.shape)

# KPI-1: Total Employees
total_employees = df["employee_id"].nunique()
print("Total Employees : ", total_employees)

# KPI-2: Employees who left
employees_left = (df["left_company"] == "YES").sum()
print("Employees who Left : ", employees_left)

# KPI-3: Turnover rate
turnover_rate = (employees_left / total_employees) * 100
print(f"Turnover Rate: {turnover_rate:.2f}%")

# KPI-4: Average salary by departments
average_salary_by_department = df.groupby("department")["salary"].mean()
average_salary_by_department = average_salary_by_department.sort_values(ascending=False)
print(f"Average Salary by Department:\n{average_salary_by_department.map(lambda x: f'€{x:,.2f}')}")

# KPI-5: Employee headcount by department
employees_by_department = df.groupby("department")["employee_id"].size()
employees_by_department = employees_by_department.sort_values(ascending=False)
print("Employees by Department:\n ", employees_by_department)

# KPI-6: Average performance score by department
avg_performance_by_department = df.groupby("department")["performance_score"].mean()
avg_performance_by_department = avg_performance_by_department.sort_values(ascending=False)
print("Average Performance Score by Department:\n", avg_performance_by_department)

# KPI-7: Average employee satisfaction by department
avg_satisfaction_by_department = df.groupby("department")["satisfaction_score"].mean()
avg_satisfaction_by_department = avg_satisfaction_by_department.sort_values(ascending=False)
print("Average Satisfaction Score by Department:\n", avg_satisfaction_by_department)