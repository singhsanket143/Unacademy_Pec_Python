a = 1 # integer variable
b = 2
print(a+b) # print the sum
print(a, b) # print 1 2
print(a, end = "")
print(b)
print(10*a+b) # great hack
#print(a, end="", b) # error as we cannot pass anything after end


# Q -> how to take integer input from user ???
x = int(input()) # as input always gives you a string, we can use int() to convert it to integer

# Q -> can we have multiline comments

"""
this is a multiline comment
you can give it by using triple double quotes
"""

''' 
this is a multiline comment
you can give it by using triple single quotes
'''

# Q -> Significance of \t (backslash t)??
# -> when used it will give you a tab space similar to the tab key
print("sanket\t\tsingh")


# Q -> What if we want to print -> '' ? 
print("\'\'")
print("''")

# Q -> How to print -> \'
print("\\'")

# Q -> What is the use of \n ? 
# -> whever used it will add a new line to the console
print("Sanket\nSingh")

# Q -> Use of // ?
# -> Question is incomplete ??
# Because // is an operator also and // can exist in a string like two normal forward slash
c = 100 // 7
d = 100 / 7
print(c, d)

# Q -> What is the difference between and , && in python ?
# -> In python && doesnt exist, and serves the same purpose like in flowcharts

# Q -> Use of \\
# -> it will print a single \
print("\\")



"""print(not 2, not 0, not -4) 
# whenever you write any non zero integer it is evaluated as true and 0 as false
print(x and y) # returns x if x is false, otherwise y
print(x or y) # returns y if x is false, otherwise x
# positive int -> true, 0 -> false, negative -> true

print(not "", not "abs")"""

# empty string -> false, non empty string -> true

# Q - > what happens when u write print(True) ??
print(True)
print(False)

# Q -> How to print 'unacademy' with quotes
print("'unacademy'")
print('\'unacademy\'')

print("sanket \tsingh")
print("sanket\tsingh")



