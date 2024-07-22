# Force input to be list<int>
# Not use max()
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
# ----------------------------------------------------------
result = 0

for score in student_scores:
    if(result < score):
        result = score

print(result)