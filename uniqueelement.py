def findUnique(li):
	x = 0
	for i in range(0, len(li)):
		x = x ^ li[i]
	return x

n = int(input())
li = []
for i in range(0, n):
	element = int(input())
	li.append(element)

print("The unique element in the above list is ", findUnique(li))