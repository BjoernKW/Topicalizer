from __future__ import division
from turbogears import controllers, expose, flash

# from model import *
import logging
log = logging.getLogger("topicalizer.controllers")

class Root(controllers.Root):
    # constructor
    def __init__(self):
        # initialise language list
        self.languages = ['automatic',
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
        self.textCategories = dict(a = 'Press: Reportage',
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
        # Google license key
        self.googleLicenseKey = 'u1fm6zpQFHIyfhWM7XT3lz/dUJjl97NV'

    @expose(template='topicalizer.templates.welcome', format='xhtml', content_type='text/html')
    def index(self):
        import time

    	# log.debug("Happy TurboGears Controller Responding For Duty")

        return dict(now=time.ctime(),
                    languages = self.languages)

    @expose(template='topicalizer.templates.augmentKeywords', format='xhtml', content_type='text/html')
    def augmentKeywords(self):
        import time

        return dict(now=time.ctime(),
                    languages = self.languages)

    @expose(template='topicalizer.templates.coOccurrences', format='xhtml', content_type='text/html')
    def coOccurrences(self):
        import time
        from operator import itemgetter
    
    	# initialise text categories dictionary
    	textCategories = self.textCategories

        return dict(now=time.ctime(),
                    languages = self.languages,
                    textCategories = sorted(textCategories.iteritems(), key = itemgetter(0), reverse = False))

    @expose(template='topicalizer.templates.similarDocuments', format='xhtml', content_type='text/html')
    def similarDocuments(self):
        import time

        return dict(now=time.ctime(),
                    languages = self.languages)

    @expose(template='topicalizer.templates.about', format='xhtml', content_type='text/html')
    def about(self):
        import time
        return dict(now=time.ctime())

    @expose(template='topicalizer.templates.faq', format='xhtml', content_type='text/html')
    def faq(self):
        import time
        return dict(now=time.ctime())

    @expose(template='topicalizer.templates.links', format='xhtml', content_type='text/html')
    def links(self):
        import time
        return dict(now=time.ctime())

    @expose(template='topicalizer.templates.api', format='xhtml', content_type='text/html')
    def api(self):
        from operator import itemgetter
    
    	# initialise text categories dictionary
    	textCategories = self.textCategories

        return dict(languages = self.languages,
                    textCategories = sorted(textCategories.iteritems(), key = itemgetter(0), reverse = False))

    @expose(template='topicalizer.templates.tools', format='xhtml', content_type='text/html')
    def tools(self):
        import time
        return dict(now=time.ctime())

    @expose(template='topicalizer.templates.terms', format='xhtml', content_type='text/html')
    def terms(self):
        import time
        return dict(now=time.ctime())

    @expose(template='topicalizer.templates.contact', format='xhtml', content_type='text/html')
    def contact(self):
        import time
        return dict(now=time.ctime())

    @expose(template='topicalizer.templates.disclaimer', format='xhtml', content_type='text/html')
    def disclaimer(self):
        import time
        return dict(now=time.ctime())

    @expose(template='topicalizer.templates.getCompleteAnalysis', format='xml', content_type='text/xml')
    def getCompleteAnalysis(self, url = '', plainText = '', language = 'automatic', **kw):
    	from core import producer

        # create analysis producer
        analysis = producer.Analysis()
        
        return analysis.createAnalysis(url, plainText, language, self.languages)

    @expose(template='topicalizer.templates.getKeywords', format='xml', content_type='text/xml')
    def getKeywords(self, url = '', plainText = '', language = 'automatic', **kw):
        from core import helper, analyser
        from operator import itemgetter
    
    	# initialise error string
    	error = 0
    	errorMessage = ''
        
        # get corpus
        corpusHelper = helper.CorpusHelper()
        corpusInfo = corpusHelper.getCorpus(url, plainText)
        error = corpusInfo['error']
        errorMessage = corpusInfo['errorMessage']
        corpus = corpusInfo['corpus']
        charset = corpusInfo['charset']
    
    	# if retrieval was successful
    	if error != 1:
            # tokenizer
            tokenizer = analyser.Tokenizer()

            # initialise corpus helper
            corpusHelper = helper.CorpusHelper()
            
            # get tokenized corpus
            corpusInfo = corpusHelper.getTokenizedCorpus(tokenizer, corpus, language, self.languages)
            tokenizedCorpus = corpusInfo['tokenizedCorpus']

    	    # get token count
    	    tokenCount = len(tokenizedCorpus)
    
    	    # analyse text structure
    	    textStructure = analyser.TextStructure()
    
    	    # get N-grams
    	    ngrams = textStructure.getNGrams(tokenizedCorpus, tokenCount)
    	    mostFrequentUnigrams = ngrams['mostFrequentUnigrams']
    	    mostFrequentUnigramsAll = ngrams['mostFrequentUnigramsAll']
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
            			      mostFrequentUnigramsAll = sorted(mostFrequentUnigramsAll.iteritems(), key = itemgetter(1), reverse = True),
            			      keywords = keywords,
            			      debug = 0)
    
    	# if URL retrieval error
    	else:
    	    # build return dictionary
    	    returnDict = dict(error = error,
            			      errorMessage = errorMessage,
            			      debug = 1,
            			      url = url)
    
    	# return values
    	return returnDict

    @expose(template='topicalizer.templates.getCoOccurrences', format='xml', content_type='text/xml')
    def getCoOccurrences(self, plainText = '', language = 'english', textCategory = 'a', **kw):
        from core import analyser, retriever, helper
    
    	# initialise error string
    	error = 0
    	errorMessage = ''

    	# if text
    	if plainText != '':
            # stop word list
            stopWords = retriever.StopWords()

            # get appropriate stop word list for language
            stopWordList = stopWords.getStopWordList(language)

            # initialise corpus helper
            corpusHelper = helper.CorpusHelper()
            
            # get tokenized corpus
            tokenizedCorpus = corpusHelper.getTokenizedPlainTextCorpus(plainText, language, stopWordList)
    
    	    # analyse sentence structure
    	    sentenceStructure = analyser.SentenceStructure()
    
    	    # get keywords
    	    keywords = list(sentenceStructure.getCoOccurrencesFromDB(stopWordList, tokenizedCorpus, textCategory))
    
    	    # build return dictionary
    	    returnDict = dict(error = error,
            			      errorMessage = errorMessage,
            			      keywords = keywords,
            			      debug = 0)
    
    	# if error
    	else:
    	    # build return dictionary
    	    returnDict = dict(error = error,
            			      errorMessage = errorMessage,
            			      debug = 1)
    
    	# return values
    	return returnDict

    @expose(template='topicalizer.templates.getAugmentedKeywords', format='xml', content_type='text/xml')
    def getAugmentedKeywords(self, plainText = '', language = 'english', **kw):
    	from core import helper, analyser, retriever
    
    	# initialise error string
    	error = 0
    	errorMessage = ''
    
    	# if text
    	if plainText != '':
            # stop word list
            stopWords = retriever.StopWords()

            # get appropriate stop word list for language
            stopWordList = stopWords.getStopWordList(language)

            # initialise corpus helper
            corpusHelper = helper.CorpusHelper()
            
            # get tokenized corpus
            tokenizedCorpus = corpusHelper.getTokenizedPlainTextCorpus(plainText, language, stopWordList)
    
    	    # analyse sentence structure
    	    sentenceStructure = analyser.SentenceStructure()
    
    	    # get keywords
    	    keywords = list(sentenceStructure.augmentKeywordsFromSentence(stopWordList, tokenizedCorpus))
    
    	    # build return dictionary
    	    returnDict = dict(error = error,
            			      errorMessage = errorMessage,
            			      keywords = keywords,
            			      debug = 0)
    
    	# if error
    	else:
    	    # build return dictionary
    	    returnDict = dict(error = error,
            			      errorMessage = errorMessage,
            			      debug = 1)
    
    	# return values
    	return returnDict

    @expose(template='topicalizer.templates.processAugmentedKeywords', format='xhtml', content_type='text/html')
    def processAugmentedKeywords(self, plainText = '', language = 'english', **kw):
    	from core import helper, analyser, retriever
    
    	# initialise error string
    	error = 0
    	errorMessage = ''
    
    	# if text
    	if plainText != '':
            # stop word list
            stopWords = retriever.StopWords()

            # get appropriate stop word list for language
            stopWordList = stopWords.getStopWordList(language)

            # initialise corpus helper
            corpusHelper = helper.CorpusHelper()
            
            # get tokenized corpus
            tokenizedCorpus = corpusHelper.getTokenizedPlainTextCorpus(plainText, language, stopWordList)
    
    	    # analyse sentence structure
    	    sentenceStructure = analyser.SentenceStructure()
    
    	    # get keywords
    	    keywords = list(sentenceStructure.augmentKeywordsFromSentence(stopWordList, tokenizedCorpus))
    
    	    # build return dictionary
    	    returnDict = dict(corpus = plainText,
                              error = error,
            			      errorMessage = errorMessage,
            			      languageTitle = language.title(),
            			      languages = self.languages,
            			      keywords = keywords,
            			      debug = 0)
    
    	# if error
    	else:
    	    # build return dictionary
    	    returnDict = dict(languages = self.languages,
            			      error = error,
            			      errorMessage = errorMessage,
            			      debug = 1)
    
    	# return values
    	return returnDict

    @expose(template='topicalizer.templates.processCoOccurrences', format='xhtml', content_type='text/html')
    def processCoOccurrences(self, plainText = '', language = 'english', textCategory = 'a', **kw):
    	from core import helper, analyser, retriever
        from operator import itemgetter
    
    	# initialise text categories dictionary
    	textCategories = self.textCategories
    
    	# get text category title
    	textCategoryTitleDisplay = textCategories[textCategory]
    
    	# initialise error string
    	error = 0
    	errorMessage = ''
    
    	# if text
    	if plainText != '':
            # stop word list
            stopWords = retriever.StopWords()

            # get appropriate stop word list for language
            stopWordList = stopWords.getStopWordList(language)

            # initialise corpus helper
            corpusHelper = helper.CorpusHelper()
            
            # get tokenized corpus
            tokenizedCorpus = corpusHelper.getTokenizedPlainTextCorpus(plainText, language, stopWordList)
    
    	    # analyse sentence structure
    	    sentenceStructure = analyser.SentenceStructure()
    
    	    # get keywords
    	    keywords = list(sentenceStructure.getCoOccurrencesFromDB(stopWordList, tokenizedCorpus, textCategory))
    
    	    # build return dictionary
    	    returnDict = dict(corpus = plainText,
                              error = error,
            			      errorMessage = errorMessage,
            			      languageTitle = language.title(),
            			      languages = self.languages,
            			      textCategories = sorted(textCategories.iteritems(), key = itemgetter(0), reverse = False),
            			      textCategoryTitleDisplay = textCategoryTitleDisplay,
            			      textCategory = textCategory,
            			      keywords = keywords,
            			      debug = 0)
    
    	# if error
    	else:
    	    # build return dictionary
    	    returnDict = dict(languages = self.languages,
                              textCategories = sorted(textCategories.iteritems(), key = itemgetter(0), reverse = False),
            			      error = error,
            			      errorMessage = errorMessage,
            			      debug = 1)
    
    	# return values
    	return returnDict

    @expose(template='topicalizer.templates.getSimilarDocuments', format='xhtml', content_type='text/html')
    def getSimilarDocuments(self, url = '', plainText = '', language = 'automatic', **kw):
    	from core import analyser, helper
        import google
    
    	# Google licence key
    	google.LICENSE_KEY = self.googleLicenseKey
    
    	# initialise error string
    	error = 0
    	errorMessage = ''
    
        # get corpus
        corpusHelper = helper.CorpusHelper()
        corpusInfo = corpusHelper.getCorpus(url, plainText)
        error = corpusInfo['error']
        errorMessage = corpusInfo['errorMessage']
        corpus = corpusInfo['corpus']
        charset = corpusInfo['charset']
        url = corpusInfo['url']
    
    	# if retrieval was successful
    	if error != 1:
            # tokenizer
            tokenizer = analyser.Tokenizer()

            # initialise corpus helper
            corpusHelper = helper.CorpusHelper()
            
            # get tokenized corpus
            corpusInfo = corpusHelper.getTokenizedCorpus(tokenizer, corpus, language, self.languages)
            tokenizedCorpus = corpusInfo['tokenizedCorpus']
    
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
            googleHelper = helper.GoogleHelper()
            query = googleHelper.getGoogleQuery(mostFrequentUnigrams)
    
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
                errorMessage = 'Sorry, an error occured during this request, please try again'
    
    	    # build return dictionary
    	    returnDict = dict(error = error,
            			      errorMessage = errorMessage,
            			      languages = self.languages,
            			      similarDocuments = similarDocuments,
            			      debug = 0,
            			      url = url)
    
    	# if URL retrieval error
    	else:
    	    # build return dictionary
    	    returnDict = dict(error = error,
            			      errorMessage = errorMessage,
            			      languages = self.languages,
            			      debug = 1,
            			      url = url)
    
    	# return values
    	return returnDict

    @expose(template='topicalizer.templates.process', format='xhtml', content_type='text/html')
    def process(self, url = '', plainText = '', language = 'automatic', **kw):
        from core import producer

        # create analysis producer
        analysis = producer.Analysis()
        
        return analysis.createAnalysis(url, plainText, language, self.languages)

    @expose(template='topicalizer.templates.semWeb', format='xhtml', content_type='text/html')
    def semWeb(self):
        import time
    
        return dict(now=time.ctime(),
                    languages = self.languages)
    
    @expose(template='topicalizer.templates.processSemWeb', format='xhtml', content_type='text/html')
    def processSemWeb(self, term = '', language = 'automatic', **kw):
        from core import producer
        
        # create semantic web producer
        semanticWeb = producer.SemanticWeb()
        
    	return semanticWeb.createSemanticWeb(term, language, self.languages, self.googleLicenseKey)
    
    @expose(template='topicalizer.templates.getSemWeb', format='xml', content_type='text/xml')
    def getSemWeb(self, term = '', language = 'automatic', **kw):
        from core import producer
        
        # create semantic web producer
        semanticWeb = producer.SemanticWeb()

    	return semanticWeb.createSemanticWeb(term, language, self.languages, self.googleLicenseKey)
    
    @expose(template='topicalizer.templates.classify', format='xhtml', content_type='text/html')
    def classify(self):
        import time
    
        return dict(now=time.ctime(),
                    languages = self.languages)

    @expose(template='topicalizer.templates.processClassify', format='xml', content_type='text/xml')
    def processClassify(self, plainText1 = '', plainText2 = '', plainText3 = '', language = 'automatic', **kw):
    	from core import retriever, classifier
    
    	# initialise success flag
    	success = 0
    
    	# initialise category guess
    	categoryGuess = []
    
    	# initialise category
    	category = ''
    
    	# initialise probability
    	categoryProbability = 0
    
    	# stop word list
    	stopWords = retriever.StopWords()
    
    	# codifylanguageGuesser corpora
    	charset = 'us-ascii'
    	corpus1 = plainText1
    	corpus2 = plainText2
    	corpus3 = plainText3
        
        # initialise classifier
        classifier = classifier.BayesClassifier()

        # guess language
        language = classifier.guessLanguage(stopWords, corpus1 + corpus2 + corpus3, self.languages)

        # get guesses
        categoryGuesses = classifier.getCategoryGuesses(corpus1, corpus2, corpus3)
    
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
    	returnDict = dict(languages = self.languages,
            			  languageTitle = language.title(),
            			  charset = charset,
            			  success = success,
            			  category = category,
            			  categoryProbability = categoryProbability)
    
    	# return values
    	return returnDict
