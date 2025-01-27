# f=open("Z:/11-ПРОФИЛЬ/24data/24-295.txt")
# s=f.readline().replace("DE","D E").split()
# h=list(map(len,s))
# lmax=0
# for i in range(len(h)):
	# t=sum(h[i:i+241])
	# lmax=max(lmax,t)
# print(lmax)
#1792

#2
# f=open("Z:/11-ПРОФИЛЬ/24data/24-296.txt")
# s=f.readline().replace("CD","C D").split()
# h=list(map(len,s))
# lmax=0
# for i in range(len(h)):
	# t=sum(h[i:i+161])
	# lmax=max(lmax,t)
# print(lmax)
#1288
# f=open("Z:/11-ПРОФИЛЬ/24data/24-296.txt")
# s=f.readline().replace("AF","A F").split()
# h=list(map(len,s))
# lmax=987437892187499
# for i in range(len(h)):
	# t=h[i:i+200]
	# if len(t)>199:
		# g=sum(t)
		# lmax=min(g,lmax)
# print(lmax+2)
#9511
# mmax=0
# f=open("Z:/11-ПРОФИЛЬ/24data/24-298.txt")
# s=f.readline()
# for i in range(len(s)):
	# if (not(s[i] in "-0*")):
		# r=""
		# for j in range(i,len(s)-2):
			# if (not(s[j]+s[j+1] in "*--**")) and (not(s[j]+s[j+1]+s[j+2] in ["-00","*00","-07","*07","-08","*08","-09","*09"])):
				# r+=s[j]
				# if not(r[-1] in "-*"):
					# eval(r)
					# if mmax<len(r):
						# mmax=len(r)
					# else:
						# r=""
						# break
# print(mmax)			
#177

#25
# l=0
# t=[]
# for x in range(600001,1000000):
	# s=[]
	# for i in range(2,int(x**0.5)+1):
		# if (x%i)==0:
			# s.append(i)
			# s.append(x//i)
			# s=sorted(s)
	# for j in s:
		# if j%10==7 and j!=7:
			# l+=1
			# print(x,j)
			# break
	# if l==5:
		# break
#2
l=0
t=[]
for x in range(800001,1000000):
	s=[]
	for i in range(2,int(x**0.5)+1):
		if (x%i)==0:
			s.append(i)
			s.append(x//i)
			s=sorted(s)
	if s:
		h=max(s)+min(s)
		if h%10==4:
			l+=1
			print(x,h)
	if l==5:
		break
#3
# l=0
# t=[]
# for x in range(700001,1000000):
	# s=[]
	# for i in range(2,int(x**0.5)+1):
		# if (x%i)==0:
			# s.append(i)
			# s.append(x//i)
			# s=sorted(s)
	# if s:
		# h=max(s)+min(s)
		# if h%100==14:
			# l+=1
			# print(x,h)
	# if l==5:
		# break
#5
# l=0
# t=[]
# for x in range(799999,1,-1):
	# s=[]
	# for i in range(2,int(x**0.5)+1):
		# if (x%i)==0:
			# s.append(i)
			# s.append(x//i)
			# s=sorted(s)
	# if s:
		# h=max(s)+min(s)
		# if h%10==2:
			# l+=1
			# print(x,h)
	# if l==5:
		# break
# #6
# l=0
# t=[]
# for x in range(1000000,1,-1):
	# s=[]
	# for i in range(2,int(x**0.5)+1):
		# if (x%i)==0:
			# s.append(i)
			# s.append(x//i)
			# s=sorted(s)
	# if s:
		# h=max(s)+min(s)
		# if h%100==18:
			# l+=1
			# print(x,h)
	# if l==5:
		# break
		









