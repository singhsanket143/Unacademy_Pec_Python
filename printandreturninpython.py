"""
what is the exact usage and differences in
print and return when used with the context of a function

print -> anywhere when u use the print function, then it's sole purpose
is to display the content passed to it. 

return -> anywhere u write a return in a function, the value which is getting
returned is passed to it caller for any usage
as soon as we hit a return from a function, the stack frame will
be removed from the call stack for the corresponding function
"""

def add(a, b):
	c = a + b
	print("Displaying the result by printing", c)

def sqrtofdiscriminant(a, b, c):
	d = (b**2 - 4*a*c)**0.5
	print("sqrt of d is , ", d) # this will only display the value and not pass it below
	return d # this will actually pass this value as a result to the caller


def solveQuadraticEqn(a,b,c):
	"""
	ax**2 + bx + c = 0;
	"""
	root1 = (-b + sqrtofdiscriminant(a,b,c) ) / (2*a)
	root2 = (-b - sqrtofdiscriminant(a,b,c) ) / (2*a)

	print(root1, root2)

solveQuadraticEqn(1, -1, -1)