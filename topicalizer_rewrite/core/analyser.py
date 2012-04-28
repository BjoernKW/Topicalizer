# -*- coding: utf-8 -*-

from __future__ import division
import re

# Tokenizer class
class Tokenizer:
    def __init__(self):
    	self.corpus = ''

    # extract tokens from corpus
    def processWhitespaces(self, corpus, stopWordList, caseSensitive, minimumTokenLength = 3, maximumTokenLength = 25):
        from nltk import tokenize
    	
        # initialise token list
    	tokens = []

    	# initialise token buffer
    	tokenBuffer = ''
    
    	# get tokens separated by whitespaces
    	tokenizedCorpus = tokenize.whitespace(corpus)
    
    	# compile regular expression for matching special characters
    	specialCharacters = re.compile(r'\&.+\;')
    
    	# compile regular expression for matching whitespaces
    	whitespaces = re.compile(r'\s|\&nbsp\;')
    
    	# compile regular expression for sentence-boundary matching
    	sentenceBoundary = re.compile(r'[\.\:\!\?\,]')
    
    	# go through each token in corpus
    	for token in tokenizedCorpus:
    	    # get token length
    	    tokenLength = len(token)
    
    	    # see, if token contains special character
    	    specialCharacterMatches = specialCharacters.findall(token)
    
    	    # reduce special characters to size one
    	    if specialCharacterMatches:
        		for match in specialCharacterMatches:
        		    tokenLength -= (len(match) - 1)
    
    	    # if case-sensitive handling of tokens
    	    if caseSensitive == 1:
        		pass
    	    else:
        		token = token.lower()
    
    	    # remove white spaces at beginning and end
    	    token = whitespaces.sub('', token)
    
    	    # write token to buffer and remove punctuation
    	    tokenBuffer = sentenceBoundary.sub('', token)
    
    	    # mark stop words
    	    if tokenLength < minimumTokenLength or tokenLength > maximumTokenLength or tokenBuffer in stopWordList or tokenBuffer.lower() in stopWordList:
        		tokens.append(token + '<STOPWORD>')
    	    else:
        		tokens.append(token)
    
    	# return tokens
    	return tokens

    # extract tokens from corpus, without putting stop words into consideration
    def processWhitespacesWithoutStopWords(self, corpus, caseSensitive):
        from nltk import tokenize
    	
        # initialise token buffer
    	tokens = []
    
    	# get tokens separated by whitespaces
    	tokenizedCorpus = tokenize.whitespace(corpus)
    
    	# compile regular expression for matching whitespaces
    	whitespaces = re.compile(r'\s\&nbsp\;')
    
    	# go through each token in corpus
    	for token in tokenizedCorpus:
    	    # if case-sensitive handling of tokens
    	    if caseSensitive == 1:
        		pass
    	    else:
        		token = token.lower()
    
    	    # remove white spaces at beginning
    	    token = whitespaces.sub('', token)
    
    	    # append token to list
    	    tokens.append(token)
    
    	# return tokens
    	return tokens

    # extract paragraphs from corpus
    def processParagraphs(self, corpus):
        from nltk import tokenize
    	
        # get paragraphs
        paragraphs = tokenize.blankline(corpus)

        # return
    	return paragraphs

