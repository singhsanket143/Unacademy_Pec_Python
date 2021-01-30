def swap_pythonic(a, b):
	print(f"Intital values inside function are a = {a} and b = {b}")
	a, b = b, a
	print(f"After swapping inside function values are a = {a} and b = {b}")
	

def swap_using_third_var(a, b):
	print(f"Intital values inside function are a = {a} and b = {b}")
	temp = a
	a = b
	b = temp
	print(f"After swapping inside function values are a = {a} and b = {b}")



a = int(input("Enter the first number"))
b = int(input("Enter the second number"))


print(f"Intital values outside function are a = {a} and b = {b}")

swap_pythonic(a, b)

print(f"Final values outside function are a = {a} and b = {b}")

# Method 1 -> using 3rd variable

