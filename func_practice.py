def fn1():
	print("hi\nhello")
fn1()
def fn2(a=10,b=10):
	c=a+b
	return c
a=fn2(25,65)
print(a)
print(fn2())
def fn3(a="Ali"):
	print (a)
fn3()
fn3("Ayush")