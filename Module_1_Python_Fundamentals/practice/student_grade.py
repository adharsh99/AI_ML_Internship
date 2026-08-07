# Student Grade Calculator

print("===== Student Grade Calculator =====")

name = input("Enter student name: ")

python_marks = float(input("Enter Python marks: "))
sql_marks = float(input("Enter SQL marks: "))
ai_marks = float(input("Enter AI marks: "))

total = python_marks + sql_marks + ai_marks
average = total / 3

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== Student Result =====")
print("Name:", name)
print("Python:", python_marks)
print("SQL:", sql_marks)
print("AI:", ai_marks)
print("Total:", total)
print("Average:", round(average, 2))
print("Grade:", grade)

if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")