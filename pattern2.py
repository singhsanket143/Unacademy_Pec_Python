"""
  *
 ***
*****
 ***
  *
"""

n = int(input())

# way 1
row = 1
while row <= (n//2 + 1):
	print(" "*(n//2 + 1 - row), end="")
	print("*"*(2*row - 1))
	row += 1

while row <= n:
	print(" "*(row - n//2 - 1), end = "")
	print("*"*(2*(n - row) + 1))
	row += 1

# way 2
row = 1
while row <= n:

	if row <= (n//2 + 1):
		print(" "*(n//2 + 1 - row), end="")
		print("*"*(2*row - 1))
	else:
		print(" "*(row - n//2 - 1), end = "")
		print("*"*(2*(n - row) + 1))
	
	row += 1

