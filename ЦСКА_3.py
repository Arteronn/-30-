def fb(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fb(n-2)+fb(n-1)
n = int(input())
for i in range(0, n):
	print(fb(i))
