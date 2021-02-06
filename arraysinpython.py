import array as arr

x = arr.array('i', [1,2,3,4,5,6])

"""
Types for an array is derived from C language

i -> integer -> 2 byte
f -> float  -> decimal -> 4 byte
d -> double -> decimal -> 8 byte
"""

for i in range(0, len(x)):
	print(x[i])

print(x, type(x), len(x))

x[0] = 0 # update an element

x.append(-3)
x.insert(1, 99)
for i in range(0, len(x)):
	print(x[i])

# slicing

y = x[1:5]
for i in range(0, len(y)):
	print(y[i])
