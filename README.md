# Workforce Analytics & Insights

## Overview

Workforce Analytics & Insights is a Python and Power BI portfolio project that explores employee data and turns it into workforce metrics and business insights.

The project follows a practical analytics workflow: inspect the data, clean inconsistencies, calculate key performance indicators (KPIs), and communicate findings through an interactive Power BI dashboard.

---

## Project Objectives

- Explore workforce data using Python and Pandas
- Clean inconsistent values and handle missing data
- Compare employee counts and salaries across departments
- Analyze performance, satisfaction, absence, remote work, and employee departures
- Calculate and visualize workforce KPIs
- Present results in an interactive Power BI dashboard
- Document data-quality decisions so the analysis is transparent

---

## Technologies

- Python
- Pandas -- data exploration, cleaning, filtering, and aggregation
- NumPy -- numerical analysis
- Matplotlib -- Python data visualization
- Power BI Desktop -- interactive dashboard and visual reporting
- Git and GitHub -- version control and project sharing

---

## Dataset
- Employee ID, age, department, and job role
- Years of experience and salary
- Performance and satisfaction scores
- Remote-work status and absence days
- Whether the employee has left the company

---

## Data Cleaning
The data-cleaning workflow addresses common data-quality issues, including:

- Standardizing department names and text values
- Converting salary values with inconsistent formats into numeric values
- Removing an exact duplicate record
- Converting invalid salary entries to missing values before handling them
- Imputing missing salaries and satisfaction scores using the relevant department median where a department was available
- Checking for missing values, duplicate rows, and unusual age/experience combinations

One employee record has a missing department. It is intentionally left unknown rather than assigning a department without supporting information. 
Department-level visuals may therefore omit that record from department groupings.

---

## Current Analysis

The Python analysis explores questions such as:

- How many employees are in the dataset?
- How many employees are marked as having left, and what share of the dataset is that?
- How does employee count vary by department?
- How do average salaries and performance scores compare across departments?ysis
- How does employee satisfaction vary by department?
- How are remote and non-remote employees distributed?
- What workforce patterns can be explored using absence and turnover-related fields?

---

## Power BI Dashboard

The Power BI Dashboard currently includes:

- Total employees
- Employees who have left
- Dataset-level turnover percentage
- Employees by department
- Average salary by department
- Average performance score by department
- Remote-work distribution
- Average employee satisfaction by department

---


## Project Structure

```text
workforce-analytics/
├── data/
│   ├── employees.csv
│   ├── employees_messy.csv
│   └── employees_clean.csv
├── notebooks/
│   ├── 01_data_exploration.py
│   ├── 02_data_cleaning.py
│   └── 03_kpi_analysis.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt

```
---
## 👤 Author

**Kazi Shoubo**  
*Master of Science — Information Systems Management(Business Informatics)*  
Technical University of Berlin  