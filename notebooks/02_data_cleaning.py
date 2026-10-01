import pandas as pd
from pathlib import Path

data_path = Path(__file__).resolve().parent.parent / "data" / "employees_messy.csv"

df = pd.read_csv(data_path)

print(df.head())
print(df.shape)

print("\nData Types: ")
print(df.dtypes)

# Found salary datatype str  which is wired!
print("\nSalary values: ")
print(df["salary"].unique())

# Standardize salary
df["salary"] = (
    df["salary"]
    .str.replace("€", "")
    .str.replace(",", "")
)

df["salary"] = (
    df["salary"]
    .str.replace("47k", "47000")
)

df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

print(df["salary"].dtype)
print(df["salary"].unique())
print("\nMissing salaries:", df["salary"].isnull().sum())

# We will investigate 2 missing salary rows
print("\nMissing salary rows: ")
print(df[df["salary"].isnull()])

# We will assume the department wise salary median to fill out the missing salary
print("\nSalary median department wise: ")
department_salary_median = df.groupby("department")["salary"].median()
print(department_salary_median)

# We have encountered another problem with department naming, let's standardize department
print(df["department"].unique())

# Remove extra space, standardize capitalization and handle the synonym
df["department"] = df["department"].str.strip()
df["department"] = df["department"].str.upper()
df["department"] = df["department"].replace(
    {"INFORMATION TECHNOLOGY": "IT"}
)

print(df["department"].unique())
print("\nOne of the employee doesn't have a department: ")
print(df[df["department"].isna()])

# Let's deal with missing two salary rows
print(df[df["salary"].isna()])

print("\nSalary median department wise after cleaning: ")
department_salary_median_clean = df.groupby("department")["salary"].median()
print(department_salary_median_clean)

print("\nPrinting the employees who has no salary input: ")
print(df[df["salary"].isna()][["employee_id", "department", "salary"]])

# Fill the missing salaries
df["salary"] = df["salary"].fillna(  # replace the salaries that are currently NaN
    df["department"].map(department_salary_median_clean)  # creates the appropriate median for each employee based on their department.
)
print("\nChecking the employee's row after fill in salary: ")
print(df[df["employee_id"].isin(["E003", "E028"])]
      [["employee_id", "department", "salary"]])

print(df["salary"].isna().sum())

# Now let's deal with the missing department
# There is no way we know what department could this employee belong to. So, we keep it as NaN.

print("\nInvestigate employee row who has no department: ")
print(df[df["employee_id"] == "E011"].T) # Transposes the row

# Let's deal with the duplicates
print("\nInvestigate the duplicate row: ")
print(df[df.duplicated()])

# remove the duplicate row
df = df.drop_duplicates()
print("Duplicate rows: ", df.duplicated().sum())
print("Dataset shape: ", df.shape)


# Investigate and clean Inconsistent categorial columns remote_work and left_company
print("\nBefore cleaning categorial values for remote_work and left_company: ")
print(df["remote_work"].unique())
print(df["left_company"].unique())

df["remote_work"] = df["remote_work"].str.strip().str.upper()
df["left_company"] = df["left_company"].str.strip().str.upper()

print("\nAfter cleaning categorial values for remote_work and left_company: ")
print(df["remote_work"].unique())
print(df["left_company"].unique())

# Investigate and clean Inconsistent categorial column job_role
print("\nBefore cleaning categorial column job_role: ")
print(df["job_role"].unique())

df["job_role"] = df["job_role"].str.strip()
df["job_role"] = df["job_role"].replace(
    {"marketing manager": "Marketing Manager"}
)

print("\nAfter cleaning categorial column job_role: ")
print(df["job_role"].unique())

#------------validate the numerical columns-----------
print("\nInspecting the ranges of our numerical columns: ")
numeric_columns = [
    "age",
    "experience_years",
    "salary",
    "performance_score",
    "satisfaction_score",
    "absence_days"
]
pd.set_option("display.max_columns", None)
print("\nCHeck the employee who has no satisfaction score: ")
print(df[numeric_columns].describe().T)
print(df[df["satisfaction_score"].isna()])
print(
    df[df["satisfaction_score"].isna()][
        ["employee_id", "department", "job_role", "performance_score"]
    ]
)

print("\nSatisfaction_score median by department: ")
department_satisfaction_median = (
    df.groupby("department")["satisfaction_score"].median()
)

print(department_satisfaction_median)

# Filling the satisfaction_score
df["satisfaction_score"] = df["satisfaction_score"].fillna(
    df["department"].map(department_satisfaction_median)
)

print("\nMissing satisfaction scores after cleaning:")
print(df["satisfaction_score"].isna().sum())

# Investigate age
print("\nPotentially unusual ages:")
print(df[df["age"].isin([17, 72])][
    ["employee_id", "age", "job_role", "experience_years", "salary"]
])

print("\nPotentially inconsistent age/experience:")
print(
    df[df["experience_years"] > df["age"] - 15][
        ["employee_id", "age", "experience_years", "job_role"]
    ]
)

#--------Final Data Check---------
# E011 has a missing department.
# Department was left as NaN because there is not enough information
# to reliably determine the employee's department.

print("\n=== FINAL DATA QUALITY CHECK ===")

print("\nShape:")
print(df.shape)

print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

print("\nDepartment values:")
print(df["department"].unique())

print("\nRemote work values:")
print(df["remote_work"].unique())

print("\nLeft company values:")
print(df["left_company"].unique())

print("\nJob role count:")
print(df["job_role"].nunique())

#-----Export the clean dataset------

output_path  = Path(__file__).resolve().parent.parent / "data" / "employees_clean.csv"
df.to_csv(output_path, index=False)

print(f"\nCleaned dataset saved to: {output_path}")