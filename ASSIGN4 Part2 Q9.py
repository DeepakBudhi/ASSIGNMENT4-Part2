a =[]
b = int(input("Enter How many words you want in your list: "))
for i in range(1,b+1):
    d = input(f"Enter a word at {i}th position : ")
    c = d.strip(" ")
    try:
        f = int(c)
        print("Although it is a number.But for you I will treat it as a string here.")
        a.append(c)
    except:
         a.append(c)

a.sort()
store = ""
for items in a :
    if items != store:
        counting = a.count(items)
        print("The occurrence of ", items,"is",counting)

    else:
        continue
    store = items