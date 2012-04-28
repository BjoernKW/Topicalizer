import pickle
from operator import itemgetter

# set path
path = './corpora/brown/'

# open file
file = open(path + 'a.co.dump', 'r')

# get co-occurrence matrix
coOccurrences = pickle.load(file)

# go through each token
for token in coOccurrences:
    # print token
    print token

    # get most frequent co-occurrences
    thisCoOccurrences = coOccurrences[token]
    mostFrequentCoOccurrences = sorted(thisCoOccurrences.iteritems(), key = itemgetter(1), reverse = True)[0:5]

    # get coOccurrences for each token
    for coOccurrence in mostFrequentCoOccurrences:
	print coOccurrence[0], coOccurrence[1]
