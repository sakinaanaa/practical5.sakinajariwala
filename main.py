from students import students


def display_students():
    print("===== Student Management System =====")

    for student in students:
        print("Name:", student["name"])
        print("Enrollment Number:", student["enrollment"])
        print("Marks:", student["marks"])
        print("-----------------------------")


def calculate_average():
    total = sum(student["marks"] for student in students)
    return total / len(students)


def search_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found:")
            print("Name:", student["name"])
            print("Enrollment Number:", student["enrollment"])
            print("Marks:", student["marks"])
            return

    print("\nStudent not found")


display_students()

print("Average Marks:", calculate_average())

search_student("Aisha")