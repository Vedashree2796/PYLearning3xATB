marks = float(input("Please enter the marks (0-100: "))
if marks >= 90:
    grade ='A'
elif marks >=80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade ='F'
print("Grade:", grade)
