a = int(input("Give input of first angle ")) # giving user a prompt during input
b = int(input("Give input of second angle "))
c = int(input("Give input of third angle "))

if a > 0 and b > 0 and c > 0:
	if a + b + c == 180:
		print("Yes they are angles of a triangle")
	else:
		print("No they are not angles of triangle")
else:
	print("If the angles are not greater than zero then it is degenerate")