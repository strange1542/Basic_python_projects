students = [
    ("Rahul", 85, "Python"),
    ("Priya", 92, "Java"),
    ("Aman", 76, "Python"),
    ("Rohit", 88, "Java"),
    ("Karan", 95, "Python")
]
print("All students :-")
for name, marks, course in students:
    print(f"{name} - {marks} - {course}")

highest_name = ""
highest_marks = 0

for name, marks,course in students:
    if marks > highest_marks:
        highest_name = name
        highest_marks = marks
print()
print("Highest scorer :",highest_name)
print("Marks :",highest_marks)
print()
total = 0

for name, marks, course in students:
    total += marks 

avg = total / len(students)

print("Average marks:", avg)

courses = set()

for name, marks, course in students:
    courses.add(course)

print(courses)
print()
python = 0 
java = 0

for name, marks, course in students:
    if course == "Python":
        python += 1
    elif course == "Java":
        java += 1

print("Python :",python)
print("Java :",java)
student_dict = {}
for name, marks, course in students:
    student_dict[name] = marks
print()
print(student_dict)
print()

new_name = ""
new_marks = 0
for name, marks, course in students:
    if marks >= 80:
        new_name = name
        new_marks = marks
        print(f"{new_name} - {new_marks}")
