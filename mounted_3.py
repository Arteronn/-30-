def f_3(a, b):
	if a > b:
		return 0
	if a == b:
		return 1
	t = 0
	if a // 10 % 10 == 9:
		t = 10
	return f_3(a+1, b) + f_3(a+10-t, b)
a = int(input())
b = int(input())
print(f_3(a, b))