# Word structure class
class WordStructure:
    def __init__(self):
    	self.tokens = ''
    	self.stopWordPattern = re.compile('\<STOPWORD\>')

    # get analysis
    def getAnalysis(self, tokens, minWordsPerSentence = 2):
    	# initialise type dictionary
    	types = {}
    
    	# initialise word and sentence lists
    	words = []
    	sentences = []
    	sentenceWordCount = []
    
    	# initialise sentence string list
    	sentenceStrings = []
    
    	# initialise sentence string
    	sentenceString = ''
    
    	# initialise character dictionary
    	charactersPerToken = {}
    
    	# initialise sentence iteration counter
    	i = 0
    
    	# initialise minimum and maximum sentence and token lengths
    	maxSentenceLength = 0
    	minSentenceLength = 1000
    	maxSentence = ''
    	minSentence = ''
    	maxTokenLength = 0
    	minTokenLength = 1000
    	maxToken = ''
    	minToken = ''
    
    	# initialise sum of characters
    	sumOfCharacters = 0
    
    	# compile regular expression for sentence-boundary matching
    	sentenceBoundary = re.compile(r'[\.\:\!\?]')
    
    	# compile regular expression for matching special characters
    	specialCharacters = re.compile(r'\&.+\;')
    
    	# go through tokens
    	for token in tokens:
    	    # add token to sentence
    	    words.append(self.stopWordPattern.sub('', token))
    
    	    # if sentence-boundary has been found in this token
    	    if sentenceBoundary.findall(token):
                # add to sentencelist
                sentenceWordCount.append(len(words))
                sentences.append(words)
                
                # recompose sentence
                sentenceString = ' '.join(words)
                
                # add to sentence string list
                sentenceStrings.append(sentenceString)
        
                # get sentences with maximum length
                sentenceLength = len(words)
                if sentenceLength > maxSentenceLength:
                    maxSentenceLength = sentenceLength
                    maxSentence = sentenceString

        		# get sentence with minimum length
                if sentenceLength < minSentenceLength and sentenceLength >= minWordsPerSentence:
        		    minSentenceLength = sentenceLength
        		    minSentence = sentenceString
        
        		# empty word list
                words[0:] = []
        
        		# empty sentence string
                sentenceString = ''
    
            # only process tokens, if no stop word
            if self.stopWordPattern.findall(token):
            	pass
            else:
            	# calculate type frequencies
            	types[token] = types.get(token, 0) + 1
    
        		# see, if token contains special character
                specialCharacterMatches = specialCharacters.findall(token)
        
        		# get token length
                tokenLength = len(token)
        
        		# reduce special characters to size one
                if specialCharacterMatches:
        		    for match in specialCharacterMatches:
        			tokenLength -= (len(match) - 1)
        
        		# get token with maximum length
                if tokenLength > maxTokenLength:
        		    maxTokenLength = tokenLength
        		    maxToken = token
        
        		# get token with minimum length
                if tokenLength < minTokenLength:
        		    minTokenLength = tokenLength
        		    minToken = token
        
        		# get characters per token
                charactersPerToken[token] = tokenLength
        
        		# add to grand total of characters
                sumOfCharacters += charactersPerToken[token]
    
    	# build dictionary with return values and return it
    	returnDict = dict(types = types,
            			  sentences = sentences,
            			  sentenceStrings = sentenceStrings,
            			  maxSentenceLength = maxSentenceLength,
            			  minSentenceLength = minSentenceLength,
            			  maxTokenLength = maxTokenLength,
            			  minTokenLength = minTokenLength,
            			  maxSentence = maxSentence,
            			  minSentence = minSentence,
            			  maxToken = maxToken,
            			  minToken = minToken,
            			  charactersPerToken = charactersPerToken,
            			  sumOfCharacters = sumOfCharacters)
        
    	return returnDict

    # analyse syllables
    def getSyllableInformation(self, tokens, types):
    	# define dictionaries for syllables per token and type
    	syllablesPerToken = {}
    	syllablesPerType = {}

    	# initialise total amount of syllables
    	sum = 0
    
    	# compile regular expression for counting syllables
    	syllables = re.compile(r'[\;AEIOU���Yaeiou���y][BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz]')
    
    	# go through each token
    	for token in tokens:
    	    matches = syllables.findall(token)
    	    syllablesPerToken[token] = len(matches)
    	    sum += syllablesPerToken[token]
    
    	# go through each type
    	for type in types:
    	    matches = syllables.findall(type)
    	    syllablesPerType[type] = len(matches)
    
    	# compile return dictionary and return it
    	returnDict = dict(syllablesPerToken= syllablesPerToken,
            			  syllablesPerType= syllablesPerType,
            			  sum = sum)
    	return returnDict

