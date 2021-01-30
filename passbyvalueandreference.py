def update_list(li):
	print(f"Inside function before update li = {li}")
	li.append(10)
	print(f"Inside function after update li = {li}")


def update_string(s):
	print(f"Inside function before update s = {s}")
	s = s + "Bye"
	print(f"Inside function after update s = {s}")


li = [1,2,3,4,5,6,7,8,9]

print(f"Outside function before update li = {li}")
update_list(li)
print(f"Outside function after update li = {li}")

s = "Hi"
print(f"Outside function before update s = {s}")
update_string(s)
print(f"Outside function after update s = {s}")

