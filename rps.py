import random
rps=["r","p","s"]
while True:
	user=input("\nEnter your choice, r for rock, p for paper, s for scissor, q to quit \n")
	comp=random.choice(rps)
	if user=='q':
		exit()
	if user==comp:
		print("Draw")
	elif (user=='r' and comp=='s') or (user=='p' and comp=='r') or (user=='s' and comp=='p'):
		print("User Wins")
	else:
		print("Computer Wins")