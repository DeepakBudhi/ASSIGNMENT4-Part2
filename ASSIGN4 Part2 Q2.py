a = int(input("Enter a number which you want to find the multiples : "))
print("Now enter range")
b = int(input("Enter the lower limit of range: "))
c = int(input("Enter the upper limit of the range: "))

for i in range(b,c+1):
    if i%a == 0:
        print(i)