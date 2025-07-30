#Write a program to swap two numbers without taking a temporary variable.

a=int(input("Enter a value of A:"))
b=int(input("Enter a value of B:"))

a=a+b
b=a-b
a=a-b

#a,b=b,a

print("Swapping of Two numbers")
print(f"A:{a} \t B:{b}")
