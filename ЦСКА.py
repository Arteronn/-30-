import math
def mode(m, n):
	if m == 1:
		no_1(n)
	if m == 2:
		no_2(n)
	if m == 3:
		no_3(n)
	if m == 4:
		no_4(n)
	if m == 5:
		no_5(n)
	if m == 6:
		no_6(n)
def no_1(n):
	N = [i for i in range(n)]
	for i in range(2, math.ceil(math.sqrt(n))):
		for j in range(i, n):
			if N[j] % i == 0:
				N[j] = 0
	for i in N:
		if i != 0:
			print(i, " ")
def no_2(n):
	N = [i for i in range(n*n)]
	for i in range(2, n):
		for j in range(i, n*n):
			if N[j] % i == 0:
				N[j] = 0
	A = []
	for i in range(2, n + 2):
		if N[i] != 0:
			A.append(N[i])
	for i in A:
		print(i)
m = int(input())
mode(m, int(input()) + 1)
