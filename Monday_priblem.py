# 1. **Common Students Finder**

# You are given two sets of students — those who enrolled in "Python" and "Data Science."
# Find students enrolled in both courses.

# ```python
# Input:
# python = {"Asha", "Vijay", "Kiran", "Ravi"}
# data_science = {"Kiran", "Ravi", "Anu"}

# # Output: {'Kiran', 'Ravi'}
# common_names = python & data_science
# print(common_names)


# 2. **Student Marks Analyzer**

# Given a list of students where each student is represented as a dictionary containing their name and marks,
# print the name of the student who scored the highest marks.

# ```python
# Input:
# students = [
#     {"name": "Arun", "marks": 78},
#     {"name": "Priya", "marks": 88},
#     {"name": "Kiran", "marks": 91}
# ]

# Output:
# Kiran

# students = [
#     {"name": "Arun", "marks": 78},
#     {"name": "priya", "marks": 88},
#     {"name": "kiran", "marks": 91},
#     {"name": "Antoniya", "marks": 95},
#     {"name": "Nathiya", "marks": 99}
# ]
# top_student = students[0]
# for student in students:
#     if student["marks"] > top_student["marks"]:
#         student["marks"] = top_student["marks"]
# print(top_student)

# top_student = students[0]  

# for student in students:
#     if student["marks"] > top_student["marks"]:
#         top_student = student 

# print(top_student)
