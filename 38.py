largest = 0

for i in range(1,10000):
	multiplication = ''
	multiplier = 1
	while len(multiplication) < 9:
		multiplication += str(i * multiplier)
		multiplier += 1		
	if ((len(multiplication) == 9) and (len(set(multiplication)) == 9) and ('0' not in multiplication)):
		if int(multiplication) > largest:
			largest = int(multiplication)
print (largest)
