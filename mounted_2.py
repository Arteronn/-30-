def f_2(a, b):
	if a > b:
		return 0
	if a == b:
		return 1
	return f_2(a+1, b) + f_2(a*2, b) + f_2(a*a, b)
a = int(input())
b = int(input())
print(f_2(a, b))
