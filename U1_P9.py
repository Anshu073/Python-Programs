''' Write a program to assert the user enters a number greater 
than zero. '''


try:
    n=float(input("Enter a value:"))
    assert n>0,"Enter greater than 0"
    print("Entered value is ",n)

except AssertionError as e:
    print("AssertionError:",e)
    
except ValueError:
    print("Please enter numeric value.")
