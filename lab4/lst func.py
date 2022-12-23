#make a list and ask the user to add a number and add it to the list

'''lst = [1,3,5,7,8,9]
x = int(input("Please add a number"))
lst.append(x)
print(lst)'''
'''
Ask the user to enter how many numbers do you want to insert
run the loop that many times
and apend all the nums inside empty list
'''
'''lst= []
len = int(input("Enter how many numbers you want to insert"))
for i in range(len):
    x = int(input("Enter the number"))
    lst.append(x)
print(lst)'''
'''#ask the user to enter the names separated by comas ,
x = input("Enter a name")
lst = x.split(",")
print(lst)
'''

str = "GlItCh"
for i in str:
    if i.islower():
        print(i.lower())
    else:
        print(i.upper())
        print(str,end=" ")

