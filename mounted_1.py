def f_1(a, b):
	if a > b:
		return 0
	if a == b:
		return 1
	return f_1(a+1, b) + f_1(a*2, b) + f_1(a*3, b)
a = int(input())
b = int(input())
print(f_1(a, b))
