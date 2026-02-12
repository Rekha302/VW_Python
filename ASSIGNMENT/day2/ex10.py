mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))

average = (mark1 + mark2 + mark3) / 3

if 90 <= average <= 100:
    grade = "A"
elif 80 <= average < 90:
    grade = "B"
elif 70 <= average < 80:
    grade = "C"
elif 60 <= average < 70:
    grade = "D"
elif 0 <= average < 60:
    grade = "F"
else:
    grade = "Invalid Marks"

print("Average =", average)
print("Grade =", grade)
