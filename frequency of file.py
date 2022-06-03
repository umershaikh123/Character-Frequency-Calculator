#Change the path of the file "G:\data.txt" to your own file from your hard disk
f = open("G:\data.txt" , "r+")
record = f.readline()

sd = []

for i in range(len(record)):
     record = f.readline()
     fields = record.split(sep="\t")
     sd.append(fields)

     #This inner loop removes empty strings ' ' from the list
     for j in range(len(record)):
         del sd[i][6:19]
       

    
a = []
for i in range(257):
    a.append(0)


for i in range(len(sd)):
    
    for j in sd[i][0]:
        nc = ord(j)
        a[nc] += 1

    for q in sd[i][1]:
        nc = ord(q)
        a[nc] += 1

    for w in sd[i][2]:
        nc = ord(w)
        a[nc] += 1

    for e in sd[i][3]:
        nc = ord(e)
        a[nc] += 1

    for r in sd[i][4]:
        nc = ord(r)
        a[nc] += 1


for i in range(len(a)):
    if (a[i] != 0):
       print(chr(i) ," : ", a[i])    