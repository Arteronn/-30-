a = 2
count = 0
n = int(input())
while (count < n):
	if all (a % j != 0 for j in range(2, a)):
		print(a)
		count+=1
	a+=1
