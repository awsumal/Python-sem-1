import random
d,p=0,0
snl={8:37,13:34,40:68,52:81,76:97,11:2,25:4,38:9,89:70,65:46,93:64}
while True:
	r=input("Press r to roll q to quit ")
	if r=='r':
		d=random.randint(1,6)
		print("You got ",d)
		if d==6:
			print("You can play now")
			break
		else:
			print("Roll again, till you get 6")
	elif r=='q':
		print("Bye")
		exit()
	else:
		print("I asked for r or q")
while True:
	r=input("Press r to roll q to quit ")
	if r=='r':
		d=random.randint(1,6)
		print("You got ",d)
		p=p+d
		if p>100:
			p=p-d
			print("Wait till you get",100-p,"or less")
		print("Your new position is ",p)
		if p==100:
			print("You Win")
			exit()
		if p in snl:
			if p>snl[p]:
				print("You got a snake")
			else:
				print("You got a ladder")
			p=snl[p]
			print("Your new position is ",p)
	elif r=='q':
		print("Bye")
		exit()
	else:
		print("I asked for r or q")