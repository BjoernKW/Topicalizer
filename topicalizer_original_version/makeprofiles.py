import re, os, codecs
from operator import itemgetter
from nltk_lite import tokenize

# n-gram structure function
def getNGramStructure(sourceFile):
    # initialise n-gram dictionary
    ngrams = {}

    # read file
    corpus = sourceFile.read()

    # get tokens separated by whitespaces
    tokenizedCorpus = tokenize.whitespace(corpus)

    # go through each token
    for token in tokenizedCorpus:
	# split token in single characters
	characters = list(token)

	# copy character list
	charactersBuffer = list(characters)

	# initialise buffer
	buffer1 = ''

	# go through character list
	for char1 in characters:
	    # write each n-gram to list
	    buffer1 += char1
	    ngrams[buffer1] = ngrams.get(buffer1, 0) + 1

	    # shift from character list copy
	    charactersBuffer.pop(0)

	    # initialise buffer
	    buffer2 = ''

	    # go through copy of character list
	    for char2 in charactersBuffer:
		buffer2 += char2
		ngrams[buffer2] = ngrams.get(buffer2, 0) + 1

   # return n-grams
    return ngrams

# get directory listing
listOfSourceFiles = os.listdir('languageprofiles/sourcefiles/')

# compile regular expression for files starting with '.'
dotAtBeginning = re.compile('^\.')

# go through each file
for sourceFileName in listOfSourceFiles:
    # process, if no '.' at beginning of source file name
    if dotAtBeginning.findall(sourceFileName):
	pass
    else:
	# open source and profile file
	sourceFile = codecs.open('languageprofiles/sourcefiles/' + sourceFileName, 'r', 'iso-8859-1')
	profileFile = codecs.open('languageprofiles/' + sourceFileName, 'w', 'iso-8859-1')

	# get n-grams from source file
	ngrams = getNGramStructure(sourceFile)

	# sort n-grams and go through each n-gram and write it to profile
	for ngram, ngramValue in sorted(ngrams.iteritems(), key = itemgetter(1), reverse = True):
	    profileFile.write(ngram + '\n')
