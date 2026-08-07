# Module 1 - Loops

print("For Loop")
print("--------")

for number in range(1, 6):
    print(number)

print("\nWhile Loop")
print("----------")

count = 1

while count <= 5:
    print(count)
    count += 1

print("\nMultiplication Table")

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)