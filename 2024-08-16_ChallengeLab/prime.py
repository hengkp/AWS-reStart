# Function to check prime number
def is_prime(num):
	if num < 2:
		return False
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return False
	return True

# Apply to 1-250 range
prime = [str(num) for num in range(1, 251) if is_prime(num)]

# Print the prime number
print("Prime Numbers: "+", ".join(prime))

# Save to file
with open("results.txt", "w") as txtFile:
	txtFile.write("\n".join(prime))