# Given the names and grades for each student in a Physics class of N students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the same grade, order their names alphabetically
# and print each name on a new line.
#
# Input Format
# The first line contains an integer, N, the number of students.
# The 2N subsequent lines describe each student over 2 lines;
# the first line contains a student's name, and the second line contains their grade.
#
# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics;
# if there are multiple students, order their names alphabetically and print each one on a new line.
#
# Sample Input
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
#
# Sample Output
# Berry
# Harry

# inputs
students_quantity = int(input())
students = [[str(input()), float(input())] for i in range(students_quantity)]

# get the lowest grade and remove all occurences of it from the list of grades
lowest_grade = min([grade for name, grade in students])
grades = [grade for name, grade in students]
lowest_grade_count = grades.count(lowest_grade)
for i in range(lowest_grade_count):
    grades.remove(lowest_grade)

# get the second lowest grade and
# check which students have this grade
second_lowest_grade = min(grades)
second_lowest_grade_students = [name for name, grade in students if grade == second_lowest_grade]
second_lowest_grade_students.sort()

# print in alphabetical order the students names
for student_name in second_lowest_grade_students:
    print(student_name)
