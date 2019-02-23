a=int(input("Enter a positive integer "))
if (a==0):
	print("Factorial of 0 is 1")
elif (a<0):
	print("I asked for a POSITIVE integer")
else:
	i=1
	fact=1
	while(i<=a):
		fact=fact*i
		i=i+1
	print(fact)