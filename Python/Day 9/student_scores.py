"""
In this program we will look at a new topic called dictionary

In this program we would have the access to a dictionary called as 
student_scores, the key in this dictionary would be the name of the
student and the value of each key would be the marks that they have
acheieved.

We have their marks into grades and then store them in a dictionary

Done By Adeeb Imam
Date 31st May 2024
"""

student_scores = {
    "Harry": 81,
    "Ron": 78
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)
