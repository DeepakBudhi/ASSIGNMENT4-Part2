n=int(input ("enter desired number of rows\n"))
print ()
a=0
for i in range (n):
    for j in range (i*(i+1)//2, (i+1)*(i+2)//2):
      a= j-(j//26)*26+65
      print (f"{chr(a)}" ,end=""  )
    print ()