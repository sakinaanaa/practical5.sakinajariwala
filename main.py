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


def validate_marks(marks):
    if 0 <= marks <= 100:
        return True
    return False
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


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