courses = ["MIT", "Datascience", "Cybersecurity"]
print(courses)

# Accessing an element in an array
print(courses[1])

# Looping through an array
for y in courses:
    print("Course is",y)

# Adding a new element
courses.append("Android Development")
print(courses)


# Deleting an element
courses.remove("MIT")
print(courses)