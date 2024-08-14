banana = 0

while banana > 0:
    banana = int(input("How many banana? (type 0 to exit) "))
    if banana >= 5:
        print("I have a bunch of bananas.")
    elif (banana < 5 and banana >= 1):
        print("I have a small bunch of bananas.")
    else:
        print("I have no bananas.")
print("exit program.")