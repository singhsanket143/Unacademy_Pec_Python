"""
n = 4
			1
		1	2	1
	1	2	3	2	1
1	2	3	4	3	2	1
"""

n = int(input())

row = 1
while row <= n:
	print("\t"*(n - row), end = "") # for each row we have n - row spaces
	count = 1
	while count <= row:
		print(count, end = "\t")
		count += 1

	count -= 2
	while count >= 1:
		print(count, end = "\t")
		count -= 1
	print("")
	row += 1
