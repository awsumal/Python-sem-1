try:
	a=int(input("Enter a number "))
	if a<5:
		raise NameError
	elif a==5:
		raise TypeError
except ValueError:
	print("Ewwwwwwwwwww, value error")
except NameError:
	print("Ewwwwwwwwwww, name error")
except TypeError:
	print("Ewwwwwwwwwww, type error")
else:
	print("Yayyyyyyy no error")
finally:
	print("Execution Completed")