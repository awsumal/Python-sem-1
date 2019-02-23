a=int(input("Enter a number "))
for i in range(2,a):
	if(a%i==0):
		print(a,"is not prime \n",i,"times",(a//i),"=",a)
		break;
else:
	print(a,"is prime")