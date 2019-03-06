l=[1,1]
n=int(input("How many terms? "))
if(n==1):
	print("1")
elif(n==2):
	print("1\n1")
elif(n>=2):
	print("1\n1")
	for i in range(2,n):
		next_term=l[i-1]+l[i-2]
		print(next_term)
		l.append(next_term)
else:
	print("Fibonacci series for",n,"does not exist")