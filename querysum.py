def calculate_prefix_sum(li):
	result = []
	sum = 0
	for i in range(0, len(li)):
		sum += li[i]
		result.append(sum)
	return result

def process_query(prefix, li, l, r):
	return prefix[r] - prefix[l] + li[l]

n = int(input())
li = []
for i in range(0, n):
	x = int(input())
	li.append(x)

prefix_sum = calculate_prefix_sum(li)
q = int(input())

while(q > 0):
	l, r = input().split()
	l = int(l)
	r = int(r)

	print(process_query(prefix_sum, li, l, r))
	q -= 1