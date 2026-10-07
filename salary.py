# Task 1: Employee Salary Calculation
name = input("Employee name: ")
basic = float(input("Basic salary: "))
deduction = float(input("Monthly deduction: "))

allowance = 0.10 * basic       # 10% housing allowance
gross = basic + allowance
net = gross - deduction

print(f"\nEmployee: {name}")
print(f"Basic Salary: {basic:.2f}")
print(f"Housing Allowance: {allowance:.2f}")
print(f"Gross Salary: {gross:.2f}")
print(f"Deduction: {deduction:.2f}")
print(f"Net Salary: {net:.2f}")
