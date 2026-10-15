print("Student Scholarship Program")

name = input("Enter your name: ")
father_name = input("Enter your father's name: ")
cnic = input("Enter your CNIC number: ")
cell = input("Enter your cell number: ")
roll_no = input("Enter your roll number: ")
percentage = float(input("Enter your percentage: "))

print("\nStudent Information")
print("Name:", name)
print("Father Name:", father_name)
print("CNIC:", cnic)
print("Cell Number:", cell)
print("Roll Number:", roll_no)
print("Percentage:", percentage)

if percentage > 90:
    print("Congratulations! You can apply for scholarship.")
else:
    print("Sorry! You cannot apply for scholarship.")