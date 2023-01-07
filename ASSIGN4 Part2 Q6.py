print("I would print all the prime numbers in your given range")
a = int(input("Enter the lower limit of your range: "))
v = int(input("Enter the upper limit of your range: "))
b = []
temp = 0
if a<v:
  for i in range(a, v):
    if i == 1:
        continue
    elif i == 2:
        b.append(i)
    elif i == 3:
        b.append(i)
    else:
        for j in range(2, i // 2 + 1):
           if i % j == 0:
              temp = 0
              break
           elif i % j != 0:
              temp = 1
        if temp == 0:
           continue
        elif temp == 1:
           b.append(i)

  print("The list of prime numbers between ", a, " to ", v, " is", b)

else:
    print("Invalid input.")