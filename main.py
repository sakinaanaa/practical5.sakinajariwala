from students import students


def display_students():
    print("===== Student Management System =====")

    for student in students:
        print("Name:", student["name"])
        print("Enrollment Number:", student["enrollment"])
        print("Marks:", student["marks"])
        print("-----------------------------")


display_students()