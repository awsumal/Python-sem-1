import random
def function():
	print("\nFinal scores are \nuser:",us,"\ncomputer:",cs)
	if(us>cs):
		print("User wins")
	elif(us==cs):
		print("It is a draw")
	else:
		print("Computer wins")
	exit()
us,cs=0,0
rps={'r':"rock",'p':"paper",'s':"scissor",'q':"quit"}
psr=['r','p','s']
while True:
	user=input("\nEnter your choice, r for rock, p for paper, s for scissor, q to quit \n")
	comp=random.choice(psr)
	if user=='q':
		function()
	print("\nYou have chosen",rps[user])
	print("Computer has chosen",rps[comp])
	if user==comp:
		print("Draw")
	elif (user=='r' and comp=='s') or (user=='p' and comp=='r') or (user=='s' and comp=='p'):
		print("User gets a point")
		us=us+1
	else:
		print("Computer gets a point")
		cs=cs+1
	if(us ==3 or cs ==3):
		function()
	print("\nScore\n\nUser:",us,"\nComputer:",cs)
