li = [[1,2,3], [4,5,6], [7,8,9]]

for i in range(0, len(li)):
	print(li[i])


y = []

n = int(input())
m = int(input())

for i in range(0, n):
	y.append([]) # appending the ith row
	for j in range(0, m):
		x = int(input())
		y[i].append(x)

print(y)

print(y[0][1]) # accessing 1st column of the 0th row