# Sentence structure class
class SentenceStructure:
    def __init__(self):
    	self.underscore = re.compile(r'_')

    # augment keywords from words in sentence
    def augmentKeywordsFromSentence (self, stopWordList, tokens):
        from stdwn import impl

    	# initialise keyword list
    	keywords = []
    
    	# get WordNet information for each relevant word
    	for token in tokens:
    	    # get synsets
    	    synsets = impl.lookupSynsetsByForm(token)
    
            # go through synsets
            for synset in synsets:
            	# append synonyms
            	for synonym in synset.synonyms:
            	    keywords.append(self.underscore.sub(' ', synonym.form))
        
                # go through hyponyms
                for hyponym in synset.hyponyms():
                    # append synonyms
                    for synonym in hyponym.synonyms:
                        keywords.append(self.underscore.sub(' ', synonym.form))
        
                # go through hypernyms
                for hypernym in synset.relations('@'):
                    # append synonyms
                    for synonym in hypernym.synonyms:
                        keywords.append(self.underscore.sub(' ', synonym.form))
    
    	# build set with unique values
    	keywords = set(keywords)
    
    	# return keywords
    	return keywords

    # get co-occurrences for words in sentence using a database
    def getCoOccurrencesFromDB (self, stopWordList, tokens, textCategory):
        from topicalizer.model import token_by_category, co_occurrence

    	# initialise keyword list
    	keywords = []
    
    	# initialise token entity list
    	tokenEntities = []
    
    	# initialise co-occurrence entity list
    	coOccurrenceEntities = []
    
    	# get co-occurrences for each word
    	for token in tokens:
            # get token information from database
            try:
            	tokenEntities = list(token_by_category.select("""token_by_category.token='""" + token + """' AND token_by_category.category='""" + textCategory + """'"""))
            	tokenEntity = tokenEntities[0]
            	tokenID = str(tokenEntity.id)
    
    		    # get five most frequent co-occurrences from database
                coOccurrenceEntities = list(co_occurrence.select("""co_occurrence.co_occurs_with='""" + tokenID + """'""", orderBy = co_occurrence.q.count).reversed())[:10]
    
    		    # get coOccurrences for each token
                for coOccurrenceEntity in coOccurrenceEntities:
    		        keywords.append(coOccurrenceEntity.token)
    	    except IndexError:
        		pass
    
    	# build set with unique values
    	keywords = set(keywords)
    
    	# return keywords
    	return keywords

