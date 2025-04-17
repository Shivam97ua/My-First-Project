# Task 1: Check if a Number is Even or Odd

a=int(input('Enter a Number :'))
b=a%2
if b==1:
    print(a, "is an Odd Number.")
else:
    print(a, "is an Even Number.")

print("Thank You")

# Task 2: Sum of Integers from 1 to 50 Using a Loop
a=0
for i in range(1,51):
    a+=i
print("The a of Numbers from 1 to 50 is :", a)
print("Thank You")