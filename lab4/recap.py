import random

#Generate 3 random integers between 100 and 999 which is divisible by 5
for i in range(3):
    x = random.randrange(100,999,5)
    print(x)

#Generate 5 random Even numbers
for i in range(5):
    x = random.randrange(0,9,2)
    print(x)


#Make a list and print only the even numbers from it
lst = [1,2,3,4,5,6,7,8,9,0]
for i in range(len(lst)):
    if i % 2 == 0:
        print(i)

#To find the largest number
x = input("enter the first number")
y = input("enter the second number")
z = input("enter the third number")
if x>y and x>z:
    print(x,"is the greatest number")
elif y>x and y>z:
    print(y,"is the greatest number")
elif z>x and z>y:
    print(z,"is the greatest number")
else:
    print("two or more numbers are equal")


#Make a list of names and print them
lst = ['Nolvos','Glitch','Kunal']
print(lst)

#Make a list of numbers and print the list from the end (DESC ORDER)
lst = [0,1,2,3,4,5,6,7,8,9,11]

for i in range(10,-1,-1):
    print(lst[i])