# Text structure class
class TextStructure:
    def __init__(self):
	self.stopWordPattern = re.compile('\<STOPWORD\>')

    # analyse readability according to Gunning-Fog Index
    def analyseReadabilityGF(self, averageTokensPerSentence, syllablesPerType, tokenCount):
    	# initialise number of types with three or more syllables
    	numberOfComplexTypes = 0
    
    	# initialise complex types buffer
    	complexTypes = []
    
    	# go through types
    	for type in syllablesPerType:
    	   if syllablesPerType[type] >= 3:
    	       numberOfComplexTypes += 1
    	       complexTypes.append(type)
    
    	# calculate percentage of types with three or more syllables
    	percentageOfComplexTypes = numberOfComplexTypes * 100 / tokenCount
    
    	# calculate readability
    	readability = round((averageTokensPerSentence + percentageOfComplexTypes) * 0.4, 2)
    
    	# return readability
    	return readability

    # analyse readability according to Automated Readability Index
    def analyseReadabilityAR(self, averageCharactersPerWord, averageTokensPerSentence):
    	# calculate readability
    	readability = round((4.71 * averageCharactersPerWord) + (0.5 * averageTokensPerSentence) - 21.43, 2)
    
    	# return readability
    	return readability

    # analyse readability according to Coleman-Liau Index
    def analyseReadabilityCL(self, averageCharactersPerWord, sentenceCount, tokenCount):
    	# calculate readability
    	readability = round((5.89 * averageCharactersPerWord) -  (3 * sentenceCount) / (1000 * tokenCount) - 15.8, 2)
    
    	# return readability
    	return readability

    # get n-grams
    def getNGrams(self, tokens, tokenCount):
        from operator import itemgetter

    	# compile regular expression for sentence-boundary matching
    	sentenceBoundary = re.compile(r'[\.\:\!\?\,]')
    
    	# compile regular expression for whitespace matching
    	whitespaces = re.compile(r'^\s+?$')
    
    	# initialise unigram, bigram and trigram rank lists
    	mostFrequentUnigrams = {}
    	mostFrequentUnigramsAbstract = {}
    	mostFrequentBigrams = {}
    	mostFrequentTrigrams = {}
    	mostFrequentUnigramsAll = {}
    	mostFrequentBigramsAll = {}
    	mostFrequentTrigramsAll = {}
    	mostFrequentTetragramsAll = {}
    	mostFrequentPentagramsAll = {}
    	mostFrequentBigramsWithStopWords = {}
    	mostFrequentTrigramsWithStopWords = {}
    	mostFrequentBigramsWithStopWordsAll = {}
    	mostFrequentTrigramsWithStopWordsAll = {}
    	mostFrequentTetragramsWithStopWordsAll = {}
    	mostFrequentPentagramsWithStopWordsAll = {}
    
    	# initialise frequency dictionaries
    	unigramFrequencies = {}
    	bigramFrequencies = {}
    	trigramFrequencies = {}
    	tetragramFrequencies = {}
    	pentagramFrequencies = {}
    	bigramFrequenciesWithStopWords = {}
    	trigramFrequenciesWithStopWords = {}
    	tetragramFrequenciesWithStopWords = {}
    	pentagramFrequenciesWithStopWords = {}
    
    	# initialise buffers
    	bigram = ''
    	trigram = ''
    	tetragram = ''
    	pentagram = ''
    	bigramWithStopWords = ''
    	trigramWithStopWord = ''
    	tetragramWithStopWords = ''
    	pentagramWithStopWord = ''
    	unigramBuffer = ''
    	bigramBuffer = ''
    	trigramBuffer = ''
    	tetragramBuffer = ''
    	pentagramBuffer = ''
    	bigramWithStopWordsBuffer = ''
    	trigramWithStopWordBuffer = ''
    	tetragramWithStopWordsBuffer = ''
    	pentagramWithStopWordBuffer = ''
    
    	# build frequency dictionaries
    	for i, token in enumerate(tokens):
    	    # unigrams
    	    if (i < tokenCount):
        		# only process tokens, if no stop word
        		if self.stopWordPattern.findall(token):
        		    pass
        		else:
        		    # remove punctuation
        		    unigramBuffer = sentenceBoundary.sub('', token)
        
        		    # process unigrams
        		    if unigramBuffer != '' and not whitespaces.search(unigramBuffer):
            			unigramFrequencies[unigramBuffer] = unigramFrequencies.get(unigramBuffer, 0) + 1
    
    	    # only process n-grams, if no sentence boundary detected in first token
    	    if sentenceBoundary.findall(token):
        		pass
    	    else:
                # bigrams
                if (i + 1 < tokenCount):
                    # bigram strings
                    bigram = token + " " + tokens[i + 1]
                    bigramWithStopWords = self.stopWordPattern.sub('', token + " " + tokens[i + 1])
                    
                    # remove punctuation
                    bigramWithStopWordsBuffer = sentenceBoundary.sub('', bigramWithStopWords)
                    
                    # process bigrams with stop words
                    if bigramWithStopWordsBuffer != '' and not whitespaces.search(bigramWithStopWordsBuffer):
                        bigramFrequenciesWithStopWords[bigramWithStopWordsBuffer] = bigramFrequenciesWithStopWords.get(bigramWithStopWordsBuffer, 0) + 1
                
                    # only process bigram, if no stop word contained
                    if self.stopWordPattern.findall(bigram):
                    	pass
                    else:
                    	# remove punctuation
                    	bigramBuffer = sentenceBoundary.sub('', bigram)
                
                    	# process bigrams
                        if bigramBuffer != '' and not whitespaces.search(bigramBuffer):
                    	    bigramFrequencies[bigramBuffer] = bigramFrequencies.get(bigramBuffer, 0) + 1
                
                # trigrams
                if (i + 2 < tokenCount):
                    # only process trigrams, if no sentence boundary detected in second token
                    if sentenceBoundary.findall(tokens[i + 1]):
                		pass
                    else:
                		# trigram strings
                		trigram = token + " " + tokens[i + 1] + " " + tokens[i + 2]
                		trigramWithStopWords = self.stopWordPattern.sub('', token + " " + tokens[i + 1] + " " + tokens[i + 2])
                
                		# remove punctuation
                		trigramWithStopWordsBuffer = sentenceBoundary.sub('', trigramWithStopWords)
                
                		# process trigrams with stop words
                		if trigramWithStopWordsBuffer != '' and not whitespaces.search(trigramWithStopWordsBuffer):
                		    trigramFrequenciesWithStopWords[trigramWithStopWordsBuffer] = trigramFrequenciesWithStopWords.get(trigramWithStopWordsBuffer, 0) + 1
                
                		# only process trigram, if no stop word contained
                		if self.stopWordPattern.findall(trigram):
                		    pass
                		else:
                		    # remove punctuation
                		    trigramBuffer = sentenceBoundary.sub('', trigram)
                
                		    # process trigrams
                		    if trigramBuffer != '' and not whitespaces.search(trigramBuffer):
                				trigramFrequencies[trigramBuffer] = trigramFrequencies.get(trigramBuffer, 0) + 1
                
                # tetragrams
                if (i + 3 < tokenCount):
                    # only process tetragrams, if no sentence boundary detected in second or third token
                    if sentenceBoundary.findall(tokens[i + 1]) or sentenceBoundary.findall(tokens[i + 2]):
                    	pass
                    else:
                        # tetragram strings
                        tetragram = token + " " + tokens[i + 1] + " " + tokens[i + 2] + " " + tokens[i + 3]
                        tetragramWithStopWords = self.stopWordPattern.sub('', token + " " + tokens[i + 1] + " " + tokens[i + 2] + " " + tokens[i + 3])
                        
                        # remove punctuation
                        tetragramWithStopWordsBuffer = sentenceBoundary.sub('', tetragramWithStopWords)
                        
                        # process tetragrams with stop words
                        if tetragramWithStopWordsBuffer != '' and not whitespaces.search(tetragramWithStopWordsBuffer):
                            tetragramFrequenciesWithStopWords[tetragramWithStopWordsBuffer] = tetragramFrequenciesWithStopWords.get(tetragramWithStopWordsBuffer, 0) + 1
                        
                        # only process tetragram, if no stop word contained
                        if self.stopWordPattern.findall(tetragram):
                            pass
                        else:
                            # remove punctuation
                            tetragramBuffer = sentenceBoundary.sub('', tetragram)
                
                            # process tetragrams
                            if tetragramBuffer != '' and not whitespaces.search(tetragramBuffer):
                                tetragramFrequencies[tetragramBuffer] = tetragramFrequencies.get(tetragramBuffer, 0) + 1
                
                # pentagrams
                if (i + 4 < tokenCount):
                    # only process pentagrams, if no sentence boundary detected in second, third or fourth token
                    if sentenceBoundary.findall(tokens[i + 1]) or sentenceBoundary.findall(tokens[i + 2])  or sentenceBoundary.findall(tokens[i + 3]):
                    	pass
                    else:
                        # pentagram strings
                        pentagram = token + " " + tokens[i + 1] + " " + tokens[i + 2] + " " + tokens[i + 3] + " " + tokens[i + 4]
                        pentagramWithStopWords = self.stopWordPattern.sub('', token + " " + tokens[i + 1] + " " + tokens[i + 2] + " " + tokens[i + 3] + " " + tokens[i + 4])
                        
                        # remove punctuation
                        pentagramWithStopWordsBuffer = sentenceBoundary.sub('', pentagramWithStopWords)
                        
                        # process pentagrams with stop words
                        if pentagramWithStopWordsBuffer != '' and not whitespaces.search(pentagramWithStopWordsBuffer):
                            pentagramFrequenciesWithStopWords[pentagramWithStopWordsBuffer] = pentagramFrequenciesWithStopWords.get(pentagramWithStopWordsBuffer, 0) + 1
                        
                        # only process pentagram, if no stop word contained
                        if self.stopWordPattern.findall(pentagram):
                            pass
                        else:
                            # remove punctuation
                            pentagramBuffer = sentenceBoundary.sub('', pentagram)
                            
                            # process pentagrams
                            if pentagramBuffer != '' and not whitespaces.search(pentagramBuffer):
                                pentagramFrequencies[pentagramBuffer] = pentagramFrequencies.get(pentagramBuffer, 0) + 1
    
    	# get ten most frequent unigram tokens
    	for unigram, value in sorted(unigramFrequencies.iteritems(), key = itemgetter(1), reverse = True)[0:10]:
    	    mostFrequentUnigrams[unigram] = value
    
    	# get ten most frequent unigram tokens for abstract
    	for unigram, value in sorted(unigramFrequencies.iteritems(), key = itemgetter(1), reverse = True)[0:3]:
    	    mostFrequentUnigramsAbstract[unigram] = value
    
    	# get ten most frequent bigram tokens
    	for bigram, value in sorted(bigramFrequencies.iteritems(), key = itemgetter(1), reverse = True)[0:10]:
    	    mostFrequentBigrams[bigram] = value
    
    	# get ten most frequent trigram tokens
    	for trigram, value in sorted(trigramFrequencies.iteritems(), key = itemgetter(1), reverse = True)[0:10]:
    	    mostFrequentTrigrams[trigram] = value
    
    	# get most frequent unigram tokens with frequency > 1
    	for unigram, value in sorted(unigramFrequencies.iteritems(), key = itemgetter(1), reverse = True):
    	    if value > 1:
                mostFrequentUnigramsAll[unigram] = value
    
    	# get ten most frequent bigram tokens with frequency > 1
    	for bigram, value in sorted(bigramFrequencies.iteritems(), key = itemgetter(1), reverse = True):
    	    if value > 1:
                mostFrequentBigramsAll[bigram] = value
    
    	# get ten most frequent trigram tokens with frequency > 1
    	for trigram, value in sorted(trigramFrequencies.iteritems(), key = itemgetter(1), reverse = True):
    	    if value > 1:
                mostFrequentTrigramsAll[trigram] = value
    
    	# get most frequent tetragram tokens
    	for tetragram, value in sorted(tetragramFrequencies.iteritems(), key = itemgetter(1), reverse = True):
    	    if value > 1:
                mostFrequentTetragramsAll[tetragram] = value
    
    	# get most frequent pentagram tokens
    	for pentagram, value in sorted(pentagramFrequencies.iteritems(), key = itemgetter(1), reverse = True):
    	    if value > 1:
                mostFrequentPentagramsAll[pentagram] = value
    
    	# get ten most frequent bigram tokens, including stop words
    	for bigram, value in sorted(bigramFrequenciesWithStopWords.iteritems(), key = itemgetter(1), reverse = True)[0:10]:
            mostFrequentBigramsWithStopWords[bigram] = value
    
    	# get ten most frequent trigram tokens, including stop words
    	for trigram, value in sorted(trigramFrequenciesWithStopWords.iteritems(), key = itemgetter(1), reverse = True)[0:10]:
    	    mostFrequentTrigramsWithStopWords[trigram] = value
    
    	# get most frequent bigram tokens with frequency > 1, including stop words
    	for bigram, value in sorted(bigramFrequenciesWithStopWords.iteritems(), key = itemgetter(1), reverse = True):
    	    if value > 1:
                mostFrequentBigramsWithStopWordsAll[bigram] = value
    
    	# get most frequent trigram tokens with frequency > 1, including stop words
    	for trigram, value in sorted(trigramFrequenciesWithStopWords.iteritems(), key = itemgetter(1), reverse = True):
    	    if value > 1:
                mostFrequentTrigramsWithStopWordsAll[trigram] = value
    
    	# get most frequent tetragram tokens with frequency > 1, including stop words
    	for tetragram, value in sorted(tetragramFrequenciesWithStopWords.iteritems(), key = itemgetter(1), reverse = True):
    	    if value > 1:
                mostFrequentTetragramsWithStopWordsAll[tetragram] = value
    
    	# get most frequent pentagram tokens with frequency > 1, including stop words
    	for pentagram, value in sorted(pentagramFrequenciesWithStopWords.iteritems(), key = itemgetter(1), reverse = True):
    	    if value > 1:
                mostFrequentPentagramsWithStopWordsAll[pentagram] = value
    
    	# build dictionary with return values and return it
    	returnDict = dict(mostFrequentUnigrams = mostFrequentUnigrams,
            			  mostFrequentUnigramsAbstract = mostFrequentUnigramsAbstract,
            			  mostFrequentBigrams = mostFrequentBigrams,
            			  mostFrequentTrigrams = mostFrequentTrigrams,
            			  mostFrequentUnigramsAll = mostFrequentUnigramsAll,
            			  mostFrequentBigramsAll = mostFrequentBigramsAll,
            			  mostFrequentTrigramsAll = mostFrequentTrigramsAll,
            			  mostFrequentTetragramsAll = mostFrequentTetragramsAll,
            			  mostFrequentPentagramsAll = mostFrequentPentagramsAll,
            			  mostFrequentBigramsWithStopWords = mostFrequentBigramsWithStopWords,
            			  mostFrequentTrigramsWithStopWords = mostFrequentTrigramsWithStopWords,
            			  mostFrequentBigramsWithStopWordsAll = mostFrequentBigramsWithStopWordsAll,
            			  mostFrequentTrigramsWithStopWordsAll = mostFrequentTrigramsWithStopWordsAll,
            			  mostFrequentTetragramsWithStopWordsAll = mostFrequentTetragramsWithStopWordsAll,
            			  mostFrequentPentagramsWithStopWordsAll = mostFrequentPentagramsWithStopWordsAll)
        
    	return returnDict

    # get keywords
    def getKeywords(self, mostFrequentUnigrams, mostFrequentBigrams, mostFrequentTrigrams,mostFrequentBigramsWithStopWords, mostFrequentTrigramsWithStopWords):
        from operator import itemgetter
    	
        # initialise keyword list
    	keywords = []
    
    	# initialise keyword buffer list
    	keywordsBuffer = []
    
    	# compile regular expression for sentence-boundary matching
    	sentenceBoundary = re.compile(r'[\.\:\!\?\,]')
    
    	# go through ten most frequent unigram tokens
    	for unigram, unigramValue in sorted(mostFrequentUnigrams.iteritems(), key = itemgetter(1), reverse = True):
    	    # go through ten most frequent bigram tokens for this unigram
    	    for bigram, bigramValue in sorted(mostFrequentBigrams.iteritems(), key = itemgetter(1), reverse = True):
        		# regular expression for matching unigram to bigram
        		if re.findall(re.escape(unigram), bigram, re.I):
        		    keywords.append(unigram)
        		    keywords.append(bigram)
    
    	    # go through ten most frequent trigram tokens for this unigram
    	    for trigram, trigramValue in sorted(mostFrequentTrigrams.iteritems(), key = itemgetter(1), reverse = True):
        		# regular expression for matching unigram to trigram
        		if re.findall(re.escape(unigram), trigram, re.I):
        		    keywords.append(unigram)
        		    keywords.append (trigram)
    
    	    # go through ten most frequent trigram tokens with stop words for this unigram
    	    for trigram, trigramValue in sorted(mostFrequentTrigramsWithStopWords.iteritems(), key = itemgetter(1), reverse = True):
        		# regular expression for matching unigram to trigram
        		if re.findall(re.escape(unigram), trigram, re.I):
        		    keywords.append(unigram)
        		    keywords.append (trigram)
    
    	# go through ten most frequent bigram tokens
    	for bigram, bigramValue in sorted(mostFrequentBigrams.iteritems(), key = itemgetter(1), reverse = True):
    	    # go through ten most frequent trigram tokens for this bigram
    	    for trigram, trigramValue in sorted(mostFrequentTrigrams.iteritems(), key = itemgetter(1), reverse = True):
        		# regular expression for matching bigram to trigram
        		if re.findall(re.escape(bigram), trigram, re.I):
        		    keywords.append (bigram)
        		    keywords.append (trigram)
    
    	# remove commas
    	for keyword in keywords:
    	    keywordsBuffer.append(sentenceBoundary.sub('', keyword))
    
    	# build set with unique keyword values from keywordsBuffer
    	keywords = set(keywordsBuffer)
    
    	# return keywords
    	return keywords

    # get keywords with frequencies
    def getKeywordsWithFrequencies(self, mostFrequentUnigrams, mostFrequentBigrams, mostFrequentTrigrams,mostFrequentBigramsWithStopWords, mostFrequentTrigramsWithStopWords):
        from operator import itemgetter
    	
        # initialise keyword dictionary
    	keywords = {}
    
    	# initialise keyword buffer dictionary
    	keywordsBuffer = {}
    
    	# compile regular expression for sentence-boundary matching
    	sentenceBoundary = re.compile(r'[\.\:\!\?\,]')
    
    	# go through ten most frequent unigram tokens
    	for unigram, unigramValue in sorted(mostFrequentUnigrams.iteritems(), key = itemgetter(1), reverse = True):
    	    # go through ten most frequent bigram tokens for this unigram
    	    for bigram, bigramValue in sorted(mostFrequentBigrams.iteritems(), key = itemgetter(1), reverse = True):
        		# regular expression for matching unigram to bigram
        		if re.findall(re.escape(unigram), bigram, re.I):
        		    keywords[unigram] = keywords.get(unigram, unigramValue) + unigramValue
        		    keywords[bigram] = keywords.get(bigram, bigramValue) + bigramValue
    
    	    # go through ten most frequent trigram tokens for this unigram
    	    for trigram, trigramValue in sorted(mostFrequentTrigrams.iteritems(), key = itemgetter(1), reverse = True):
        		# regular expression for matching unigram to trigram
        		if re.findall(re.escape(unigram), trigram, re.I):
        		    keywords[unigram] = keywords.get(unigram, unigramValue) + unigramValue
        		    keywords[trigram] = keywords.get(trigram, trigramValue) + trigramValue
    
    	    # go through ten most frequent trigram tokens with stop words for this unigram
    	    for trigram, trigramValue in sorted(mostFrequentTrigramsWithStopWords.iteritems(), key = itemgetter(1), reverse = True):
        		# regular expression for matching unigram to trigram
        		if re.findall(re.escape(unigram), trigram, re.I):
        		    keywords[unigram] = keywords.get(unigram, unigramValue) + unigramValue
        		    keywords[trigram] = keywords.get(trigram, trigramValue) + trigramValue
    
    	# go through ten most frequent bigram tokens
    	for bigram, bigramValue in sorted(mostFrequentBigrams.iteritems(), key = itemgetter(1), reverse = True):
    	    # go through ten most frequent trigram tokens for this bigram
    	    for trigram, trigramValue in sorted(mostFrequentTrigrams.iteritems(), key = itemgetter(1), reverse = True):
        		# regular expression for matching bigram to trigram
        		if re.findall(re.escape(bigram), trigram, re.I):
        		    keywords[bigram] = keywords.get(bigram, bigramValue) + bigramValue
        		    keywords[trigram] = keywords.get(trigram, trigramValue) + trigramValue
    
    	# remove commas
    	for keyword, keywordValue in keywords.iteritems():
    	    keywordsBuffer[sentenceBoundary.sub('', keyword)] = keywordValue
    
    	# return keywords
    	return keywords

    # get abstract
    def getAbstract(self, keywords, sentences):
    	# initialise abstract dictionary
    	abstract = {}

    	# go through sentences
    	for sentence in sentences:
    	    # go through keywords
    	    for keyword in keywords:
        		# regular expression for matching unigram to sentence
        		if re.findall(re.escape(keyword), sentence, re.I):
        		    abstract[sentence] = abstract.get(sentence, 0) + 1
    
    	# return abstract
    	return abstract
