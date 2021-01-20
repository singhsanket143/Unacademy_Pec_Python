# Assignment Operators

# 1. = -> It will assign the value on the rhs to the variable on lhs
a = 10
b = 30
c = b 
print(a, b, c)
# 2. += -> It will act same as a = a + 1

a += 1 # Instead of writing a = a + 1, we write this
b += a # Instead of writing b = b + a, we write this

print(a, b)

# 3. -= -> It will act same as a = a - 1
a -= 1 # Instead of writing a = a - 1, we write this
b -= a # Instead of writing b = b - a, we write this
print(a, b)


# 4. *= -> It will act same as a = a * 2
a *= 2

# 5. %= -> It will act same as a = a % 7
a %= 7

# 6. /= -> It will act same as a = a / 2
a /= 2

# 7. //= -> It will act same as a = a // 2
a //= 2

# 8. **= -> It will act same as a = a ** 2
a **= 2



# Can we do something like a++ or ++a for a = a + 1 in python -> No


# what will happen if we write a =- 1
a = -1
print(a)


# What will happen if we write a -= -1 -> a = a - (-1)


#-----------------------------------------------------------

# Bitwise Operator -> these will work on bit by bit level

# 1. & -> a&b -> it will do bitwise and on the binary of a, b
z = 5 & 4 # 5-> 101 , 4-> 100, 101&100 -> 100 (4)
print(z)

# 2. | -> a|b -> it will do bitwise or on the binary of a, b
z = 5 | 4 # 5-> 101 , 4-> 100, 101|100 -> 101 (5)
print(z)

# 3. ^ -> a^b -> it will do bitwise xor on the binary of a, b
z = 5 ^ 4 # 5-> 101 , 4-> 100, 101^100 -> 001 (1)
print(z)

# 4. ~ -> ~a -> it will do bitwise not on the binary of a
z = ~5 # 5-> 101 , ~101 -> -6
print(z)

# 4. << -> Left shift operator
z = 1 << 3 # it will append 3 zeroes to the right of 1 -> 1000
print(z)

# ex-> 6 (110) -> 6 << 2 -> 110 -> 1100 -> 11000

# 5. >> -> right shift operator
z = 5 >> 2 # it will prepend 2 zeroes to the left of 5 and remove last 2 bits
print(z)

# (101) >> 2
# 101 -> 010 -> 001

# 5 >> 3 -> (101) -> 010 -> 001 > 000


#-----------------------------------------
# Membership operator

# 1. in operator
arr = [1,2,3,'sanket']
print(3 in arr) # is there a value 3 in arr ? 
print('sanketsingh' in arr) # -> False

# 2. not in

print(3 not in arr) # is 3 not available in arr ? 

print("for string", 'a' in 'astrology')

# -----------------------------------------
# Identity Operator

# -> it will check if the two values are of same type and having same value

print(3 is 4)
print((2 == 2) is True)
print(4 is True)
print(6 is 6)

print(7 is not 7)







