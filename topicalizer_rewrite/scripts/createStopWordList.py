from core import retriever

# initialise language list
languages = ['english',
		     'german',
		     'french',
		     'dutch',
		     'spanish',
		     'italian',
		     'russian',
		     'danish',
		     'norwegian',
		     'portuguese',
		     'swedish']

# compile regular expression for removing trailing spaces
trailingSpaces = re.compile('\,\s$')

# initialise stop word getter
stopWords = retriever.StopWords()

# open output file
outputFile = codecs.open('stopWords.java', 'w', 'utf-8')

# iterate over languages
for language in languages:
    # initialise output string
    outputString = '\t\t// ' + language.title() + '\n\t\tHashtable ' + language + 'StopWords = new Hashtable();\n'

    # get stop word list for language
    stopWordList = stopWords.getStopWordList(language)

    # iterate over stop words
    for stopWord in stopWordList:
		outputString += '\t\t' + language + 'StopWords.put("' + stopWord + '", "1");\n'

    # finalise output string
    outputString = trailingSpaces.sub('', outputString)
    outputString += '\t\tstopWordsTable.put("' + language + '", ' + language + 'StopWords);\n\n'
    outputFile.write(outputString)

# close output file
outputFile.close()

