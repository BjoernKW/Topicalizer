from reverend.thomas import Bayes
import retriever, urllib

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

# set test corpus
url = 'http://fr.wikipedia.org/wiki/Mégalithe'
url = urllib.unquote(url)

# instantiate URL retriever class
urlRetriever = retriever.URLRetriever()

# try retrieval of url
try:
    corpusSet = urlRetriever.retrieveURL(url)
    corpus = corpusSet['corpus']
    charset = corpusSet['charset']
except IOError:
    error = 1
    errorMessage = 'URL could not be retrieved'

# stop word object
stopWords = retriever.StopWords()

# guess language
guesser = Bayes()
for selectLanguage in languages:
    if selectLanguage != 'automatic':
	stopWordString = stopWords.getStopWordString(selectLanguage)
	guesser.train(selectLanguage, stopWordString)
	language = guesser.guess(corpus)

	# print stopword string
	print stopWordString

# print language
# print language.pop(0)[0]
print language
