# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   SDuncan,11/07/24,Script Changed for Assignment05
#
# ------------------------------------------------------------------------------------------ #

import json # Added for the ability of Python to run json command set
from io import TextIOWrapper


# Define the program's data
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json" # Changed from .csv to .json for this assignment
''' Please note in the original Enrollments.json file that was included with this assignment had a bad key.
    I discovered one of the Keys didn't match the programs key reference in the starter file.
    The second student listed had Email as a key instead of LastName
'''

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
menu_choice: str = ''  # Hold the choice made by the user.
student_data: dict = {}  # changed from list to dict for this assignment
student_remove: str = '' # added in an attempt to allow the removal a student
students: list[dict[str, str]] = []
file:TextIOWrapper = None

# students: list = []  # REM'd out, program worked fine with this line, but I added (File:TextIOWrapper
#                       and students: list[dict[str, str]] = [] )to see if it would run.. runs ether way.
# csv_data: str = ''  # REM'd out, not needed for this assignment
json_data:str = '' # set to empty string
# file = None  # Holds a reference to an opened file. REM'd out used (file:TextIOWrapper) instead

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
#
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    ''' I was showing the contents of the file upon load, but felt it was redundant so I REM'd it out'''
 #   print("")
 #   print("")
 #   print("The current data in this file:")
 #   print("*" * 50)
 #   for student in students:
 #       print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")

    ''' # Error Handling for a missing file '''
except FileNotFoundError as e:
    print("")
    print(f" ERROR: \n The file {FILE_NAME:} does not exist")
    print("")
    print(e, e.__doc__, type(e), sep='\n')
    print("")
    print("")

    ''' # Error Handling for missing or syntax errored file keys '''
except KeyError as e:
    print("")
    print(f" ERROR: \n The Category (Key) {e.args[0]:} does not exist or is malformed")
    print("")
    print(e, e.__doc__, type(e), sep='\n')
    print("Exiting the Program")
    exit()

finally:
    if file.closed == False:
 #  print("*" * 50) -- These two lines were a part of the original file screen print noted above
 #  print("")
        file.close()
# Present and Process the data
while (True):
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")
    print()  # Adding extra space for menu formating.

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        ''' this Error Handling was taken from Module 5 course notes
            I attempted to create my own but failed '''
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("--> Please enter the student's first name in Alpha format ONLY <--")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            # print(e.__str__())
            print("")
            print("Lets start again")
            continue # upon user's input error it will loop back to the main menu
        try:
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("---> Please enter the student's last name in Alpha format ONLY <---")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            # print(e.__str__())
            print("")
            print("Lets start again")
            continue  # upon user's input error it will loop back to the main menu
        finally:
            course_name = input("Enter the student's course name: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)


    # Present the current data
    elif menu_choice == "2":
        print("-"*50)
        print("The Current Roster Shows the following Students are registered:")
        print("-" * 50)
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        print("-"*50)
        continue
###########################################################
    # attempt to provide a way to remove a student from the roster
    elif menu_choice == "5":
        print("The Current Roster Shows the following Students are Registered:")
        print("+"*50)
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        print("+"*50)
        print("")


        student_remove = input("Enter the LAST name (Case Specific) \n"
                                  "of the student you wish to remove from the roster: ")
        if student_remove in students:
            print("here we are now")
            print(f"{student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")

            del student_remove
                # student_remove = student_last_name

            student_data = {"FirstName": student_first_name,
                           "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
        input("please press enter to continue")
    # continue
################################################################

    # Save the data to a file '''

    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            # continue
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            print(f" SAVED: \n The file {FILE_NAME:} has been updated\n")
            continue



     # Stop the loop '''

    elif menu_choice == "4":
        print("Thankyou, Please Come Again")
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3 or 4 to EXIT")

print("Program Ended")