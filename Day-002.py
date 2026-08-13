# Question 1
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Question 2 Student Grade
maths = int(input("Enter your Maths marks: "))
stats = int(input("Enter your Stats marks: "))
total = maths + stats
average = total / 2
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

print(f"Maths: {maths}")
print(f"Stats: {stats}")
print(f"Average: {average}")
print(f"Your grade is: {grade}")

#Question 3 — Python Study Recommendation
python_hours_per_day = int(input("Enter the number of hours you study Python per day: "))
if python_hours_per_day < 1:
    print("You must code today.")
elif python_hours_per_day >= 1 and python_hours_per_day < 3:
    print("Keep going")
elif python_hours_per_day >= 3 and python_hours_per_day < 5:
    print("Good")
else:
    print("Excellent! You are a Python pro.")

# Question 4 — Predict the Output

Output = 'A'