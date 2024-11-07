n = int(input())
N = [i for i in range(1, n + 1)]
for i in range(2, int(n**0.5) + 1):
	for j in range(i, n):
		if N[j] % i == 0:
			N[j] = 0
for i in range(1, n):
	if N[i] != 0:
		print(N[i], " ")
