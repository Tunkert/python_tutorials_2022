
number_of_students = int(input("How many students are there in your class? "))
sum = 0

student_list = []
grades_list = []

for x in range(0, number_of_students):
    current_student = input("What is the next student's name? ")
    current_grade = int(input("What is this student's grade? "))
    student_list.append(current_student)
    grades_list.append(current_grade)

alter_grades = "y"

while alter_grades == "y":
    alter_grades = input("Do you want to change a student's grade? (y for yes, n for no) ")
    if alter_grades == "y":
        which_student = input("Which student's grade do you want to change? ")
        which_index = student_list.index(which_student)
        if which_index != -1:
            new_grade = int(input("What is the new grade you want to enter? "))
            grades_list[which_index] = new_grade
        else:
            print("That is not a student you entered.")

for x in range(0, len(grades_list)):
    sum += grades_list[x]

average = sum / number_of_students

print("The class average is %.1f." % average)
    
