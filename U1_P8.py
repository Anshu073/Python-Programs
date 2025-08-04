''' Write a menu driven program to perform the 
following menu: (1) Find Area of Circle (2) Find 
Area of Triangle (3) Find Area of Square (4) 
Find Simple Interest (5) Exit. (using match-case). '''


n=int(input("Enter ending value:"))
s=0
for i in range(1,n+1):
    if i%2==0:
        #print(i,end=" ")
        print("{0}".format(i))
        s+=i
print("\nSum of even numbers is ",s)




import math

while True:
    print("---menu---")
    print("1:Area of circle")
    print("2:Area of triangle")
    print("3:square and Rectangle")
    print("4:Simple interest")
    print("5:Exit")

    ch=int(input("Enter a choice="))

    match(ch):
        case 1:
            radius=float(input("Enter radius of circle:"))
            area=math.pi*radius**2
            print("Area of circle is ",area)

        case 2:
            base=float(input("Enter base of triangle:"))
            height=float(input("Enter height of triangle:"))
            area=0.5*base*height
            print("Area of triangle is ",area)

        case 3:
            print("1:square")
            print("2:Rectangle")

            n=int(input("Enter 1 or 2"))

            if n==1:
                side=float(input("Enter side of square"))
                area=side**2
                print("Area of square is ",area)
            elif n==2:
                length=float(input("Enter length of rectangled:"))
                breadth=float(input("Enter breadth of rectangle:"))
                area=length*breadth
                print("Area of rectangle is ",area)
            else:
                print("Invalid input")

        case 4:
            principal=float(input("Enter principal amount"))
            rate=float(input("Enter rate"))
            time=float(input("Enter time in years"))
            si=(principal*time*rate)/100
            print("Simple interest is ",si)

        case 5:
            print("Bye Bye...")
            break

        case _:
            print("Please enter valid choice.")

