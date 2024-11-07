def size_sort(M):
	for j in range(len(M)):
		for i in range(len(M) - 1):
			if M[i].size > M[i+1].size:
				M[i], M[i+1] = M[i+1], M[i]
class File:
	name = ""
	size = 0
	ftype = ""
	created = ""
	edited = ""
	access = ""
class N_S:
	name = ""
	size = 0
A = []
types = []
top_10 = []
preses = []
vids = []
d = 0
for i in open("files.csv", "r"):
	A.append(File())
	A[d].name = i.split(",")[0]
	A[d].size = int(i.split(",")[1])
	A[d].ftype = i.split(",")[2]
	A[d].created = i.split(",")[3]
	A[d].edited = i.split(",")[4]
	A[d].access = i.split(",")[5]
	d += 1
for i in A:
	if i.ftype not in types:
		types.append(i.ftype)
	if i.ftype == "презентация" and i.access == "ограничен" and i.edited.split(".")[2] == "2012":
		preses.append(i.name)
	if i.ftype == "видео" and i.size > 102400 and i.created.split(".")[2] == "2011" and int(i.created.split(".")[1]) > 6:
		vids.append(i)
for i in range(10):
	for j in range(len(A) - 1):
		if A[j].size > A[j+1].size:
			A[j], A[j+1] = A[j+1], A[j]
	top_10.append(N_S())
	top_10[i] = A[-i]
for i in range(len(top_10)):
	top_10[i] = str(top_10[i].name)
top_10 = sorted(top_10)
preses = sorted(preses)
size_sort(vids)
d = 0
print("Количество файлов каждого типа:")
for i in types:
	d = 0
	for j in A:
		if j.ftype == i:
			d += 1
	print(i, ": ", d, sep="")
print("10 самых больших файлов:")
for i in top_10:
	for j in A:
		if i.name == j.name:
			print(j.name, ": ", j.size, sep="")
print("Презентации с ограниченным доступом:")
for i in preses:
	print(i)
print("Видео больше 100Мб:")
for i in vids:
	print(i.name)
