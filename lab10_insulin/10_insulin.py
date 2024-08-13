seq = ""
with open('preproinsulin-seq.txt') as txtFile:
    for row in txtFile:
        seq += row.strip()  # strip() removes leading and trailing whitespace, including newlines

# Clean the sequence by removing unwanted characters
seq = seq.replace('ORIGIN', '').replace(' ', '').replace('//', '')
seq = ''.join([c for c in seq if not c.isdigit()])  # Removes all digits

print(len(seq))
print(seq)

# Define the output files and their respective start and end positions
newFiles = [["lsinsulin-seq-clean.txt", 0, 24],
            ["binsulin-seq-clean.txt", 24, 54],
            ["cinsulin-seq-clean.txt", 54, 89],
            ["ainsulin-seq-clean.txt", 89, 110]]

# Write the specified subsequences to their respective files
for myFile in newFiles:
    myFileName = myFile[0]
    myStart = myFile[1]
    myEnd = myFile[2]
    with open(myFileName, 'w') as outFile:  # Open the file in write mode
        outFile.write(seq[myStart:myEnd])  # Write the sequence slice to the file
    print("Saved file: {}".format(myFileName))