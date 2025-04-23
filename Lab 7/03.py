employees = [
    {'dept_no': 101, 'roll_no': 'E001', 'salary': 50000},
    {'dept_no': 102, 'roll_no': 'E002', 'salary': 60000},
    {'dept_no': 101, 'roll_no': 'E003', 'salary': 45000},
    {'dept_no': 103, 'roll_no': 'E004', 'salary': 70000},
    {'dept_no': 102, 'roll_no': 'E005', 'salary': 55000},
    {'dept_no': 101, 'roll_no': 'E006', 'salary': 60000},
    {'dept_no': 103, 'roll_no': 'E007', 'salary': 65000},
]

dept_salaries = {}
for emp in employees:
    dept = emp['dept_no']
    salary = emp['salary']
    if dept not in dept_salaries:
        dept_salaries[dept] = []
    dept_salaries[dept].append(salary)


result = {}
for dept, salaries in dept_salaries.items():
    result[dept] = {'min_salary': min(salaries), 'max_salary': max(salaries)}


for dept, stats in result.items():
    print(f"Department {dept}: Min Salary = {stats['min_salary']}, Max Salary = {stats['max_salary']}")