prime = []
for num in range(1,251):
	if num < 2:
		is_prime = False
	else:
		is_prime = True
	for i in range(2, int(num**0.5)+1):
		if num % i == 0:
			is_prime = False
			break
	if is_prime:
		prime.append(str(num))

print(prime)

with open("results2.txt","w") as txtFile:
	txtFile.write("\n".join(prime))