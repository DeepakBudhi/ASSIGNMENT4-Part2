a = input("Enter a string: ")
length = len(a)
b = []
for i in range(1,length+1) :
    b.append(a[length - i])

for items in b:
    print(items,end='')