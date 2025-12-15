# Project Prompt:

# You are hired to build a Student Lookup Tool for a school front office. The secretary must be able to:

    # Enter a student’s full name

    # Instantly see:

            # CPS ID

            # Homeroom

            # Grade Level

            # Primary Email

            # Students must:

            # Describe the search process

## be able to add new data
# Your program must allow the secretary to ADD a brand new student
# into the system while the program is running.

# Your job is to let the secretary type in a new student just like filling out a registration form.
# Once the form is complete, your program must turn that information into a dictionary and add it to the main list of students.
# If the student already exists (same CPS ID), your program must block the entry to prevent duplicates.

# The program should:
    # 1. Ask the user for the following information:
    #    - CPS ID
    #    - First Name
    #    - Last Name
    #    - Middle Name
    #    - Homeroom
    #    - Grade Level
    #    - Primary Email
    #    - Secondary Email

import student_data




students = student_data.students

# Collect information from user
cps_id = int(input("Enter CPS ID: "))
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
middle_name = input("Enter Middle Name: ")
homeroom = input("Enter Homeroom: ")
grade_level = int(input("Enter Grade Level: "))
primary_email = input("Enter Primary Email: ")
secondary_email = input("Enter Secondary Email: ")













# 2. Combine the First and Last name into this format:
    #    "Last, First"  

combo_name = f"{last_name}, {first_name}"







# 3. Store all of the new information into ONE dictionary
    #    that matches the structure of the existing student data.

new_student = {
    "CPSID": cps_id,
    "Combo,Name": combo_name,
    "LName": last_name,
    "FName": first_name,
    "MName": middle_name,
    "HR": homeroom,
    "GL": grade_level,
    "Email": [primary_email, secondary_email]
}







# 4. Add (append) that new dictionary into the main students list.




# Check for duplicate CPS ID

# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken

duplicate_found = False
for student in students:
    if student["CPSID"] == cps_id:
        duplicate_found = True
        break

# If duplicate found, display error; otherwise add the student





if duplicate_found:
    print(f"\nError: CPS ID {cps_id} already exists in the system.")
else:
    students.append(new_student)
    
    # 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record
    
    print("\nStudent successfully added!")
    
    print(f"Total students in system: {len(students)}")

    print("\nNewly added student record:")
    print(f"  CPS ID: {new_student['CPSID']}")
    print(f"  Name: {new_student['Combo,Name']}")
    print(f"  Homeroom: {new_student['HR']}")
    print(f"  Grade Level: {new_student['GL']}")
    print(f"  Primary Email: {new_student['Email'][0]}")
    print(f"  Secondary Email: {new_student['Email'][1]}")
    


# 6. The program must NOT delete or overwrite any existing students.












