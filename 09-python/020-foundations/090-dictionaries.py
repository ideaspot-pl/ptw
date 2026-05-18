student = {
    "name": "John",
    "age": 21,
    "course": "Computer Science"
}
print(student)

print(student["name"])

student["age"] = 22
student["city"] = "Szczecin"
print(student)

print("Details:")
for key, value in student.items():
    print("\t", key, ":", value)
