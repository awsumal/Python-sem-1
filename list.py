l=[]
print(l)
l=[5,10,15,"a","b","c","abc"]
print(l)
print(l[2])
for i in l:
	print(i)
for i in range(0,7):
	print(l[i])
l[2]=100
print(l[2])
length=len(l)
print(length)
if 10 in l:
	print("Yes")
else:
	print("No")
l.append(200)
print (l[7])
import random
print(random.choice(l))
print(random.randint(1,6))
d=input("Enter a value")
print (d)