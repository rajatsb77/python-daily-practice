# Question 1
num = 1
for i in range(1,11):
    print(i)

# Question 2 — Even Numbers
num = 1
for i in range(1,21):
    c = i % 2
    if c == 0:
        print(i)


# Question 3 — Sum of Numbers
total = 0
for i in range(1, 101):
    total = total + i
print(f"The sum of numbers from 1 to 100 is: {total}")

# Question 4 — Multiplication Table
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1,num+1):
    print(f"{num} x {i} = {num*i}")

# Question 5 — while Loop
while num > 0:
    print(num)
    num -= 1

print("Blast off!")


# Thinking Challenge
# Answer - 2,4,6,8,10