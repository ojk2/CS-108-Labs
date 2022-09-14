"""CS 108 - Lab 3.1

This program will generate user ids by
taking the first letter of the first name,
the last name, and the first two digits
of the student id and combining them.

@author: OWEN KOH (2635799)
"""

# get input to create new objects from user
first_name = input("First name: ")
last_name = input("Last name: ")
student_id = input("Student ID: ")

# combine all objects into one string, slicing them into shape
user_id = f"{first_name[0]}{last_name}{student_id[0]}{student_id[1]}"

print(f"User ID: {user_id}")

#user_id = first_name[0] + last_name + stu_id[0:2]
#print(f"User ID: {user_id}")
