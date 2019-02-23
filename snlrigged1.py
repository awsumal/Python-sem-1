for i in range (1,8):
	d=input("press r to roll, q to quit")       
	if d=='r':
		if i==1 or i==2 or i==5:
			print("You got 6")
		elif i==4 or i==6 or i==7:
			print("You got 3")
		else:
			print("You got 2")
	elif d=='q':
		print("Bye")
		exit()
print("Hurray, you won!")