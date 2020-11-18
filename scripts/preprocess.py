import csv
import random

# This function checks if a latin transliteration begins, or ends, with a hyphen.
def isHyphen(latinText):
    if latinText[0] == '-' or latinText[len(latinText)-1] == '-':
        return True
    else:
        return False

# Open combined csv and save data into a local variable.
with open('../dataset/raw/output.csv', encoding='utf-8-sig') as combinedCsv:
    combinedData = list(csv.reader(combinedCsv, delimiter=','))
combinedCsv.close()

newCombinedData = []

# Count dupes.
dupesCount = 0

# Count words that begin, or end, with a hyphen.
hyphenWords = 0

# Find and remove duplicates. Also remove words that begin, or end, with a hyphen.
for item in combinedData:
    # If the word begins, or ends, with a hyphen, exclude it.
    if isHyphen(item[1]):
        hyphenWords = hyphenWords+1
        continue
    # Check for dupes. If dupe, don't include in new data var.
    if item not in newCombinedData:
        newCombinedData.append(item)
    else:
        dupesCount = dupesCount+1

# Randomly shuffle the list.
random.shuffle(newCombinedData)

# Save arabic data.
arabicDoc = open("../dataset/processed/phonetik.arabic", "w+", encoding='utf-8-sig')

for item in newCombinedData:
    arabicDoc.write(item[0]+"\n")

arabicDoc.close()

# Save latin data.
latinDoc = open("../dataset/processed/phonetik.latin", "w+", encoding='utf-8-sig')

for item in newCombinedData:
    latinDoc.write(item[1]+"\n")

latinDoc.close()

print("hyphen words: ", hyphenWords,"\n")
print("dupes: ", dupesCount, "\n")
