# ~ F = open("Z:/11-ПРОФИЛЬ/17data/17-403.txt")
# ~ A = []
# ~ for line in F:
	# ~ A.append(int(line))
# ~ t = 0
# ~ maxsum = 0
# ~ minnum = 100001
# ~ for i in A:
	# ~ if i < minnum:
		# ~ minnum = i
# ~ for i in range(len(A)-1):
	# ~ if A[i] % 18 + A[i+1] % 18 == minnum:
			# ~ t += 1
			# ~ if A[i] + A[i+1] > maxsum:
				# ~ maxsum = A[i] + A[i+1]
# ~ print(t)
# ~ print(maxsum)


# ~ F = open("Z:/11-ПРОФИЛЬ/17data/17-404.txt")
# ~ A = []
# ~ for line in F:
	# ~ A.append(int(line))
# ~ t = 0
# ~ minsum = 200002
# ~ minnum = 100001
# ~ for i in A:
	# ~ if i < minnum:
		# ~ minnum = i
# ~ for i in range(len(A)-1):
	# ~ if A[i] % 55 == minnum or A[i+1] % 55 == minnum:
			# ~ t += 1
			# ~ if A[i] + A[i+1] < minsum:
				# ~ minsum = A[i] + A[i+1]
# ~ print(t)
# ~ print(minsum)


# ~ F = open("Z:/11-ПРОФИЛЬ/17data/17-403.txt")
# ~ A = []
# ~ for line in F:
	# ~ A.append(int(line))
# ~ t = 0
# ~ maxsum = 0
# ~ minnum = 100001
# ~ for i in A:
	# ~ if i < minnum:
		# ~ minnum = i
# ~ for i in range(len(A)-1):
	# ~ if A[i] % 65 + A[i+1] % 65 == minnum:
			# ~ t += 1
			# ~ if A[i] + A[i+1] > maxsum:
				# ~ maxsum = A[i] + A[i+1]
# ~ print(t)
# ~ print(maxsum)


# ~ F = open("Z:/11-ПРОФИЛЬ/17data/17-403.txt")
# ~ A = []
# ~ for line in F:
	# ~ A.append(int(line))
# ~ t = 0
# ~ minpro = 1000000000
# ~ minnum = 100001
# ~ for i in A:
	# ~ if i < minnum:
		# ~ minnum = i
# ~ for i in range(len(A)-1):
	# ~ if (A[i] % 77) * (A[i+1] % 77) == minnum ** 2:
			# ~ t += 1
			# ~ if A[i] * A[i+1] < minpro:
				# ~ minpro = A[i] * A[i+1]
# ~ print(t)
# ~ print(minpro)


# ~ F = open("Z:/11-ПРОФИЛЬ/17data/17-407.txt")
# ~ A = []
# ~ for line in F:
	# ~ A.append(int(line))
# ~ t = 0
# ~ td = 0
# ~ maxsum = 0
# ~ for i in A:
	# ~ if i % 32 == 0:
		# ~ td += 1
# ~ for i in range(len(A)-1):
	# ~ if (A[i] < 0 or A[i+1] < 0) and A[i] + A[i+1] < td:
		# ~ t += 1
		# ~ if A[i] + A[i+1] > maxsum:
			# ~ maxsum = A[i] + A[i+1]
# ~ print(t)
# ~ print(maxsum)


# ~ F = open("Z:/11-ПРОФИЛЬ/17data/17-408.txt")
# ~ A = []
# ~ for line in F:
	# ~ A.append(int(line))
# ~ t = 0
# ~ maxsum = 0
# ~ thr = 0
# ~ tri = 0
# ~ bigguy = 0
# ~ for i in A:
	# ~ if abs(i % 10) == 3 and abs(i) > 99 and abs(i) < 1000 and i > bigguy:
		# ~ bigguy = i
# ~ for i in range(len(A)-2):
	# ~ thr = 0
	# ~ tri = 0
	# ~ for j in range(3):
		# ~ if abs(A[i+j]) % 10 == 3:
			# ~ thr += 1
	# ~ for j in range(3):
		# ~ if abs(A[i+j]) > 99 and abs(A[i+j]) < 1000:
			# ~ tri += 1
	# ~ if thr > 0 and tri > 0 and A[i] + A[i+1] + A[i+2] < bigguy:
		# ~ t += 1
		# ~ if A[i] + A[i+1] + A[i+2] > maxsum:
			# ~ maxsum = A[i] + A[i+1] + A[i+2]
# ~ print(t)
# ~ print(maxsum)


# ~ F = open("Z:/11-ПРОФИЛЬ/17data/17-409.txt")
# ~ A = []
# ~ for line in F:
	# ~ A.append(int(line))
# ~ t = 0
# ~ maxsum = 0
# ~ svn = 0
# ~ qua = 0
# ~ bigguy = 0
# ~ for i in A:
	# ~ if abs(i % 10) == 7 and abs(i) > 999 and abs(i) < 10000 and i > bigguy:
		# ~ bigguy = i
# ~ for i in range(len(A)-2):
	# ~ svn = 0
	# ~ qua = 0
	# ~ for j in range(3):
		# ~ if abs(A[i+j] % 10) == 7:
			# ~ svn += 1
	# ~ for j in range(3):
		# ~ if abs(A[i+j]) > 999 and abs(A[i+j]) < 10000:
			# ~ qua += 1
	# ~ if svn > 1 and qua > 1 and A[i] + A[i+1] + A[i+2] > bigguy:
		# ~ t += 1
		# ~ if A[i] + A[i+1] + A[i+2] > maxsum:
			# ~ maxsum = A[i] + A[i+1] + A[i+2]
# ~ print(t)
# ~ print(maxsum)


# ~ F = open("Z:/11-ПРОФИЛЬ/17data/17-410.txt")
# ~ A = []
# ~ for line in F:
	# ~ A.append(int(line))
# ~ t = 0
# ~ maxsum = 0
# ~ minnum = 100001
# ~ for i in A:
	# ~ if i < minnum:
		# ~ minnum = i
# ~ for i in range(len(A)-1):
	# ~ if A[i] % 16 == minnum or A[i+1] % 16 == minnum:
			# ~ t += 1
			# ~ if A[i] + A[i+1] > maxsum:
				# ~ maxsum = A[i] + A[i+1]
# ~ print(t)
# ~ print(maxsum)


# ~ F = open("Z:/11-ПРОФИЛЬ/17data/17-426.txt")
# ~ A = []
# ~ for line in F:
	# ~ A.append(int(line))
# ~ t = 0
# ~ minsum = 3000000001
# ~ thr = 0
# ~ tri = 0
# ~ bigguy = 0
# ~ for i in A:
	# ~ if abs(i % 100) == 43 and abs(i) > 9999 and abs(i) < 100000 and i > bigguy:
		# ~ bigguy = i
# ~ for i in range(len(A)-2):
	# ~ thr = 0
	# ~ tri = 2
	# ~ for j in range(3):
		# ~ if abs(A[i+j]) % 100 == 43 and abs(A[i+j]) > 9999 and abs(A[i+j]) < 100000:
			# ~ thr += 1
	# ~ if thr > 0 and tri > 0 and A[i] ** 2 + A[i+1] ** 2 + A[i+2] ** 2 < bigguy ** 2:
		# ~ t += 1
		# ~ if A[i] ** 2 + A[i+1] ** 2 + A[i+2] ** 2 < minsum:
			# ~ minsum = A[i] ** 2 + A[i+1] ** 2 + A[i+2] ** 2
# ~ print(t)
# ~ print(minsum)
