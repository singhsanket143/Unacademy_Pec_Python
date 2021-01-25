t = int(input()) # the number of test cases

while t > 0:
	c, d, l = input().split()
	c = int(c)
	d = int(d)
	l = int(l)
	if l % 4 != 0:
		print("no")
	else:
		y = c + d # total animals
		y = y - (l // 4) # animals riding
		if y >= 0 and y <= min(c, 2*d):
			print("yes")
		else:
			print("no") 

	t -= 1
	