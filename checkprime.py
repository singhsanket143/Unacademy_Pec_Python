from math import floor
def check_prime(n):
	if n == 2:
		return True

	for i in range(2, floor(n**0.5)+1):
		if n % i == 0:
			return False


	return True


n = int(input()) # n will always be an integer

result = check_prime(n)

if(result == True):
	print("Yes it is a prime")
else:
	print("No it's not a prime")