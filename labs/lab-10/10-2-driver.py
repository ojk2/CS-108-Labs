"""CS 108 Lab 10.2

This driver uses the Employee class to compute and save corporate statistics.

@author: OWEN KOH (ojk2)
@date: Fall, 2022
"""

from employee import Employee

employees = []

# Construct an employee object for each employee specified in 'employees.txt'
# and add it to the employees list.
# YOUR CODE HERE
targetfile = open('employees.txt')

for lines in targetfile.readlines():
    values = lines.split(',')
    person = Employee(values[0], values[1], values[2], int(values[3]))
    employees.append(person)
targetfile.close()

# algorithm following loading the employees list
if len(employees) == 0:
    print("There are no employees!!")
else:
    # totals dictionary is the 
    totals, counts = {}, {}
    max_employee = employees[0]
    min_employee = employees[0]
    for employee in employees:
        if employee.rank in totals:
            totals[employee.rank] += employee.salary
            counts[employee.rank] += 1
        else:
            totals[employee.rank] = employee.salary
            counts[employee.rank] = 1
        if employee.salary >= max_employee.salary:
            max_employee = employee
        if min_employee.salary >= employee.salary:
            min_employee = employee

file_out = open('employee-stats.txt', 'w')
file_out.write("Maximum and Minimum Salaries" + '\n')
file_out.write(str(max_employee) + '\n' + str(min_employee) + '\n')
file_out.write("Rank and Average Salaries" + '\n')
for rank in totals:
    file_out.write(f'{rank}: {totals[rank] / counts[rank]:0.2f}' + '\n')

# Write the total number of employees into the 'employee-count.txt' file.
# YOUR CODE HERE
newfile = open('employee-count.txt', 'w')
newfile.write(str(len(employees)))
newfile.close()

# Compute and print out statistics for employees
#print(employees) # YOU WILL REPLACE THIS LINE.
#for employee in employees:
#    print(employee)
