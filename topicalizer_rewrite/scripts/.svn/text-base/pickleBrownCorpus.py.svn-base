import pickle, re
from nltk import tokenize
from core import retriever

# set path
path = '../core/corpora/brown/'

# set categories
categories = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r']

# compile regular expression for sentence-boundary matching
sentenceBoundary = re.compile(r'[\.\:\!\?]')

# compile regular expression for special character matching
specialCharacters = re.compile(r'[\.\:\!\?\,\;]')

# compile regular expression for tag matching
tag = re.compile(r'\/.+?$')

# compile regular expression for matching carriage returns
cr = re.compile(r'[\n]')

# initialise stop word getter
stopWords = retriever.StopWords()

# get stop word list
stopWordList = stopWords.getStopWordList('english')

# initialise word and sentence buffers
words = []
sentences = []
sentence = ''

# read files
for category in categories:
    # show category
    print category

    # initialise
    corpus = ''
    sentenceString = ''
    words = []
    sentences = []

    # initialise co-occurrence matrix
    coOccurrences = {}

    # open file
    file = open(path + category, 'r')

    # add each line to corpus
    for line in file:
    	corpus += line

    # close file pointer
    file.close()

    # get tokens from corpus
    tokenizedCorpus = tokenize.whitespace(corpus)

    # go through tokens
    for token in tokenizedCorpus:
    	# add token to sentence
    	words.append(tag.sub('', token))

	# if sentence-boundary has been found in this token
	if sentenceBoundary.findall(token):
	    # recompose sentence
	    for word in words:
    		sentenceString += word + ' '

	    # add to sentence string list
	    sentences.append(sentenceString)

	    # empty word list
	    words[0:] = []

	    # empty sentence string
	    sentenceString = ''

    # go through each sentence
    for sentence in sentences:
    	# tokenize sentence
    	tokenizedSentence = list(tokenize.whitespace(cr.sub('', sentence)))

	# go through each token
	for token in tokenizedSentence:
	    # to lower case
	    token = token.lower()

	    # if token is in stop word list, discard it
	    if token in stopWordList:
    		pass
	    else:
    		# initialise co-occurrence matrix
    		if coOccurrences.get(token, 0) == 0:
    		    coOccurrences[token] = {}
    		thisCoOccurrences = coOccurrences[token]

		# for each token go through each token
		for token2 in tokenizedSentence:
		    # to lower case
		    token2 = token2.lower()

		    # if token is in stop word list, discard it
		    if token2 in stopWordList or token2 == token or specialCharacters.search(token2) or token2 == '\'' or token2 == '\'\'' or token2 == '\`\`' or token2 == '\`' or len(token2) < 3:
    			pass
		    else:
    			# get co-occurrences
    			thisCoOccurrences[token2] = thisCoOccurrences.get(token2, 0) + 1

		# write co-occurrences to main matrix
		coOccurrences[token] = thisCoOccurrences

    # open pickle dump file
    dump = open(path + category + '.co.dump', 'w')

    # pickle co-occurence matrix
    pickle.dump(coOccurrences, dump)

    # close dump file
    dump.close()
