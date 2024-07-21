# Force input to be list<int>
# Not use len() or sum()
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# ----------------------------------------------------------

total_height = 0
number_of_students = 0
average_height = 0

for student in student_heights:
    total_height += student
    number_of_students += 1

average_height = total_height / number_of_students

print(f"total height: {total_height}\n number of students: {number_of_students}\n average height: {average_height}")