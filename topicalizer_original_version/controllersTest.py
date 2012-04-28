from __future__ import division
import turbogears
from turbogears import controllers

class Root(controllers.Root):
    # initialise language list
    languages = ['automatic',
		 'english',
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

    # initialise text categories dictionary
    textCategories = dict(a = 'Press: Reportage',
			  b = 'Press: Editorial',
			  c = 'Press: Reviews',
			  d = 'Religion',
			  e = 'Skill and Hobbies',
			  f = 'Popular Lore',
			  g = 'Belles-Lettres',
			  h = 'Miscellaneous: Government & House Organs',
			  j = 'Learned',
			  k = 'Fiction: General',
			  l = 'Fiction: Mystery',
			  m = 'Fiction: Science',
			  n = 'Fiction: Adventure',
			  p = 'Fiction: Romance',
			  r = 'Humour')

    @turbogears.expose(template='topicalizer.templates.welcome', format='xhtml', content_type='text/html')
    def index(self):
        import time

	# initialise language list
	languages = self.languages

        return dict(now=time.ctime(),
		    languages = languages)

    @turbogears.expose(template='topicalizer.templates.augmentKeywords', format='xhtml', content_type='text/html')
    def augmentKeywords(self):
        import time

	# initialise language list
	languages = self.languages

        return dict(now=time.ctime(),
		    languages = languages)

    @turbogears.expose(template='topicalizer.templates.coOccurrences', format='xhtml', content_type='text/html')
    def coOccurrences(self):
        import time
	from operator import itemgetter

	# initialise language list
	languages = self.languages

	# initialise text categories dictionary
	textCategories = self.textCategories

        return dict(now=time.ctime(),
		    languages = languages,
		    textCategories = sorted(textCategories.iteritems(), key = itemgetter(0), reverse = False))

    @turbogears.expose(template='topicalizer.templates.similarDocuments', format='xhtml', content_type='text/html')
    def similarDocuments(self):
        import time

	# initialise language list
	languages = self.languages

        return dict(now=time.ctime(),
		    languages = languages)

    @turbogears.expose(template='topicalizer.templates.tagging', format='xhtml', content_type='text/html')
    def tagging(self):
        import time
        return dict(now=time.ctime())

    @turbogears.expose(template='topicalizer.templates.processTagging', format='xhtml', content_type='text/html')
    def processTagging(self, plainText = '', language = 'automatic', **kw):
	import retriever, analyser, re, urllib
	from operator import itemgetter
	from reverend.thomas import Bayes

	# initialise charset
	charset = ''

	# initialise corpus
	corpus = ''

	# initialise language list
	languages = self.languages

	# initialise error string
	error = 0
	errorMessage = ''

	# initialise fallback status
	fallback = 0

	# if text
	if plainText != '':
	    # decode text
	    plainText = urllib.unquote(plainText)

	    # codify corpus
	    charset = 'utf-8'
	    corpus = unicode(plainText, charset, 'replace')

	    # stop word list
	    stopWords = retriever.StopWords()

	    # tokenizer
	    tokenizer = analyser.Tokenizer()

	    # set language to English
	    language = 'english'

	    # get appropriate stop word list for language
	    stopWordList = stopWords.getStopWordList(language)

	    # tokenize, get paragraphs
	    tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 1))

	    # get token count
	    tokenCount = len(tokenizedCorpus)

	    # analyse sentence structure
	    sentenceStructure = analyser.SentenceStructure()

	    # build return dictionary
	    returnDict = dict(corpus = corpus,
			      error = error,
			      errorMessage = errorMessage,
			      languageTitle = language.title(),
			      languages = languages,
			      charset = charset,
			      fallback = fallback,
			      debug = 0)

	# if error
	else:
	    # set corpus to empty value
	    corpus = ''

	    # build return dictionary
	    returnDict = dict(corpus = corpus,
			      error = error,
			      errorMessage = errorMessage,
			      fallback = fallback,
			      debug = 1)

	# return values
	return returnDict

    @turbogears.expose(template='topicalizer.templates.about', format='xhtml', content_type='text/html')
    def about(self):
        import time
        return dict(now=time.ctime())

    @turbogears.expose(template='topicalizer.templates.faq', format='xhtml', content_type='text/html')
    def faq(self):
        import time
        return dict(now=time.ctime())

    @turbogears.expose(template='topicalizer.templates.links', format='xhtml', content_type='text/html')
    def links(self):
        import time
        return dict(now=time.ctime())

    @turbogears.expose(template='topicalizer.templates.api', format='xhtml', content_type='text/html')
    def api(self):
	from operator import itemgetter

	# initialise language list
	languages = self.languages

	# initialise text categories dictionary
	textCategories = self.textCategories

        return dict(languages = languages,
		    textCategories = sorted(textCategories.iteritems(), key = itemgetter(0), reverse = False))

    @turbogears.expose(template='topicalizer.templates.tools', format='xhtml', content_type='text/html')
    def tools(self):
        import time
        return dict(now=time.ctime())

    @turbogears.expose(template='topicalizer.templates.terms', format='xhtml', content_type='text/html')
    def terms(self):
        import time
        return dict(now=time.ctime())

    @turbogears.expose(template='topicalizer.templates.contact', format='xhtml', content_type='text/html')
    def contact(self):
        import time
        return dict(now=time.ctime())

    @turbogears.expose(template='topicalizer.templates.disclaimer', format='xhtml', content_type='text/html')
    def disclaimer(self):
        import time
        return dict(now=time.ctime())

    @turbogears.expose(template='topicalizer.templates.getCompleteAnalysis', format='xml', content_type='text/xml')
    def getCompleteAnalysis(self, url = '', plainText = '', language = 'automatic', **kw):
	import retriever, analyser, re, urllib, smtplib
	from email.MIMEText import MIMEText
	from operator import itemgetter
	from reverend.thomas import Bayes

	# initialise charset
	charset = ''

	# initialise corpus
	corpus = ''

	# initialise language list
	languages = self.languages

	# initialise error string
	error = 0
	errorMessage = ''

	# initialise fallback status
	fallback = 0

	# if URL
	if url != 'Enter URL' and url != '':
	    # decode url
	    url = urllib.unquote(url)

	    # instantiate URL retriever class
	    urlRetriever = retriever.URLRetriever()

	    # try retrieval of URL
	    try:
		corpusSet = urlRetriever.retrieveURL(url)
		corpus = corpusSet['corpus']
		charset = corpusSet['charset']
	    except IOError:
		error = 1
		errorMessage = 'URL could not be retrieved'

	# if text
	elif plainText != '':
	    # decode text
	    plainText = urllib.unquote(plainText)

	    # set URL for display
	    url = 'text'

	    # codify corpus
	    charset = 'utf-8'
	    corpus = unicode(plainText, charset, 'replace')

	# if retrieval was successful
	if error != 1:
	    # ML tag stripper
	    mlStripper = retriever.MLStripper()

	    # try removing ML tags
	    try:
		mlStripper.feed(corpus)
		corpus = mlStripper.getStripped()
	    except:
		# handle tags with fallback method
		mlFallback = retriever.MLFallback()
		corpus = mlFallback.getStripped(corpus)
		fallback = 1

		# dispatch an e-mail
		msg = MIMEText('The URL' + url + 'could not be parsed, using fallback instead.')
		msg['Subject'] = 'URL could not be parsed:' + url
		msg['From'] = 'webmaster@topicalizer.com'
		msg['To'] = 'bjoern@topicalizer.com'

		# send via SMTP
		s = smtplib.SMTP()

		# try to connect
	        try:
	            s.connect()
	            s.sendmail(msg['From'], msg['To'], msg.as_string())
	            s.close()
		except:
		    pass

	    # stop word list
	    stopWords = retriever.StopWords()

	    # tokenizer
	    tokenizer = analyser.Tokenizer()

	    # analyse word structure
	    wordStructure = analyser.WordStructure()

	    # if language is set to 'automatic', try to guess language by Bayesian classification
	    if language == 'automatic':
		# instantiate guesser
		guesser = Bayes()

		# go through language in order to train guesser
		for selectLanguage in languages:
		    if selectLanguage != 'automatic':
			stopWordString = stopWords.getStopWordString(selectLanguage)
			guesser.train(selectLanguage, stopWordString)
			
		# get list of possible languages
		languageGuesses = guesser.guess(corpus)

		# get most probable language
		try:
		    language = languageGuesses.pop(0)[0]
		except IndexError:
		    language = 'english'

	    # get appropriate stop word list for language
	    stopWordList = stopWords.getStopWordList(language)

	    # tokenize, get paragraphs
	    if language == 'german':
		tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 1))
	    else:
		tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 0))
	    paragraphs = list(tokenizer.processParagraphs(corpus))

	    # get types, characters, sentences
	    typesCharactersSentences = wordStructure.getTypesCharactersSentences(tokenizedCorpus)
	    types = list(typesCharactersSentences['types'])
	    sentences = list(typesCharactersSentences['sentences'])
	    sentenceStrings = list(typesCharactersSentences['sentenceStrings'])
	    charactersPerToken = list(typesCharactersSentences['charactersPerToken'])
	    maxSentenceLength = typesCharactersSentences['maxSentenceLength']
	    minSentenceLength = typesCharactersSentences['minSentenceLength']
	    maxTokenLength = typesCharactersSentences['maxTokenLength']
	    minTokenLength = typesCharactersSentences['minTokenLength']
	    maxSentence = typesCharactersSentences['maxSentence']
	    minSentence = typesCharactersSentences['minSentence']
	    maxToken = typesCharactersSentences['maxToken']
	    minToken = typesCharactersSentences['minToken']
	    sumOfCharacters = typesCharactersSentences['sumOfCharacters']

	    # calculate some average values
	    paragraphCount = len(paragraphs)
	    tokenCount = len(tokenizedCorpus)
	    typeCount = len(types)
	    sentenceCount = len(sentences)

	    # if token count is not 0
	    if tokenCount != 0:
		lexicalDensity = round(typeCount / tokenCount, 2)
		averageCharactersPerWord = round(sumOfCharacters / tokenCount, 2)
	    else:
		lexicalDensity = 0
		averageCharactersPerWord = 0

	    # if sentence count is not 0
	    if sentenceCount != 0:
		averageTokensPerSentence = round(tokenCount / sentenceCount, 2)
		averageTokensPerParagraph = round(tokenCount / paragraphCount, 2)
	    else:
		averageTokensPerSentence = 0
		averageTokensPerParagraph = 0

	    # if paragraph count is not 0
	    if paragraphCount != 0:
		averageSentencesPerParagraph = round(sentenceCount / paragraphCount, 2)
	    else:
		averageSentencesPerParagraph = 0

	    # syllables
	    syllableInformation = wordStructure.getSyllableInformation(tokenizedCorpus, types)
	    totalSyllables = syllableInformation['sum']
	    syllablesPerToken = syllableInformation['syllablesPerToken']
	    syllablesPerType = syllableInformation['syllablesPerType']

	    # if token count is not 0
	    if tokenCount != 0:
		averageSyllablesPerWord = round(totalSyllables / tokenCount, 2)
	    else:
		averageSyllablesPerWord = 0

	    # analyse text structure
	    textStructure = analyser.TextStructure()

	    # get N-grams
	    ngrams = textStructure.getNGrams(tokenizedCorpus, tokenCount)
	    mostFrequentUnigrams = ngrams['mostFrequentUnigrams']
	    mostFrequentUnigramsAbstract = ngrams['mostFrequentUnigramsAbstract']
	    mostFrequentBigrams = ngrams['mostFrequentBigrams']
	    mostFrequentTrigrams = ngrams['mostFrequentTrigrams']
	    mostFrequentBigramsWithStopWords = ngrams['mostFrequentBigramsWithStopWords']
	    mostFrequentTrigramsWithStopWords = ngrams['mostFrequentTrigramsWithStopWords']

	    # get keywords
	    keywords = list(textStructure.getKeywords(mostFrequentUnigrams, mostFrequentBigrams, mostFrequentTrigrams, mostFrequentBigramsWithStopWords, mostFrequentTrigramsWithStopWords))

	    # get abstract
	    abstract = textStructure.getAbstract(mostFrequentUnigramsAbstract, sentenceStrings)

	    # if token count is 0
	    if tokenCount == 0:
		readabilityGF = 0
		readabilityCL = 0
	    else:
		# readability according to Gunning-Fog Index
		readabilityGF = textStructure.analyseReadabilityGF(averageTokensPerSentence, syllablesPerType, tokenCount)

		# readability according to Coleman-Liau Index
		readabilityCL = textStructure.analyseReadabilityCL(averageCharactersPerWord, sentenceCount, tokenCount)

	    # readability according to Automated Readability Index
	    readabilityAR = textStructure.analyseReadabilityAR(averageCharactersPerWord, averageTokensPerSentence)

	    # average readability
	    readabilityAverage = round((readabilityGF + readabilityAR + readabilityCL) / 3, 2)

	    # build return dictionary
	    returnDict = dict(corpus = corpus,
			      languageTitle = language.title(),
			      languages = languages,
			      stopWordList = stopWordList,
			      error = error,
			      errorMessage = errorMessage,
			      charset = charset,
			      paragraphCount = paragraphCount,
			      sentenceCount = sentenceCount,
			      tokenCount = tokenCount,
			      typeCount = typeCount,
			      lexicalDensity = lexicalDensity,
			      averageCharactersPerWord = averageCharactersPerWord,
			      averageSyllablesPerWord = averageSyllablesPerWord,
			      mostFrequentUnigrams = sorted(mostFrequentUnigrams.iteritems(), key = itemgetter(1), reverse = True),
			      mostFrequentBigrams = sorted(mostFrequentBigrams.iteritems(), key = itemgetter(1), reverse = True),
			      mostFrequentTrigrams = sorted(mostFrequentTrigrams.iteritems(), key = itemgetter(1), reverse = True),
			      mostFrequentBigramsWithStopWords = sorted(mostFrequentBigramsWithStopWords.iteritems(), key = itemgetter(1), reverse = True),
			      mostFrequentTrigramsWithStopWords = sorted(mostFrequentTrigramsWithStopWords.iteritems(), key = itemgetter(1), reverse = True),
			      keywords = keywords,
			      abstract = sorted(abstract.iteritems(), key = itemgetter(1), reverse = True)[0:5],
			      readabilityGF = readabilityGF,
			      readabilityAR = readabilityAR,
			      readabilityCL = readabilityCL,
			      readabilityAverage = readabilityAverage,
			      averageTokensPerSentence = averageTokensPerSentence,
			      averageTokensPerParagraph = averageTokensPerParagraph,
			      averageSentencesPerParagraph = averageSentencesPerParagraph,
			      maxSentenceLength = maxSentenceLength,
			      minSentenceLength = minSentenceLength,
			      maxTokenLength = maxTokenLength,
			      minTokenLength = minTokenLength,
			      maxSentence = maxSentence,
			      minSentence = minSentence,
			      maxToken = maxToken,
			      minToken = minToken,
			      debug = 0,
			      url = unicode(url, 'utf-8', 'replace'))

	# if URL retrieval error
	else:
	    # set corpus to empty value
	    corpus = ''

	    # build return dictionary
	    returnDict = dict(corpus = corpus,
			      error = error,
			      errorMessage = errorMessage,
			      fallback = fallback,
			      debug = 1,
			      url = unicode(url, 'utf-8', 'replace'))

	# return values
	return returnDict

    @turbogears.expose(template='topicalizer.templates.getKeywords', format='xml', content_type='text/xml')
    def getKeywords(self, url = '', plainText = '', language = 'automatic', **kw):
	import retriever, analyser, re, urllib, smtplib
	from email.MIMEText import MIMEText
	from operator import itemgetter
	from reverend.thomas import Bayes

	# initialise charset
	charset = ''

	# initialise corpus
	corpus = ''

	# initialise language list
	languages = self.languages

	# initialise error string
	error = 0
	errorMessage = ''

	# initialise fallback status
	fallback = 0

	# if URL
	if url != 'Enter URL' and url != '':
	    # decode url
	    url = urllib.unquote(url)

	    # instantiate URL retriever class
	    urlRetriever = retriever.URLRetriever()

	    # try retrieval of URL
	    try:
		corpusSet = urlRetriever.retrieveURL(url)
		corpus = corpusSet['corpus']
		charset = corpusSet['charset']
	    except IOError:
		error = 1
		errorMessage = 'URL could not be retrieved'

	# if text
	elif plainText != '':
	    # decode text
	    plainText = urllib.unquote(plainText)

	    # set URL for display
	    url = 'text'

	    # codify corpus
	    charset = 'utf-8'
	    corpus = unicode(plainText, charset, 'replace')

	# if retrieval was successful
	if error != 1:
	    # ML tag stripper
	    mlStripper = retriever.MLStripper()

	    # try removing ML tags
	    try:
		mlStripper.feed(corpus)
		corpus = mlStripper.getStripped()
	    except:
		# handle tags with fallback method
		mlFallback = retriever.MLFallback()
		corpus = mlFallback.getStripped(corpus)
		fallback = 1

		# dispatch an e-mail
		msg = MIMEText('The URL' + url + 'could not be parsed, using fallback instead.')
		msg['Subject'] = 'URL could not be parsed:' + url
		msg['From'] = 'webmaster@topicalizer.com'
		msg['To'] = 'bjoern@topicalizer.com'

		# send via SMTP
		s = smtplib.SMTP()

		# try to connect
	        try:
	            s.connect()
	            s.sendmail(msg['From'], msg['To'], msg.as_string())
	            s.close()
		except:
		    pass

	    # stop word list
	    stopWords = retriever.StopWords()

	    # tokenizer
	    tokenizer = analyser.Tokenizer()

	    # if language is set to 'automatic', try to guess language by Bayesian classification
	    if language == 'automatic':
		# instantiate guesser
		guesser = Bayes()

		# go through language in order to train guesser
		for selectLanguage in languages:
		    if selectLanguage != 'automatic':
			stopWordString = stopWords.getStopWordString(selectLanguage)
			guesser.train(selectLanguage, stopWordString)
			
		# get list of possible languages
		languageGuesses = guesser.guess(corpus)

		# get most probable language
		try:
		    language = languageGuesses.pop(0)[0]
		except IndexError:
		    language = 'english'

	    # get appropriate stop word list for language
	    stopWordList = stopWords.getStopWordList(language)

	    # tokenize, get paragraphs
	    if language == 'german':
		tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 1))
	    else:
		tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 0))

	    # get token count
	    tokenCount = len(tokenizedCorpus)

	    # analyse text structure
	    textStructure = analyser.TextStructure()

	    # get N-grams
	    ngrams = textStructure.getNGrams(tokenizedCorpus, tokenCount)
	    mostFrequentUnigrams = ngrams['mostFrequentUnigrams']
	    mostFrequentBigrams = ngrams['mostFrequentBigrams']
	    mostFrequentTrigrams = ngrams['mostFrequentTrigrams']
	    mostFrequentBigramsWithStopWords = ngrams['mostFrequentBigramsWithStopWords']
	    mostFrequentTrigramsWithStopWords = ngrams['mostFrequentTrigramsWithStopWords']

	    # get keywords
	    keywords = list(textStructure.getKeywords(mostFrequentUnigrams, mostFrequentBigrams, mostFrequentTrigrams, mostFrequentBigramsWithStopWords, mostFrequentTrigramsWithStopWords))

	    # build return dictionary
	    returnDict = dict(error = error,
			      errorMessage = errorMessage,
			      mostFrequentUnigrams = sorted(mostFrequentUnigrams.iteritems(), key = itemgetter(1), reverse = True),
			      keywords = keywords,
			      fallback = fallback,
			      debug = 0,
			      url = unicode(url, 'utf-8', 'replace'))

	# if URL retrieval error
	else:
	    # set corpus to empty value
	    corpus = ''

	    # build return dictionary
	    returnDict = dict(corpus = corpus,
			      error = error,
			      errorMessage = errorMessage,
			      fallback = fallback,
			      debug = 1,
			      url = unicode(url, 'utf-8', 'replace'))

	# return values
	return returnDict

    @turbogears.expose(template='topicalizer.templates.getCoOccurrences', format='xml', content_type='text/xml')
    def getCoOccurrences(self, plainText = '', language = 'automatic', textCategory = 'a', **kw):
	import retriever, analyser, re, urllib
	from operator import itemgetter
	from reverend.thomas import Bayes

	# initialise charset
	charset = ''

	# initialise corpus
	corpus = ''

	# initialise language list
	languages = self.languages

	# initialise text categories dictionary
	textCategories = self.textCategories

	# initialise error string
	error = 0
	errorMessage = ''

	# initialise fallback status
	fallback = 0

	# if text
	if plainText != '':
	    # decode text
	    plainText = urllib.unquote(plainText)

	    # codify corpus
	    charset = 'utf-8'
	    corpus = unicode(plainText, charset, 'replace')

	    # stop word list
	    stopWords = retriever.StopWords()

	    # tokenizer
	    tokenizer = analyser.Tokenizer()

	    # set language to English
	    language = 'english'

	    # get appropriate stop word list for language
	    stopWordList = stopWords.getStopWordList(language)

	    # tokenize, get paragraphs
	    tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 1))

	    # get token count
	    tokenCount = len(tokenizedCorpus)

	    # analyse sentence structure
	    sentenceStructure = analyser.SentenceStructure()

	    # get keywords
	    keywords = list(sentenceStructure.getCoOccurrencesFromDB(stopWordList, tokenizedCorpus, textCategory))

	    # build return dictionary
	    returnDict = dict(error = error,
			      errorMessage = errorMessage,
			      keywords = keywords,
			      fallback = fallback,
			      debug = 0)

	# if error
	else:
	    # set corpus to empty value
	    corpus = ''

	    # build return dictionary
	    returnDict = dict(corpus = corpus,
			      error = error,
			      errorMessage = errorMessage,
			      fallback = fallback,
			      debug = 1)

	# return values
	return returnDict

    @turbogears.expose(template='topicalizer.templates.getAugmentedKeywords', format='xml', content_type='text/xml')
    def getAugmentedKeywords(self, plainText = '', language = 'automatic', **kw):
	import retriever, analyser, re, urllib
	from operator import itemgetter
	from reverend.thomas import Bayes

	# initialise charset
	charset = ''

	# initialise corpus
	corpus = ''

	# initialise language list
	languages = self.languages

	# initialise error string
	error = 0
	errorMessage = ''

	# initialise fallback status
	fallback = 0

	# if text
	if plainText != '':
	    # decode text
	    plainText = urllib.unquote(plainText)

	    # codify corpus
	    charset = 'utf-8'
	    corpus = unicode(plainText, charset, 'replace')

	    # stop word list
	    stopWords = retriever.StopWords()

	    # tokenizer
	    tokenizer = analyser.Tokenizer()

	    # set language to English
	    language = 'english'

	    # get appropriate stop word list for language
	    stopWordList = stopWords.getStopWordList(language)

	    # tokenize, get paragraphs
	    tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 0))

	    # get token count
	    tokenCount = len(tokenizedCorpus)

	    # analyse sentence structure
	    sentenceStructure = analyser.SentenceStructure()

	    # get keywords
	    keywords = list(sentenceStructure.augmentKeywordsFromSentence(stopWordList, tokenizedCorpus))

	    # build return dictionary
	    returnDict = dict(error = error,
			      errorMessage = errorMessage,
			      keywords = keywords,
			      fallback = fallback,
			      debug = 0)

	# if error
	else:
	    # set corpus to empty value
	    corpus = ''

	    # build return dictionary
	    returnDict = dict(corpus = corpus,
			      error = error,
			      errorMessage = errorMessage,
			      fallback = fallback,
			      debug = 1)

	# return values
	return returnDict

    @turbogears.expose(template='topicalizer.templates.processAugmentedKeywords', format='xhtml', content_type='text/html')
    def processAugmentedKeywords(self, plainText = '', language = 'automatic', **kw):
	import retriever, analyser, re, urllib
	from operator import itemgetter
	from reverend.thomas import Bayes

	# initialise charset
	charset = ''

	# initialise corpus
	corpus = ''

	# initialise language list
	languages = self.languages

	# initialise error string
	error = 0
	errorMessage = ''

	# initialise fallback status
	fallback = 0

	# if text
	if plainText != '':
	    # decode text
	    plainText = urllib.unquote(plainText)

	    # codify corpus
	    charset = 'utf-8'
	    corpus = unicode(plainText, charset, 'replace')

	    # stop word list
	    stopWords = retriever.StopWords()

	    # tokenizer
	    tokenizer = analyser.Tokenizer()

	    # set language to English
	    language = 'english'

	    # get appropriate stop word list for language
	    stopWordList = stopWords.getStopWordList(language)

	    # tokenize, get paragraphs
	    tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 0))

	    # get token count
	    tokenCount = len(tokenizedCorpus)

	    # analyse sentence structure
	    sentenceStructure = analyser.SentenceStructure()

	    # get keywords
	    keywords = list(sentenceStructure.augmentKeywordsFromSentence(stopWordList, tokenizedCorpus))

	    # build return dictionary
	    returnDict = dict(corpus = corpus,
			      error = error,
			      errorMessage = errorMessage,
			      languageTitle = language.title(),
			      languages = languages,
			      charset = charset,
			      keywords = keywords,
			      fallback = fallback,
			      debug = 0)

	# if error
	else:
	    # set corpus to empty value
	    corpus = ''

	    # build return dictionary
	    returnDict = dict(corpus = corpus,
			      error = error,
			      errorMessage = errorMessage,
			      fallback = fallback,
			      debug = 1)

	# return values
	return returnDict

    @turbogears.expose(template='topicalizer.templates.processCoOccurrences', format='xhtml', content_type='text/html')
    def processCoOccurrences(self, plainText = '', language = 'automatic', textCategory = 'a', **kw):
	import retriever, analyser, re, urllib
	from operator import itemgetter
	from reverend.thomas import Bayes

	# initialise charset
	charset = ''

	# initialise corpus
	corpus = ''

	# initialise language list
	languages = self.languages

	# initialise text categories dictionary
	textCategories = self.textCategories

	# get text category title
	textCategoryTitleDisplay = textCategories[textCategory]

	# initialise error string
	error = 0
	errorMessage = ''

	# initialise fallback status
	fallback = 0

	# if text
	if plainText != '':
	    # decode text
	    plainText = urllib.unquote(plainText)

	    # codify corpus
	    charset = 'utf-8'
	    corpus = unicode(plainText, charset, 'replace')

	    # stop word list
	    stopWords = retriever.StopWords()

	    # tokenizer
	    tokenizer = analyser.Tokenizer()

	    # set language to English
	    language = 'english'

	    # get appropriate stop word list for language
	    stopWordList = stopWords.getStopWordList(language)

	    # tokenize, get paragraphs
	    tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 0))

	    # get token count
	    tokenCount = len(tokenizedCorpus)

	    # analyse sentence structure
	    sentenceStructure = analyser.SentenceStructure()

	    # get keywords
	    keywords = list(sentenceStructure.getCoOccurrencesFromDB(stopWordList, tokenizedCorpus, textCategory))

	    # build return dictionary
	    returnDict = dict(corpus = corpus,
			      error = error,
			      errorMessage = errorMessage,
			      languageTitle = language.title(),
			      languages = languages,
			      textCategories = sorted(textCategories.iteritems(), key = itemgetter(0), reverse = False),
			      textCategoryTitleDisplay = textCategoryTitleDisplay,
			      textCategory = textCategory,
			      charset = charset,
			      keywords = keywords,
			      fallback = fallback,
			      debug = 0)

	# if error
	else:
	    # set corpus to empty value
	    corpus = ''

	    # build return dictionary
	    returnDict = dict(corpus = corpus,
			      error = error,
			      errorMessage = errorMessage,
			      fallback = fallback,
			      debug = 1)

	# return values
	return returnDict

    @turbogears.expose(template='topicalizer.templates.getSimilarDocuments', format='xhtml', content_type='text/html')
    def getSimilarDocuments(self, url = '', plainText = '', language = 'automatic', **kw):
	import retriever, analyser, re, urllib, smtplib, google
	from email.MIMEText import MIMEText
	from operator import itemgetter
	from reverend.thomas import Bayes

	# initialise charset
	charset = ''

	# initialise corpus
	corpus = ''

	# initialise query string
	query = ''

	# Google licence key
	google.LICENSE_KEY = 'u1fm6zpQFHIyfhWM7XT3lz/dUJjl97NV'

	# initialise language list
	languages = self.languages

	# initialise error string
	error = 0
	errorMessage = ''

	# initialise fallback status
	fallback = 0

	# if URL
	if url != 'Enter URL' and url != '':
	    # decode url
	    url = urllib.unquote(url)

	    # instantiate URL retriever class
	    urlRetriever = retriever.URLRetriever()

	    # try retrieval of URL
	    try:
		corpusSet = urlRetriever.retrieveURL(url)
		corpus = corpusSet['corpus']
		charset = corpusSet['charset']
	    except IOError:
		error = 1
		errorMessage = 'URL could not be retrieved'

	# if text
	elif plainText != '':
	    # decode text
	    plainText = urllib.unquote(plainText)

	    # set URL for display
	    url = 'text'

	    # codify corpus
	    charset = 'utf-8'
	    corpus = unicode(plainText, charset, 'replace')

	# if retrieval was successful
	if error != 1:
	    # ML tag stripper
	    mlStripper = retriever.MLStripper()

	    # try removing ML tags
	    try:
		mlStripper.feed(corpus)
		corpus = mlStripper.getStripped()
	    except:
		# handle tags with fallback method
		mlFallback = retriever.MLFallback()
		corpus = mlFallback.getStripped(corpus)
		fallback = 1

		# dispatch an e-mail
		msg = MIMEText('The URL' + url + 'could not be parsed, using fallback instead.')
		msg['Subject'] = 'URL could not be parsed:' + url
		msg['From'] = 'webmaster@topicalizer.com'
		msg['To'] = 'bjoern@topicalizer.com'

		# send via SMTP
		s = smtplib.SMTP()

		# try to connect
	        try:
	            s.connect()
	            s.sendmail(msg['From'], msg['To'], msg.as_string())
	            s.close()
		except:
		    pass

	    # stop word list
	    stopWords = retriever.StopWords()

	    # tokenizer
	    tokenizer = analyser.Tokenizer()

	    # if language is set to 'automatic', try to guess language by Bayesian classification
	    if language == 'automatic':
		# instantiate guesser
		guesser = Bayes()

		# go through language in order to train guesser
		for selectLanguage in languages:
		    if selectLanguage != 'automatic':
			stopWordString = stopWords.getStopWordString(selectLanguage)
			guesser.train(selectLanguage, stopWordString)
			
		# get list of possible languages
		languageGuesses = guesser.guess(corpus)

		# get most probable language
		try:
		    language = languageGuesses.pop(0)[0]
		except IndexError:
		    language = 'english'

	    # get appropriate stop word list for language
	    stopWordList = stopWords.getStopWordList(language)

	    # tokenize, get paragraphs
	    if language == 'german':
		tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 1))
	    else:
		tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 0))

	    # get token count
	    tokenCount = len(tokenizedCorpus)

	    # analyse text structure
	    textStructure = analyser.TextStructure()

	    # get N-grams
	    ngrams = textStructure.getNGrams(tokenizedCorpus, tokenCount)
	    mostFrequentUnigrams = ngrams['mostFrequentUnigrams']
	    mostFrequentBigrams = ngrams['mostFrequentBigrams']
	    mostFrequentTrigrams = ngrams['mostFrequentTrigrams']
	    mostFrequentBigramsWithStopWords = ngrams['mostFrequentBigramsWithStopWords']
	    mostFrequentTrigramsWithStopWords = ngrams['mostFrequentTrigramsWithStopWords']

	    # get keywords
	    keywords = list(textStructure.getKeywords(mostFrequentUnigrams, mostFrequentBigrams, mostFrequentTrigrams, mostFrequentBigramsWithStopWords, mostFrequentTrigramsWithStopWords))

	    # build string for Google query
	    for unigram in sorted(mostFrequentUnigrams.iteritems(), key = itemgetter(1), reverse = True)[0:5]:
		query += unigram[0] + ' '

	    # query Google
	    try:
		data = google.doGoogleSearch(query)
		similarDocuments = data.results
	    except:
		if url != 'text':
		    url = '/getSimilarDocuments/?url=' + url
		else:
		    url = '/getSimilarDocuments/?plainText=' + plainText
		similarDocuments = []
		error = 1
		errorMessage = 'Sorry, an occured during this request, please try again'

	    # build return dictionary
	    returnDict = dict(corpus = corpus,
			      error = error,
			      errorMessage = errorMessage,
			      languages = languages,
			      similarDocuments = similarDocuments,
			      fallback = fallback,
			      debug = 0,
			      url = unicode(url, 'utf-8', 'replace'))

	# if URL retrieval error
	else:
	    # set corpus to empty value
	    corpus = ''

	    # build return dictionary
	    returnDict = dict(corpus = corpus,
			      error = error,
			      errorMessage = errorMessage,
			      languages = languages,
			      fallback = fallback,
			      debug = 1,
			      url = unicode(url, 'utf-8', 'replace'))

	# return values
	return returnDict

    @turbogears.expose(template='topicalizer.templates.process', format='xhtml', content_type='text/html')
    def process(self, url = '', plainText = '', language = 'automatic', **kw):
	import retriever, analyser, re, urllib, smtplib
	from email.MIMEText import MIMEText
	from operator import itemgetter
	from reverend.thomas import Bayes

	# initialise charset
	charset = ''

	# initialise corpus
	corpus = ''

	# initialise query string
	query = ''

	# initialise language list
	languages = self.languages

	# initialise error string
	error = 0
	errorMessage = ''

	# initialise fallback status
	fallback = 0

	# if URL
	if url != 'Enter URL' and url != '':
	    # decode url
	    url = urllib.unquote(url)

	    # instantiate URL retriever class
	    urlRetriever = retriever.URLRetriever()

	    # try retrieval of URL
	    try:
		corpusSet = urlRetriever.retrieveURL(url)
		corpus = corpusSet['corpus']
		charset = corpusSet['charset']
	    except IOError:
	    	error = 1
	    	errorMessage = 'URL could not be retrieved'

	# if text
	elif plainText != '':
	    # set URL for display
	    url = 'text'

	    # codify corpus
	    charset = 'utf-8'
	    corpus = unicode(plainText, charset, 'replace')

	# if retrieval was successful
	if error != 1:
	    # ML tag stripper
	    mlStripper = retriever.MLStripper()

	    # try removing ML tags
	    try:
		mlStripper.feed(corpus)
		corpus = mlStripper.getStripped()
	    except:
		# handle tags with fallback method
		mlFallback = retriever.MLFallback()
		corpus = mlFallback.getStripped(corpus)
		fallback = 1

		# dispatch an e-mail
		msg = MIMEText('The URL' + url + 'could not be parsed, using fallback instead.')
		msg['Subject'] = 'URL could not be parsed:' + url
		msg['From'] = 'webmaster@topicalizer.com'
		msg['To'] = 'bjoern@topicalizer.com'

		# send via SMTP
		s = smtplib.SMTP()

		# try to connect
	        try:
	            s.connect()
	            s.sendmail(msg['From'], msg['To'], msg.as_string())
	            s.close()
		except:
		    pass

	    # stop word list
	    stopWords = retriever.StopWords()

	    # tokenizer
	    tokenizer = analyser.Tokenizer()

	    # analyse word structure
	    wordStructure = analyser.WordStructure()

	    # if language is set to 'automatic', try to guess language by Bayesian classification
	    if language == 'automatic':
		# instantiate guesser
		guesser = Bayes()

		# go through language in order to train guesser
		for selectLanguage in languages:
		    if selectLanguage != 'automatic':
			stopWordString = stopWords.getStopWordString(selectLanguage)
			guesser.train(selectLanguage, stopWordString)
			
		# get list of possible languages
		languageGuesses = guesser.guess(corpus)

		# get most probable language
		try:
		    language = languageGuesses.pop(0)[0]
		except IndexError:
		    language = 'english'

	    # get appropriate stop word list for language
	    stopWordList = stopWords.getStopWordList(language)

	    # tokenize, get paragraphs
	    if language == 'german':
		tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 1))
	    else:
		tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 0))
	    paragraphs = list(tokenizer.processParagraphs(corpus))

	    # get types, characters, sentences
	    typesCharactersSentences = wordStructure.getTypesCharactersSentences(tokenizedCorpus)
	    types = list(typesCharactersSentences['types'])
	    sentences = list(typesCharactersSentences['sentences'])
	    sentenceStrings = list(typesCharactersSentences['sentenceStrings'])
	    charactersPerToken = list(typesCharactersSentences['charactersPerToken'])
	    maxSentenceLength = typesCharactersSentences['maxSentenceLength']
	    minSentenceLength = typesCharactersSentences['minSentenceLength']
	    maxTokenLength = typesCharactersSentences['maxTokenLength']
	    minTokenLength = typesCharactersSentences['minTokenLength']
	    maxSentence = typesCharactersSentences['maxSentence']
	    minSentence = typesCharactersSentences['minSentence']
	    maxToken = typesCharactersSentences['maxToken']
	    minToken = typesCharactersSentences['minToken']
	    sumOfCharacters = typesCharactersSentences['sumOfCharacters']

	    # calculate some average values
	    paragraphCount = len(paragraphs)
	    tokenCount = len(tokenizedCorpus)
	    typeCount = len(types)
	    sentenceCount = len(sentences)

	    # if token count is not 0
	    if tokenCount != 0:
		lexicalDensity = round(typeCount / tokenCount, 2)
		averageCharactersPerWord = round(sumOfCharacters / tokenCount, 2)
	    else:
		lexicalDensity = 0
		averageCharactersPerWord = 0

	    # if sentence count is not 0
	    if sentenceCount != 0:
		averageTokensPerSentence = round(tokenCount / sentenceCount, 2)
		averageTokensPerParagraph = round(tokenCount / paragraphCount, 2)
	    else:
		averageTokensPerSentence = 0
		averageTokensPerParagraph = 0

	    # if paragraph count is not 0
	    if paragraphCount != 0:
		averageSentencesPerParagraph = round(sentenceCount / paragraphCount, 2)
	    else:
		averageSentencesPerParagraph = 0

	    # syllables
	    syllableInformation = wordStructure.getSyllableInformation(tokenizedCorpus, types)
	    totalSyllables = syllableInformation['sum']
	    syllablesPerToken = syllableInformation['syllablesPerToken']
	    syllablesPerType = syllableInformation['syllablesPerType']

	    # if token count is not 0
	    if tokenCount != 0:
		averageSyllablesPerWord = round(totalSyllables / tokenCount, 2)
	    else:
		averageSyllablesPerWord = 0

	    # analyse text structure
	    textStructure = analyser.TextStructure()

	    # get N-grams
	    ngrams = textStructure.getNGrams(tokenizedCorpus, tokenCount)
	    mostFrequentUnigrams = ngrams['mostFrequentUnigrams']
	    mostFrequentUnigramsAbstract = ngrams['mostFrequentUnigramsAbstract']
	    mostFrequentBigrams = ngrams['mostFrequentBigrams']
	    mostFrequentTrigrams = ngrams['mostFrequentTrigrams']
	    mostFrequentBigramsWithStopWords = ngrams['mostFrequentBigramsWithStopWords']
	    mostFrequentTrigramsWithStopWords = ngrams['mostFrequentTrigramsWithStopWords']

	    # get keywords
	    keywords = list(textStructure.getKeywords(mostFrequentUnigrams, mostFrequentBigrams, mostFrequentTrigrams, mostFrequentBigramsWithStopWords, mostFrequentTrigramsWithStopWords))

	    # build string for Google query
	    for unigram in sorted(mostFrequentUnigrams.iteritems(), key = itemgetter(1), reverse = True)[0:5]:
		query += unigram[0] + ' '

	    # get abstract
	    abstract = textStructure.getAbstract(mostFrequentUnigramsAbstract, sentenceStrings)

	    # if token count is 0
	    if tokenCount == 0:
		readabilityGF = 0
		readabilityCL = 0
	    else:
		# readability according to Gunning-Fog Index
		readabilityGF = textStructure.analyseReadabilityGF(averageTokensPerSentence, syllablesPerType, tokenCount)

		# readability according to Coleman-Liau Index
		readabilityCL = textStructure.analyseReadabilityCL(averageCharactersPerWord, sentenceCount, tokenCount)

	    # readability according to Automated Readability Index
	    readabilityAR = textStructure.analyseReadabilityAR(averageCharactersPerWord, averageTokensPerSentence)

	    # average readability
	    readabilityAverage = round((readabilityGF + readabilityAR + readabilityCL) / 3, 2)

	    # build return dictionary
	    returnDict = dict(corpus = corpus,
			      languageTitle = language.title(),
			      languages = languages,
			      stopWordList = stopWordList,
			      error = error,
			      errorMessage = errorMessage,
			      charset = charset,
			      paragraphCount = paragraphCount,
			      sentenceCount = sentenceCount,
			      tokenCount = tokenCount,
			      typeCount = typeCount,
			      lexicalDensity = lexicalDensity,
			      averageCharactersPerWord = averageCharactersPerWord,
			      averageSyllablesPerWord = averageSyllablesPerWord,
			      mostFrequentUnigrams = sorted(mostFrequentUnigrams.iteritems(), key = itemgetter(1), reverse = True),
			      mostFrequentBigrams = sorted(mostFrequentBigrams.iteritems(), key = itemgetter(1), reverse = True),
			      mostFrequentTrigrams = sorted(mostFrequentTrigrams.iteritems(), key = itemgetter(1), reverse = True),
			      mostFrequentBigramsWithStopWords = sorted(mostFrequentBigramsWithStopWords.iteritems(), key = itemgetter(1), reverse = True),
			      mostFrequentTrigramsWithStopWords = sorted(mostFrequentTrigramsWithStopWords.iteritems(), key = itemgetter(1), reverse = True),
			      keywords = keywords,
			      abstract = sorted(abstract.iteritems(), key = itemgetter(1), reverse = True)[0:5],
			      readabilityGF = readabilityGF,
			      readabilityAR = readabilityAR,
			      readabilityCL = readabilityCL,
			      readabilityAverage = readabilityAverage,
			      averageTokensPerSentence = averageTokensPerSentence,
			      averageTokensPerParagraph = averageTokensPerParagraph,
			      averageSentencesPerParagraph = averageSentencesPerParagraph,
			      maxSentenceLength = maxSentenceLength,
			      minSentenceLength = minSentenceLength,
			      maxTokenLength = maxTokenLength,
			      minTokenLength = minTokenLength,
			      maxSentence = maxSentence,
			      minSentence = minSentence,
			      maxToken = maxToken,
			      minToken = minToken,
			      query = query,
			      fallback = fallback,
			      debug = 0,
			      url = unicode(url, 'utf-8', 'replace'))

	# if URL retrieval error
	else:
	    # set corpus to empty value
	    corpus = ''

	    # build return dictionary
	    returnDict = dict(corpus = corpus,
			      languages = languages,
			      error = error,
			      errorMessage = errorMessage,
			      fallback = fallback,
			      debug = 1,
			      url = unicode(url, 'utf-8', 'replace'))

	# return values
	return returnDict

    @turbogears.expose(template='topicalizer.templates.buildSemanticWeb', format='xhtml', content_type='text/html')
    def buildSemanticWeb(self, documentsByCategories = '', language= 'automatic', **kw):
	import retriever, analyser, re, urllib, smtplib
	from email.MIMEText import MIMEText
	from operator import itemgetter
	from reverend.thomas import Bayes

	# initialise charset
	charset = ''

	# initialise corpus
	corpus = ''

	# initialise query string
	query = ''

	# initialise language list
	languages = self.languages

	# initialise error string
	error = 0
	errorMessage = ''

	# initialise fallback status
	fallback = 0

	# initialise list for keywords which are to be deleted
	keywordsToBeDeleted = []

	# initialise keyword dictionaries
	keywordsByDocument = {}
	keywordsByCategory = {}
	keywordsComplete = {}
	categoryKeywords = {}
	keyKeywords = {}
	keywordBelongsTo = {}

	# initialise URL list
	urlList = []

	# initialise token count dictionaries
	tokenCountByDocument = {}
	tokenCountByCategory = {}
	tokenCountComplete = 0

	# initialise categories and documents for testing purposes
	mainCategory = ['http://en.wikipedia.org/wiki/Mathematics']
	subCategory = ['http://en.wikipedia.org/wiki/Differential_equations', 'http://en.wikipedia.org/wiki/Functional_analysis', 'http://en.wikipedia.org/wiki/Algebraic_geometry', 'http://en.wikipedia.org/wiki/Mathematical_beauty', 'http://en.wikipedia.org/wiki/Natural_number']
	subSubCategory = ['http://en.wikipedia.org/wiki/Hilbert_space', 'http://en.wikipedia.org/wiki/Topological_vector_space', 'http://en.wikipedia.org/wiki/Normed_vector_space', 'http://en.wikipedia.org/wiki/Banach_space']
	documentsByCategories = {'1': mainCategory, '2': subCategory, '3': subSubCategory}

	# instantiate URL retriever class
	urlRetriever = retriever.URLRetriever()

	# get each category
	for categoryTitle, categoryContent in documentsByCategories.iteritems():
	    # get each url
	    for url in categoryContent:
		# write URL to list
		urlList.append(unicode(url, 'utf-8', 'replace'))

		# reset type and token counts
		tokenCount = 0
		typeCount = 0

		# decode url
		url = urllib.unquote(url)

		# try retrieval of URL
		try:
		    error = 0
		    corpusSet = urlRetriever.retrieveURL(url)
		    corpus = corpusSet['corpus']
		    charset = corpusSet['charset']
		except IOError:
		    error = 1
		    errorMessage = 'URL could not be retrieved'

		# if retrieval was successful
		if error != 1:
		    # ML tag stripper
		    mlStripper = retriever.MLStripper()

		    # try removing ML tags
		    try:
			mlStripper.feed(corpus)
			corpus = mlStripper.getStripped()
		    except:
			# handle tags with fallback method
			mlFallback = retriever.MLFallback()
			corpus = mlFallback.getStripped(corpus)
			fallback = 1

			# dispatch an e-mail
			msg = MIMEText('The URL' + url + 'could not be parsed, using fallback instead.')
			msg['Subject'] = 'URL could not be parsed:' + url
			msg['From'] = 'webmaster@topicalizer.com'
			msg['To'] = 'bjoern@topicalizer.com'

			# send via SMTP
			s = smtplib.SMTP()

			# try to connect
			try:
			    s.connect()
			    s.sendmail(msg['From'], msg['To'], msg.as_string())
			    s.close()
			except:
			    pass

		    # stop word list
		    stopWords = retriever.StopWords()

		    # tokenizer
		    tokenizer = analyser.Tokenizer()

		    # analyse word structure
		    wordStructure = analyser.WordStructure()

		    # if language is set to 'automatic', try to guess language by Bayesian classification
		    if language == 'automatic':
			# instantiate guesser
			guesser = Bayes()

			# go through language in order to train guesser
			for selectLanguage in languages:
			    if selectLanguage != 'automatic':
				stopWordString = stopWords.getStopWordString(selectLanguage)
				guesser.train(selectLanguage, stopWordString)
			
			# get list of possible languages
			languageGuesses = guesser.guess(corpus)

			# get most probable language
			try:
			    language = languageGuesses.pop(0)[0]
			except IndexError:
			    language = 'english'

		    # get appropriate stop word list for language
		    stopWordList = stopWords.getStopWordList(language)

		    # tokenize
		    if language == 'german':
			tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 1))
		    else:
			tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 0))

		    # get types
		    typesCharactersSentences = wordStructure.getTypesCharactersSentences(tokenizedCorpus)
		    types = list(typesCharactersSentences['types'])

		    # calculate some average values
		    tokenCount = len(tokenizedCorpus)
		    typeCount = len(types)

		    # analyse text structure
		    textStructure = analyser.TextStructure()

		    # get N-grams
		    ngrams = textStructure.getNGrams(tokenizedCorpus, tokenCount)
		    mostFrequentUnigrams = ngrams['mostFrequentUnigrams']
		    mostFrequentUnigramsAbstract = ngrams['mostFrequentUnigramsAbstract']
		    mostFrequentBigrams = ngrams['mostFrequentBigrams']
		    mostFrequentTrigrams = ngrams['mostFrequentTrigrams']
		    mostFrequentBigramsWithStopWords = ngrams['mostFrequentBigramsWithStopWords']
		    mostFrequentTrigramsWithStopWords = ngrams['mostFrequentTrigramsWithStopWords']

		    # get keywords
		    keywords = textStructure.getKeywordsWithFrequencies(mostFrequentUnigrams, mostFrequentBigrams, mostFrequentTrigrams, mostFrequentBigramsWithStopWords, mostFrequentTrigramsWithStopWords)

		    # write token count to dictionaries
		    tokenCountByDocument[url] = tokenCount
		    tokenCountByCategory[categoryTitle] = tokenCountByCategory.get(categoryTitle, tokenCount) + tokenCount
		    tokenCountComplete += tokenCount

		    # write keywords to dictionaries
		    keywordsByDocument[url] = keywords
		    categoryKeywords = keywordsByCategory.get(categoryTitle, {})
		    for keyword, keywordValue in keywords.iteritems():
			categoryKeywords[keyword] = keywordsByCategory.get(keyword, keywordValue) + keywordValue
			keywordsComplete[keyword] = keywordsComplete.get(keyword, keywordValue) + keywordValue
		    keywordsByCategory[categoryTitle] = categoryKeywords 

		# if URL retrieval error
		else:
		    # set corpus to empty value
		    corpus = ''

	# remove keywords which are proportionately less frequent than in the whole corpus
	for url, keywords in keywordsByDocument.iteritems():
	    # reset list for keywords to be deleted
	    keywordsToBeDeleted = []

	    # go through keywords
	    for keyword, keywordValue in keywords.iteritems():
		# mark keywords to be deleted, if proportionately less frequent than in the whole corpus
		if (keywordValue / tokenCountByDocument[url]) <= (keywordsComplete[keyword] / tokenCountComplete):
		    keywordsToBeDeleted.append(keyword)

	    # delete
	    for deleteThis in keywordsToBeDeleted:
		del keywords[deleteThis]

	    # write buffer
	    keywordsByDocument[url] = keywords

	# go through all keyword
	for keyword in keywordsComplete:
	    # initialise dictionary for key keywords for this keyword
	    thisKeyKeywords = {}

	    # go through document
	    for url, keywordsInDocument in keywordsByDocument.iteritems():
		# if is keyword for this docment
		if keyword in keywordsInDocument:
		    # go through key keywords
		    for keyKeyword in keywordsInDocument:
			# assign key keyword as being related to keyword
			thisKeyKeywords[keyKeyword] = thisKeyKeywords.get(keyKeyword, 0) + 1

	    # get category for keywords
	    keywordsByCategory1 = keywordsByCategory['1']
	    keywordsByCategory2 = keywordsByCategory['2']
	    keywordsByCategory3 = keywordsByCategory['3']
	    if keyword in keywordsByCategory1 and keyword in keywordsByCategory2:
		if (keywordsByCategory1[keyword] / tokenCountByCategory['1']) >= (keywordsByCategory2[keyword] / tokenCountByCategory['2']):
		    keywordBelongsTo[keyword] = '1'
	    elif keyword in keywordsByCategory1:
		keywordBelongsTo[keyword] = '1'
	    elif keyword in keywordsByCategory2:
		keywordBelongsTo[keyword] = '2'
	    if keyword in keywordsByCategory2 and keyword in keywordsByCategory3:
		if (keywordsByCategory2[keyword] / tokenCountByCategory['2']) >= (keywordsByCategory3[keyword] / tokenCountByCategory['3']):
		    keywordBelongsTo[keyword] = '2'
		else:
		    keywordBelongsTo[keyword] = '3'
	    elif keyword in keywordsByCategory2:
		keywordBelongsTo[keyword] = '2'
	    elif keyword in keywordsByCategory3:
		keywordBelongsTo[keyword] = '3'

	    # assign related key keywords
	    keyKeywords[keyword] = sorted(thisKeyKeywords.iteritems(), key = itemgetter(1), reverse = True)

	# build return dictionary
	returnDict = dict(corpus = corpus,
			  languageTitle = language.title(),
			  languages = languages,
			  stopWordList = stopWordList,
			  error = error,
			  errorMessage = errorMessage,
			  keywordsByDocument = sorted(keywordsByDocument.iteritems(), key = itemgetter(1), reverse = True),
			  keywordsByCategory = sorted(keywordsByCategory.iteritems(), key = itemgetter(1), reverse = True),
			  keywordsComplete = sorted(keywordsComplete.iteritems(), key = itemgetter(1), reverse = True),
			  keyKeywords = keyKeywords,
			  tokenCountByDocument = tokenCountByDocument,
			  tokenCountByCategory = tokenCountByCategory,
			  tokenCountComplete = tokenCountComplete,
			  keywordBelongsTo = keywordBelongsTo,
			  fallback = fallback,
			  debug = 0,
			  urlList = urlList)
		    
	# return values
	return returnDict

    @turbogears.expose(template='topicalizer.templates.classify', format='xhtml', content_type='text/html')
    def classify(self):
        import time

	# initialise language list
	languages = self.languages

        return dict(now=time.ctime(),
		    languages = languages)

    @turbogears.expose(template='topicalizer.templates.processClassify', format='xml', content_type='text/xml')
    def processClassify(self, plainText1 = '', plainText2 = '', plainText3 = '', language = 'automatic', **kw):
	import retriever
	from reverend.thomas import Bayes

	# initialise charset
	charset = ''

	# initialise corpora
	corpus1 = ''
	corpus2 = ''
	corpus3 = ''

	# initialise success flag
	success = 0

	# initialise category guess
	categoryGuess = []

	# initialise category
	category = ''

	# initialise probability
	categoryProbability = 0

	# initialise language list
	languages = self.languages

	# stop word list
	stopWords = retriever.StopWords()

	# codify corpora
	charset = 'utf-8'
	corpus1 = unicode(plainText1, charset, 'replace')
	corpus2 = unicode(plainText2, charset, 'replace')
	corpus3 = unicode(plainText3, charset, 'replace')

	# instantiate guessers
	languageGuesser = Bayes()
	categoryGuesser = Bayes()

	# go through language in order to train guesser
	for selectLanguage in languages:
	    if selectLanguage != 'automatic':
		stopWordString = stopWords.getStopWordString(selectLanguage)
		languageGuesser.train(selectLanguage, stopWordString)
			
	# get list of possible languages
	languageGuesses = languageGuesser.guess(corpus1 + corpus2 + corpus3)

	# get most probable language
	try:
	    language = languageGuesses.pop(0)[0]
	except IndexError:
	    language = 'english'

	# train category guesser with first corpus
	categoryGuesser.train('first reference text', corpus1)
	categoryGuesser.train('second reference text', corpus2)

	# compare with second corpus
	categoryGuesses = categoryGuesser.guess(corpus3)

	# get probability
	try:
	    categoryGuess = categoryGuesses.pop(0)
	    category = categoryGuess[0]
	    categoryProbability = categoryGuess[1]
	    success = 1
	except IndexError:
	    category = ''
	    categoryProbabilty = 0
	    success = 0

	# build return dictionary
	returnDict = dict(languages = languages,
			  languageTitle = language.title(),
			  charset = charset,
			  success = success,
			  category = category,
			  categoryProbability = categoryProbability)

	# return values
	return returnDict
