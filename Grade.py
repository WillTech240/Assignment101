grade1 = int(input("English"))
grade2 = int(input("Mathematics"))
grade3 = int(input("Integreted Science"))
grade4 = int(input("Social Studies"))
#English grade (grade1)
if grade1 <= 100 and grade1 >= 90:
    print("A")

elif grade1 <=89 and grade1 >= 80:
    print("B")

elif grade1 >= 70 and grade1 <= 79:
    print("C")

elif grade1 < 70:
    print("F9")
