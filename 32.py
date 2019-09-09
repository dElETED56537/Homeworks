products = set()
check = set('123456789')

for i in range(100):
	for j in range(100, 10000):
		s = str(i) + str(j) + str(i * j)
		if len(s) == 9 and set(s) == check:
			products.add(i * j)
		elif len(s) > 9: break

print (sum(products))
