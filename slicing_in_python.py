"""
Slicing in python -> Slicing means extracting a substring or sublist or 
you can say a part of a string in python
slicing in python goes hand in hand with list
"""
l = [1,2,3,4,5,6,7,8,9]
s = "Codechef"

print(l[0:5]) # extract 0,1,2,3,4
print(s[1:3])

print(l[0:5:2]) # made jumps of 2

print(l[1:]) # will give u everything from index 1 to last

print(s[-2:]) # last 2 elements

print(l[:5]) # first n elements 

print(l[::2]) # will pick every 2nd element

print(l[:-2])

# we can also assign a list by using slicing 

l[1:5] = [22,33,44,55]
print(l)
