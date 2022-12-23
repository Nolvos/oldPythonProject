#Wordpress
#Shopify - ecommerce
#Bootstrap,Responsive design
lst = [31,3,1,4,45,143,14]
'''print(lst[0])
print(lst[-1])'''

'''for i in lst:
    print(i)'''



'''print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])'''
'''print(len(lst))
for i in range(len(lst)):
    print(lst[i])'''

'''
Make a list and print the square of all the list elements
Make a list of names
Linear Search program to check if something exist in list or not
'''

'''lst = [1,2,3,4,5,6,7]
for i in range(len(lst)):
    print(lst[i]*lst[i])

lst = ["Glitch", "Nolvos", "Kunal"]
print(lst)'''

'''lst = [1,47,82,97]
exist = False
search = int(input("Enter the Number"))
for i in range(len(lst)):
    if lst[i] == search:
        exist = True
        break

if exist == False:
    print("Number does not exist")
else:
    print(search,"Found")'''

'''
a = [1,2,3]
b = [9,8,7]
print(10,10,10)
'''
'''a = [1,2,3]
b = [9,8,7,5,6]
if len(a)<len(b):
    length = len(a)
    maxl = len(b)
else:
    length = len(b)
    maxl = len(a)
for i in range(length):
    print(a[i]+b[i])

#print(i)
for j in range(i+1,maxl):
    print(b[j])'''


'''lst = [11,42,3,3,13,889,10,1,-5,55,9,-6]
small = lst[0]
for i in range(len(lst)):
    if small > lst[i]:
        small = lst[i]
    print(small)'''

'''lst = [1,2,3,1,2,3,1,23,1,1,31,21,1]
freq = 0
for i in range(len(lst)):
    if lst[i] == 1:
        #print(lst[i])
        freq = freq + 1
print(freq)'''