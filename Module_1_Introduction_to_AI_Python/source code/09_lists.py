# Module 1 - Lists

skills = ["Python", "SQL", "Machine Learning"]

print("Original List:")
print(skills)

print("\nFirst Skill:")
print(skills[0])

print("\nAdding a Skill:")
skills.append("Generative AI")
print(skills)

print("\nRemoving a Skill:")
skills.remove("SQL")
print(skills)

print("\nTotal Skills:")
print(len(skills))

print("\nAll Skills:")
for skill in skills:
    print(skill)