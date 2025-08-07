# input grades for each subject
grade1 = int(input("English: "))
grade2 = int(input("Mathematics: "))
grade3 = int(input("Integrated Science: "))
grade4 = int(input("Social Studies: "))
grade5 = int(input("Physics: "))
grade6 = int(input("Chemistry: "))
grade7 = int(input("Biology: "))
grade8 = int(input("Elective Mathematics: "))

# Define a function to get grade based on score
def get_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    else:
        return "F9"

# Print grades
print("English :", get_grade(grade1))
print("Mathematics :", get_grade(grade2))
print("Integrated Science :", get_grade(grade3))
print("Social Studies :", get_grade(grade4))
print("Physics :", get_grade(grade1))
print("Chemistry :", get_grade(grade2))
print("Biology :", get_grade(grade3))
print("Elective Mathematics :", get_grade(grade4))
