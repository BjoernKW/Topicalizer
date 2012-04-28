import re, MySQLdb
from core import retriever
from nltk import tokenize

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

# connect to database and get cursor
db = MySQLdb.connect('', 'topicalizer', '0fe73f7a', 'topicalizer')
cursor = db.cursor()

# read files
for category in categories:
    # show category
    print category

    # initialise
    corpus = ''
    sentenceString = ''
    words = []
    sentences = []
    rowID = 0

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
    		# check, if token already is in database, otherwise insert it
    		sqlCmd = 'SELECT * FROM token_by_category WHERE token=%s AND category=%s'
    		parameters = (token, category)
    		cursor.execute(sqlCmd, parameters)
    		row = cursor.fetchone()

		# does token already exist for this category?
		if row != None:
		    # get row ID
		    rowID = str(row[0])
		else:
		    # if not, insert it
		    sqlCmd = 'INSERT INTO token_by_category (token,category) VALUE (%s,%s)'
		    parameters = (token, category)
		    cursor.execute(sqlCmd, parameters)

		    # get row ID
		    rowID = str(cursor.lastrowid)

		# for each token go through each token
		for token2 in tokenizedSentence:
		    # to lower case
		    token2 = token2.lower()

		    # if token is in stop word list, discard it
		    if token2 in stopWordList or token2 == token or specialCharacters.search(token2) or token2 == '\'' or token2 == '\'\'' or token2 == '\`\`' or token2 == '\`' or len(token2) < 3:
    			pass
		    else:
    			# check, if token already is in database, otherwise insert it
    			sqlCmd = 'SELECT * FROM co_occurrence WHERE token=%s AND co_occurs_with=%s'
    			parameters = (token2, rowID)
    			cursor.execute(sqlCmd, parameters)
    			row2 = cursor.fetchone()

			# does token already exist for this category?
			if row2 != None:
			    # get row ID
			    rowID2 = str(row2[0])

			    # update row
			    sqlCmd = 'UPDATE co_occurrence SET count=count+1 WHERE id=%s'
			    parameters = (rowID2)
			    cursor.execute(sqlCmd, parameters)
			else:
			    # insert row
			    sqlCmd = 'INSERT INTO co_occurrence (token,co_occurs_with) VALUE (%s,%s)'
			    parameters = (token2,rowID)
			    cursor.execute(sqlCmd, parameters)

# close database connection
db.close()
