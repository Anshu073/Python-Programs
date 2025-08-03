''' Write a program to find out and display the common and 
the non common elements in the list using membership 
operators. '''



'''
    Membership Operators:
        1)in
        2)not in
'''

l1=[10,20,30,40,50]
l2=[60,70,80,10,20]

common=[]
for i in l1:
    if i in l2:
        common.append(i)

non_common=[]
for i in l1:
    if i not in l2:
        non_common.append(i)

for i in l2:
    if i not in l1:
        non_common.append(i)

print("List 1:",l1)
print("List 2:",l2)

print("\nCommon elements:",common)
print("Non-common Elements:",non_common)
