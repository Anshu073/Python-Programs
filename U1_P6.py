''' Create a program to display memory locations of two 
variables using id() function, and then use identity 
operators two compare whether two objects are same or not. '''


a=10
b=10

print("Location of A is ",id(a))
print("location of B is ",id(b))

if a is b:
    print("a and b are same")
else:
    print("a and b are not same")

a=[1,2,3]
b=[1,2,3]

print("\nLocation of A:",id(a))
print("Location of B:",id(b))

if a is b:
    print("A and B are same")
else:
    print("A and B are not same")
