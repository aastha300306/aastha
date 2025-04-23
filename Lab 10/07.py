empcode = 101
empname = "Anjali"
date_of_joining = "2022-06-15"
salary = 55000

file = "employee_data.txt"

with open(file, 'w') as f:
    f.write(f"{empcode}\n")
    f.write(f"{empname}\n")
    f.write(f"{date_of_joining}\n")
    f.write(f"{salary}\n")

print("✅ Employee data serialized to file.")

with open(file, 'r') as f:
    lines = f.readlines()
    empcode = int(lines[0].strip())
    empname = lines[1].strip()
    date_of_joining = lines[2].strip()
    salary = float(lines[3].strip())

print("\n✅ Employee data deserialized from file:")
print(f"Employee Code: {empcode}")
print(f"Employee Name: {empname}")
print(f"Date of Joining: {date_of_joining}")
print(f"Salary: {salary}")