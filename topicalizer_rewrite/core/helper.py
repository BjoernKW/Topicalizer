# helper class fo Google-related stuff
class GoogleHelper:
    # constructor
    def __init__(self):
        pass

    # get Google querx
    def getGoogleQuery(self, mostFrequentUnigrams = dict()):
        from operator import itemgetter

        # initialise query
        query = ''

        # build string for Google query
        for unigram in sorted(mostFrequentUnigrams.iteritems(), key = itemgetter(1), reverse = True)[0:5]:
            query += unigram[0] + ' '
            
        # return
        return query

# helper class for parser-related stuff
class ParserHelper:
    # constructor
    def __init__(self):
        pass
    
    # get plain text
    def getPlainText(self, corpus = ''):
        import parser
        
        # ML tag stripper
        mlStripper = parser.MLStripper()

        # try removing ML tags
        try:
            mlStripper.feed(corpus)
            corpus = mlStripper.getStripped()
        except:
            # handle tags with fallback method
            mlFallback = parser.MLFallback()
            corpus = mlFallback.getStripped(corpus)
        
        # return
        return corpus
    
    # get linked terms
    def getLinkedTerms(self, corpus = ''):
        import parser
        
        # link extractor
        linkExtractor = parser.LinkExtractor()

        # try removing ML tags
        linkExtractor.feed(corpus)
        corpus = linkExtractor.getStripped()
        linkedTerms = linkExtractor.getTerms()
        
        # return
        return linkedTerms

# helper class for corpus-related stuff
class CorpusHelper:
    # constructor
    def __init__(self):
        pass
    
    # get plain text corpus
    def getCorpus(self, url = '', plainText = ''):
        import urllib, retriever

        # initialise corpus
        corpus = ''

        # initialise charset
        charset = 'utf-8'
        
        # initialse error message
        error = 0
        errorMessage = ''
        
        # if URL
        if url != 'Enter URL' and url != '':
            # instantiate URL retriever class
            urlRetriever = retriever.URLRetriever()
    
            # try retrieval of URL
            try:
                corpusSet = urlRetriever.retrieveURL(url)
                corpus = corpusSet['corpus']
                charset = corpusSet['charset']
            except IOError:
                print 'test'
                error = 1
                errorMessage = 'URL could not be retrieved'
    
        # if text
        elif plainText != '':
            # decode text
            plainText = urllib.unquote(plainText)
    
            # set URL for display
            url = 'text'
    
            # corpus
            corpus = plainText
            
        # return
        return dict(corpus = corpus,
                    charset = charset,
                    error = error,
                    errorMessage = errorMessage,
                    url = url)

    # get tokenized corpus
    def getTokenizedCorpus(self, tokenizer, corpus = '', language = 'automatic', languages = []):     
        import helper, retriever, classifier, analyser
        
        # create parser helper
        parserHelper = helper.ParserHelper()
        
        # parse corpus
        corpus = parserHelper.getPlainText(corpus)

        # stop word list
        stopWords = retriever.StopWords()
        
        # initialise classifier
        classifier = classifier.BayesClassifier()
        
        # if language is set to 'automatic', try to guess language by Bayesian classification
        if language == 'automatic':
            language = classifier.guessLanguage(stopWords, corpus, languages)

        # strip stop words
        tokenizedCorpus = self.stripStopWords(tokenizer, stopWords, language, corpus)
            
        # return corpus information
        return dict(corpus = corpus,
                    tokenizedCorpus = tokenizedCorpus,
                    language = language)

    # get links from corpus
    def getLinkedTerms(self, tokenizer, corpus = '', language = 'automatic', languages = []):     
        import helper
        
        # create parser helper
        parserHelper = helper.ParserHelper()
        
        # parse corpus
        linkedTerms = parserHelper.getLinkedTerms(corpus)
    
        # if language is set to 'automatic', set language to 'english'
        if language == 'automatic':
            language = 'english'

        # strip stop words
        tokenizedCorpus = self.stripStopWords(tokenizer, '', language, corpus)
            
        # return corpus information
        return dict(tokenizedCorpus = tokenizedCorpus,
                    linkedTerms = linkedTerms)

    def stripStopWords(self, tokenizer, stopWords = '', language = '', corpus = ''):
        import retriever
        
        # if no stop words instance was supplied by user
        if stopWords == '':
            # stop word list
            stopWords = retriever.StopWords()
            
        # get appropriate stop word list for language
        stopWordList = stopWords.getStopWordList(language)

        # tokenize, get paragraphs
        if language == 'german':
            tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 1))
        else:
            tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 0))
        
        # return
        return tokenizedCorpus

    # get tokenized plain text corpus
    def getTokenizedPlainTextCorpus(self, plainText = '', language = '', stopWordList = []):     
        import urllib, helper, retriever, analyser
        
        # decode text
        corpus = urllib.unquote(plainText)

        # tokenizer
        tokenizer = analyser.Tokenizer()

        # tokenize, get paragraphs
        tokenizedCorpus = list(tokenizer.processWhitespaces(corpus, stopWordList, 0))
        
        # return tokenized corpus
        return tokenizedCorpus
    