t1,t2,next=1,1,0
for i in range(0,10):
	if(i==0):
		print(t1)
	elif(i==1):
		print(t2)
	else:
		next=t1+t2
		t1=t2
		t2=next
		print(next)