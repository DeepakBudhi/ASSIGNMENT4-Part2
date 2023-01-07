import math
print("Here I am going to find the area of a triangle for you.")
a = int(input("Enter 1st side : "))
b = int(input("Enter 2nd side : "))
c = int(input("Enter 3rd side : "))

if a+b>c and b+c>a and a+c>b :
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area of the given triangle is ", area )

else:
    print("The triangle is not possible with these sides. ")