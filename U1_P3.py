''' Write a program to create a byte type array, read, modify, and
display the elements of the array. '''


import array

a=array.array('b',[10,30,40,20])

print("original array= ")

for i in a:
    print(i,end=" ")

#modify
a[2]=35

print()
    
#read
print("\nReading elements one by one=")
for i in range(len(a)):
    print(f"Eelement at index {i}={a[i]}")

#display
print("\nModified array:")
for i in a:
    print(i,end=" ")
