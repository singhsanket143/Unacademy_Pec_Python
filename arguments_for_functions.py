"""
1. Required Argument
"""

def fun(x, y):
	print("Always have fun while adding", x + y)

fun(10, 20) # x will take a value 10 and y will take a value 20

"""
2. Keyword argument
These are used while calling a function always
"""

fun(y = 3, x = 20)


"""
3. Default argument
"""

def fun1(x, y, z = 3):
	return x + y + z

print(fun1(10, 20, 30)) # will override default value
print(fun1(10, 20)) # here it will take default value of z

print(fun1(z = 5, x = 3, y = 2))

# def fun2(x , y = 4, z = 3, a): # error
# 	return x*y*z*a

# print(fun2(10, 20, 30,40))
# # print(fun2(10, 20, 30))



"""
4. variable length argument

-> we pass a special argument prepended by a *

* will say from now all the args will be variable args
"""

def sum_of_nums(x, *nums):
	i = 0
	result = 0
	while i < len(nums):
		result += nums[i]
		i += 1
	return result
	print(":codechef") # dead code


print(sum_of_nums("10", 20, 30, 12, 13, 2, 1, 2))

