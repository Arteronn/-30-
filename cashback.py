def f(W, p, t):
	if t == W:
		return 1
	if t > W:
		return 0
	d = 0
	for i in p:
		d += f(W, p, t + i)
	return d
N = int(input())
W = int(input())
p = [1]
for i in range(N):
	p.append(int(input()))
print(f(W, p, 0))
