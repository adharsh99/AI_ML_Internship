# Python Fundamentals

## 1. What is Python?

Python is a high-level, general-purpose programming language known for its simple syntax and readability.

Python is widely used in:

- Artificial Intelligence
- Machine Learning
- Data Science
- Web Development
- Automation
- Software Development

---

## 2. Variables

A variable is a name used to store a value.

Example:

```python
name = "Adarsh"
age = 22
```

Here:

- `name` stores a string
- `age` stores an integer

---

## 3. Data Types

Common Python data types include:

### Integer

```python
age = 22
```

### Float

```python
height = 6.2
```

### String

```python
name = "Adarsh"
```

### Boolean

```python
is_student = True
```

### List

```python
skills = ["Python", "SQL", "AI"]
```

### Tuple

```python
coordinates = (10, 20)
```

### Set

```python
numbers = {1, 2, 3}
```

### Dictionary

```python
student = {
    "name": "Adarsh",
    "age": 22
}
```

---

## 4. Operators

### Arithmetic Operators

```text
+   Addition
-   Subtraction
*   Multiplication
/   Division
%   Modulus
**  Exponentiation
//  Floor Division
```

### Comparison Operators

```text
==  Equal
!=  Not Equal
>   Greater than
<   Less than
>=  Greater than or Equal
<=  Less than or Equal
```

### Logical Operators

```text
and
or
not
```

---

## 5. Input and Output

Python uses `input()` to receive data from the user.

```python
name = input("Enter your name: ")
print(name)
```

The `print()` function displays output.

---

## 6. Conditional Statements

Conditional statements allow programs to make decisions.

Example:

```python
age = 18

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

## 7. Loops

Loops are used to execute a block of code repeatedly.

### For Loop

```python
for i in range(5):
    print(i)
```

### While Loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## 8. Functions

A function is a reusable block of code.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

Advantages:

- Code reuse
- Better organization
- Easier testing
- Reduced duplication

---

## 9. Lists

A list stores multiple values.

```python
skills = ["Python", "SQL", "Machine Learning"]

print(skills[0])
```

Lists are:

- Ordered
- Mutable
- Able to contain duplicate values

---

## 10. Strings

A string is a sequence of characters.

Example:

```python
name = "Adarsh"
```

Common string methods:

```python
upper()
lower()
strip()
replace()
split()
```

---

## 11. Conclusion

Python provides simple and powerful programming features that make it suitable for AI and Machine Learning development.

These fundamentals will be used in later modules for data analysis and machine learning.