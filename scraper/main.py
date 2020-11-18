import csv
# Import the requests module. This module is used for grabbing static HTML content.
import requests
# Import the BeautifulSoup module from the bs4 package. This module is used for parsing HTML content.
from bs4 import BeautifulSoup

# This function extracts arabic words and their latin transliterations/romanizations, from wiktionary pages.
def extractData (soup):
    # Init ouput var.
    output = []

    # Grab all of the arabic words by looking for "strong" tags with the class "Arab headword".
    arabicWords = soup.find_all('strong', class_='Arab headword')

    # Loop through all of the arabic words.
    for arabicWord in arabicWords:
        # Grab the latin transliteration/romanization for the current arabic word by moving to the parent tag of the word and looking for a "strong" tag with the class "headword-tr tr Latn".
        latinWord = arabicWord.parent.find('span', class_="headword-tr tr Latn")
        # Check that there is, in fact, a latin transliteration/romanization for the present arabic word.
        if latinWord:
            # Store the arabic word and its latin transliteration/romanization.
            output.append([arabicWord.text, latinWord.text])
    
    # Return the output var.
    return output

# This function gets a word list to be used for querying wiktionary.
def getWordList ():
    # Open hermitdave's FrequencyWords' 50k Arabic word list.
    with open('../dataset/wordlists/hermitdave_frequencywords_ar_50k.csv', encoding='utf-8-sig') as wordListCsv:
        # Store the word list in wordList.
        wordList = list(csv.reader(wordListCsv, delimiter=' '))
    # Close wordListCsv.
    wordListCsv.close()
    # Return the wordList.
    return wordList

# This function saves output data to output.csv.
def saveOutput (output):
    with open('../dataset/raw/output.csv', 'a', encoding='utf-8-sig', newline='') as outputFile:
        writer = csv.writer(outputFile)
        writer.writerows(output)
    outputFile.close()

# Init variable to store the final output.
output = []

# Store the word list.
wordList = getWordList()

# Init variable to count number of words [in words list] processed (before save) (not including skipped words).
wordsProcessedCount = 0

# Init variable to count words [in words list] processed (including skipped words).
OverallWordsProcessedCount = 0
# Loop through the wordList.
for word in wordList:
    OverallWordsProcessedCount = OverallWordsProcessedCount+1
    # Add to wordsProcessedCount.
    wordsProcessedCount = wordsProcessedCount + 1
    # Set the URL to be scraped.
    URL = "https://en.wiktionary.org/wiki/"+word[0]

    # Grab and store the HTML content of the URL.
    page = requests.get(URL)

    # Ensure that the URL exists. If it doesn't, skip this word.
    if page.status_code == 404:
        continue

    # Create a BeautifulSoup object to parse the content contained within the new 'page' var.
    ## There are three key options for parsers with bs4:
    ## 1. html5lib - very slow, extremely lenient (great for broken HTML).
    ## 2. html.parser - battries included, decent speed, lenient.
    ## 3. lxml - very fast, lenient.
    ## [Note: taken from: https://stackoverflow.com/questions/45494505/python-difference-between-lxml-and-html-parser-and-html5lib-with-beautifu]
    soup = BeautifulSoup(page.content, 'lxml')

    # Extract Arabic words and transliterations from the page.
    extractedData = extractData(soup)

    # Store the extractedData in the output.
    # Loop through each element in extractedData.
    for element in extractedData:
        # Append the element to output.
        output.append(element)
    
    # Check if wordsProcessedCount is greater than 499. If it is, save the output and reset the count.
    if wordsProcessedCount > 499:
        wordsProcessedCount = 0
        saveOutput(output)
        output = []
        print(OverallWordsProcessedCount)

# Check if there is still data waiting to be saved.
if output != []:
    # Save the remaining data.
    saveOutput(output)
