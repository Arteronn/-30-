from functools import lru_cache
@lru_cache(None)

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


def F(n):
	if n % 2 == 0:
		return F(n / 2) + 3
	elif  n % 3 == 0:
		return F(n / 3) + 2
	else:
		return 0
for i in range(1, 2050):
	if F(i) == 65:
		print(i)
		break


# ~ def F(n):
	# ~ if n % 2 == 0:
		# ~ return F(n / 2) + 5
	# ~ elif  n % 3 == 0:
		# ~ return F(n / 3) + 4
	# ~ else:
		# ~ return 0
# ~ for i in range(1, 2050):
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
# ~ for i in range(1, 2050):
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
# ~ for i in range(1, 2050):
	# ~ if F(i) == 130:
		# ~ print(i)
		# ~ break
