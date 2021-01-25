num = input()
no_of_digits = len(num)

num = int(num)

original_num = num
temp = 0
while num > 0:
	digit = num % 10
	num = num // 10
	temp += digit**no_of_digits

if temp == original_num:
	print("Yes")
else:
	print("No")