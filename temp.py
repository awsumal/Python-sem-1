import random
d,p=0,
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
		if p==8:
			p=37
			print("You got a ladder, your new position is",p)
		if p==13:
			p=34
			print("You got a ladder, your new position is",p)
		if p==40:
			p=68
			print("You got a ladder, your new position is",p)
		if p==52:
			p=81
			print("You got a ladder, your new position is",p)
		if p==76:
			p=97
			print("You got a ladder, your new position is",p)
		if p==11:
			p=2
			print("You got a snake, your new position is",p)
		if p==38:
			p=9
			print("You got a snake, your new position is",p)
		if p==65:
			p=46
			print("You got a snake, your new position is",p)
		if p==89:
			p=70
			print("You got a snake, your new position is",p)
		if p==93:
			p=64
			print("You got a snake, your new position is",p)
		if p==100:
			print("You Win")
			exit()
	elif r=='q':
		print("Bye")
		exit()
	else:
		print("I asked for r or q")