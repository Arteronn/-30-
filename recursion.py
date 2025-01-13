from functools import lru_cache
@lru_cache(None)


# ~ def f(n):
	# ~ if n==1:
		# ~ return 1
	# ~ if n > 1:
		# ~ return 2*n*f(n-1)
# ~ for i in range(2024):
	# ~ f(i)
# ~ print((f(2024)-4 *f(2023))/f(2022))


# ~ def f(n):
	# ~ if n==1:
		# ~ return 1
	# ~ if n>1:
		# ~ return n*f(n-1)
# ~ for i in range(2024):
	# ~ f(i)
# ~ print((2*f(2024)+f(2023))/f(2022))


# ~ from functools import *
# ~ @lru_cache(None)
# ~ def f(n):
	# ~ if n==1:
		# ~ return 1
	# ~ if n>1:
		# ~ return 3*n*f(n-1)
# ~ for i in range(2024):
	# ~ f(i)
# ~ print((f(2024)//6 + f(2023))/f(2022))
# ~ 6147897.0


# ~ from functools import *
# ~ @lru_cache(None)
# ~ def f(n):
	# ~ if n==1:
		# ~ return 1
	# ~ if n>1:
		# ~ return 2*n*f(n-1)
# ~ for i in range(2024):
	# ~ f(i)
# ~ print((f(2024)//16 - f(2023))//f(2022))


# ~ from functools import *
# ~ @lru_cache(None)
# ~ def f(n):
	# ~ if n==1:
		# ~ return 1
	# ~ if n>1:
		# ~ return (n+1)*f(n-1)
# ~ for i in range(2024):
	# ~ f(i)
# ~ print((f(2024)-3*f(2023))/f(2022))


# ~ from functools import *
# ~ @lru_cache(None)
# ~ def f(n):
	# ~ if n==1:
		# ~ return 1
	# ~ if n>1:
		# ~ return (n+1)*f(n-1)
# ~ for i in range(2024):
	# ~ f(i)
# ~ print((f(2024)+3*f(2023))/f(2022))


# ~ from functools import *
# ~ @lru_cache(None)
# ~ def f(n):
	# ~ if n==1:
		# ~ return 1
	# ~ if n>1:
		# ~ return (n+1)*f(n-1)
# ~ for i in range(2024):
	# ~ f(i)
# ~ print((f(2024)+2*f(2023))/f(2022))


# ~ def F(n):
	# ~ if n < 3:
		# ~ return 1
	# ~ elif n >= 3:
		# ~ return (n - 1) * F(n - 2)
# ~ for i in range(2050):
	# ~ F(i)
# ~ print((F(2025) - 2 * F(2023)) / F(2021))


# ~ def F(n):
	# ~ if n < 3:
		# ~ return 1
	# ~ elif n >= 3:
		# ~ return (n - 1) * F(n - 2)
# ~ for i in range(2050):
	# ~ F(i)
# ~ print((F(2026) - 5 * F(2024)) / F(2022))


# ~ def F(n):
	# ~ if n % 2 == 0:
		# ~ return F(n / 2) + 3
	# ~ elif  n % 3 == 0:
		# ~ return F(n / 3) + 2
	# ~ else:
		# ~ return 0
# ~ for i in range(1, 9999999):
	# ~ if F(i) == 65:
		# ~ print(i)
		# ~ break


# ~ def F(n):
	# ~ if n % 2 == 0:
		# ~ return F(n / 2) + 5
	# ~ elif  n % 3 == 0:
		# ~ return F(n / 3) + 4
	# ~ else:
		# ~ return 0
# ~ for i in range(1, 9999999):
	# ~ if F(i) == 108:
		# ~ print(i)
		# ~ break


# ~ def F(n):
	# ~ if n % 2 == 0:
		# ~ return F(n / 2) + 5
	# ~ elif  n % 5 == 0:
		# ~ return F(n / 5) + 2
	# ~ else:
		# ~ return 0
# ~ for i in range(1, 99999999):
	# ~ if F(i) == 130:
		# ~ print(i)
		# ~ break
		
		
# ~ def F(n):
	# ~ if n % 2 == 0:
		# ~ return F(n / 2) + 5
	# ~ elif  n % 5 == 0:
		# ~ return F(n / 5) + 2
	# ~ else:
		# ~ return 0
# ~ A = []
# ~ t = 0
# ~ for i in range(1, 1000001):
	# ~ if not(F(i) in A):
		# ~ A.append(F(i))
		# ~ t += 1
# ~ print(t)


# ~ def F(n):
	# ~ if n < 5:
		# ~ return 1
	# ~ else:
		# ~ return n * 2 * F(n - 4)
# ~ for i in range(13770):
	# ~ F(i)
# ~ print((F(13766) - 9 * F(13762)) / F(13758))
