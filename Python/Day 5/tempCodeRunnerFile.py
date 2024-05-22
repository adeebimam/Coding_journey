student_heights = input("Please enter the student height").split()

student_heights = [int(height) for height in student_heights]

total_height = 0

for height in student_heights:
    total_height +=  student_heights

print(total_height)
