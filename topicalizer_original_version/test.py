import retriever, analyser, re

# instantiate URL retriever class
urlRetriever = retriever.URLRetriever()

# get corpus
# corpus = urlRetriever.retrieveURL('http://www.krohne-mar.com/Schwebekoerper-Durchflussmessgeraete_nass_kalibriert.11121.0.html')
corpusSet = urlRetriever.retrieveURL('http://linguistik-fachschaft.de/info.html')
corpus = corpusSet['corpus']
charset = corpusSet['charset']

# ML tag stripper
mlStripper = retriever.MLStripper()

# remove ML tags
mlStripper.feed(corpus)
corpus = mlStripper.getStripped()

# stop word list
stopWords = retriever.StopWords()
stopWordList = stopWords.getStopWordList('german')

# tokenizer
tokenizer = analyser.Tokenizer()

# tokenize
tokens = tokenizer.processWhitespaces(corpus, stopWordList, 1)
tokenCount = len(tokens)

# analyse text structure
textStructure = analyser.TextStructure()

# get N-grams
ngrams = textStructure.getNGrams(tokens, tokenCount)

# print
# print tokens
# print stopWordList

# write to file
# file = open ('./test.txt', 'w')
# file.write(corpus)
