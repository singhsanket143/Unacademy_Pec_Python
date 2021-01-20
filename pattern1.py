"""
    *
   ***
  *****
 *******
*********
"""

n = int(input())

i = 1

while i <= n: # using this loop we are going to every row
	print(" "*(n - i), end = "") # this is to print n-i spaces
	print("*"*(2*i - 1)) # this is to print 2i-1 stars
	i += 1


# by using nested loop
i = 1
while i <= n:
	spaces = 1
	while spaces <= (n - i):
		print(" ", end="")
		spaces += 1
	stars = 1
	while stars <= (2*i - 1):
		print("*", end="")
		stars += 1

	print("") # new line
	# increment to next row
	i += 1
