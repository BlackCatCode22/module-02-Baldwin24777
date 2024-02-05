
# Write a Python program that uses nested if statements, nested decisions, to get three integers from the users
# and outputs the largest of the three

a = input("Enter a number here: ")
b = input("Enter a number here: ")
c = input("Enter a number here: ")

aa = float(a)
bb = float(b)
cc = float(c)

if aa >= bb:
    if aa >= cc:
        largest = aa
    else:
        largest = cc
elif bb >= cc:
    largest = bb
else:
    largest = cc
print("The largest input is: ", largest)






