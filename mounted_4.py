def f_4(a, b):
	if a > b:
		return 0
	if a == b:
		return 1
	t = 0
	s = 0
	p = 1
	while p <= a:
		if (a % (10 * p)) // p == 9:
			t += p
		s += p
		p *= 10
	return f_4(a+1, b) + f_4(a + s - t, b)
a = int(input())
b = int(input())
print(f_4(a, b))
