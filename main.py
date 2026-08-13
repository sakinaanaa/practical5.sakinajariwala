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


display_students()

print("Average Marks:", calculate_average())