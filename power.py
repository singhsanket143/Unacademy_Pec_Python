def powerIterative(a, b):
	if not isinstance(a, int) or not isinstance(b, int):
		print("Please enter valid inputs")
		return None

	temp = 1
	for i in range(0, b): # [a, b)
		temp = temp * a

	return temp


def powerRecursive(a, b):
	# base case
	if b == 0:
		return 1
	if b == 1:
		return a
	# recursive task
	return a * powerRecursive(a, b-1)

def powerRecursiveOptimized(a, b):
	if b == 0:
		return 1
	if b == 1:
		return a

	recursive_task = powerRecursiveOptimized(a, b//2)
	if b % 2 == 0:
		return recursive_task*recursive_task
	else:
		return recursive_task * recursive_task * a




a = int(input()) # this int is still necessary why ????
b = int(input())
result = powerRecursiveOptimized(a, b)
print(result)

