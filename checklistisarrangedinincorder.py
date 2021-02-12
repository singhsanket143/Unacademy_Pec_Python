def check_list(li, i):
	if(i == len(li) - 1):
		return True

	# recursive assumption
	isarrangedcorrectly = check_list(li, i+1)
	if(isarrangedcorrectly == True):
		return li[i] <= li[i+1]
	else:
		return False



n = int(input())
li = []
for i in range(0, n):
	x = int(input())
	li.append(x)

result = check_list(li, 0)

if(result == True):
	print("Yes")
else:
	print("No")