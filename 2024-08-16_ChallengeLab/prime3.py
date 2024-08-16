prime = [str(num) for num in range(2, 251) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

print("Prime Numbers: "+", ".join(prime))

with open("results3.txt", "w") as txtFile:
    txtFile.write("\n".join(prime))