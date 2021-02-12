def ways(n, i, path):
	# i ->integer -> represents where u r currently standing
	# path -> string -> store the paths
	if(i > n):
		# if you have made an invalid jump
		return
	if(i == n):
		# this base case shows u r at the destination
		# if u r at the destination just print the path and go back
		print(path)
		return

	ways(n, i+1, "1 " + path)
	ways(n, i+2, "2 " + path)


n = int(input())
ways(n, 0, "")