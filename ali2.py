a,b,c=input("Enter 3 numbers ").split()
if (a>=b) and (a>=c):
	largest=a
elif (b>=a) and (b>=c):
	largest=b
else:
	largest=c
print(largest)