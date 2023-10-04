#complete

#sen = input('Insert sentence:')
sen = 'hello world and practice makes perfect and hello world again'
senlist = sen.split(" ")
sen2 = []

for i in senlist:
    if(sen.count(i)>=1 and (i not in sen2)):
        sen2.append(i)
sen2.sort()
q = ' '.join(sen2)
print(q)

