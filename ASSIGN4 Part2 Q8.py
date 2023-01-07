print("You are asked to enter 10 numbers.")
b =[]
for i in range(1,11):
    a = int(input(f"Enter the number at position {i}: "))
    b.append(a)

# POSITIVE NUMBERS

Positive_numbers = []
print("Positive numbers are :  ")
for items in b:
    if items>=0 :
        Positive_numbers.append(items)
uniques1 = []
for items in Positive_numbers:
    if items in uniques1:
        continue
    elif items not in uniques1:
        uniques1.append(items)

for items in uniques1:
    print(items,"  ",end='')
print(" ")

# NEGATIVE NUMBERS

Negative_numbers = []
print("Negative numbers are :  ")
for items in b:
    if items < 0:
        Negative_numbers.append(items)
uniques2 = []
for items in Negative_numbers:
    if items in uniques2:
        continue
    elif items not in uniques2:
        uniques2.append(items)

for items in uniques2:
    print(items, "  ", end='')
print(" ")
# ODD NUMBERS

Odd_numbers = []
print("Odd numbers are :  ",end='')
for items in b:
    if items%2 != 0:
        Odd_numbers.append(items)
uniques3 = []
for items in Odd_numbers:
    if items in uniques3:
        continue
    elif items not in uniques3:
        uniques3.append(items)

for items in uniques3:
    print(items, "  ", end='')
print(" ")

# EVEN NUMBERS

Even_numbers = []
print("Even numbers are :  ", end = '')
for items in b:
    if items%2 == 0:
        Even_numbers.append(items)
uniques4 = []
for items in Even_numbers:
    if items in uniques4:
        continue
    elif items not in uniques4:
        uniques4.append(items)

for items in uniques4:
    print(items, "  ", end='')
print(" ")

# OCCURRENCE OF NUMBERS

Occurrence = []
store = 1233445667899876543211123456789987654
b.sort()
print("Occurrences are as follow:")
for items in b:
    if items != int(store):
       a = b.count(items)
       Occurrence.append(a)
       print("The occurrence of ", items," is ",a)
    else:
        continue
    store = items

print("THANK YOU !!!!")