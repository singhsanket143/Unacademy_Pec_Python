"""
Scope of a variable -> visibility

if we have two variables with same name but different scope, they will not interfare each other
"""
y = 30 # global
x = 100 # x is global to a function

def fun():
	x = 10 # x is local to a function
	print("x from inside the fun", x)

	x = 20 # reassignment
	print("y from inside the fun ", y)
	return x

fun()
print("y from outside fun",y)
print("x from outside fun", x)
