# Module 1 - Input and Output

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\nStudent Information")
print("-------------------")
print("Name:", name)
print("Age:", age)

if age >= 18:
    print("Status: Adult")
else:
    print("Status: Minor")