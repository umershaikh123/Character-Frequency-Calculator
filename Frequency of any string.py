a = []
for i in range(257):
    a.append(0)

D = "ABSDSASDASESAD  []';34124a/****/"
C = ['A' , 'B' , 'A', 'C']   # input characters

for i in D:
 
    nc = ord(i)
    a[nc] += 1


for i in range(len(a)):
    if (a[i] != 0):
       print(chr(i) ," : ", a[i])    