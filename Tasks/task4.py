#completed

x= range(2000, 3201)

y=[]

for i in x:
    if(i%7 == 0 and i%5 !=0):
        y.append(i)
print(y)
