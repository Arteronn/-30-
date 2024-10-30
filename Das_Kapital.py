count = 0
alg_av = 0
rus_av = 0
phys_av = 0
hist_av = 0
F = open("marks.csv", "r")
class Grades:
	surname = ""
	name = ""
	g_1 = 0
	g_2 = 0
	g_3 = 0
	g_4 = 0
	grade_sum = 0
List = []
for i in F:
	List.append(Grades())
	List[count].surname = i.split(",")[0]
	List[count].name = i.split(",")[1]
	List[count].g_1 += int(i.split(",")[2])
	List[count].g_2 += int(i.split(",")[3])
	List[count].g_3 += int(i.split(",")[4])
	List[count].g_4 += int(i.split(",")[5])
	List[count].grade_sum += List[count].g_1 + List[count].g_2 + List[count].g_3 + List[count].g_4
	alg_av += List[count].g_1
	rus_av += List[count].g_2
	phys_av += List[count].g_3
	hist_av += List[count].g_4
	count += 1
alg_av /= count
rus_av /= count
phys_av /= count
hist_av /= count
max_sum = 0
for i in List:
	if i.grade_sum > max_sum:
		max_sum = i.grade_sum
print("Средний балл по алгебре:", alg_av)
print("Средний балл по русскому:", rus_av)
print("Средний балл по физике:", phys_av)
print("Средний балл по истории:", hist_av)
print("")
print("")
print("Максимальный балл:", max_sum)
print("")
print("Ученики, набравшие максимальный балл:")
print("")
for i in List:
	if i.grade_sum == max_sum:
		print(i.surname, i.name)
print("")
print("")
print("Ученики, получившие хотя бы 1 двойку:")
print("")
for i in List:
	if (i.g_1 <= 2) or (i.g_2 <= 2) or (i.g_3 <= 2) or (i.g_4 <= 2):
		print(i.surname, i.name)
