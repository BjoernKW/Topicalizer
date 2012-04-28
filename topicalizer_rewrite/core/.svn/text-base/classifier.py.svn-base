# Bayes classifier
class BayesClassifier:
    # constructor
    def __init__(self):
        pass
    
    # method for get language guesses
    def getCategoryGuesses(self, corpus1, corpus2, corpus3):
        from reverend.thomas import Bayes

        # instantiate guesser
        guesser = Bayes()

        # train category guesser with first corpus
        guesser.train('first reference text', corpus1)
        guesser.train('second reference text', corpus2)
    
        # compare with second corpus
        guesses = guesser.guess(corpus3)
        
        return guesses
    
    # method for get language guesses
    def getLanguageGuesses(self, stopWords, corpus, languages):
        from reverend.thomas import Bayes

        # charset
        charset = 'us-ascii'

        # instantiate guesser
        guesser = Bayes()

        # go through language in order to train guesser
        for selectLanguage in languages:
            if selectLanguage != 'automatic':
                stopWordString = stopWords.getStopWordString(selectLanguage)
                guesser.train(selectLanguage, stopWordString.encode(charset, 'replace'))
        
        # get list of possible languages
        languageGuesses = guesser.guess(corpus.encode(charset, 'replace'))
        
        return languageGuesses
    
    # method for guessing document language
    def guessLanguage(self, stopWords, corpus, languages):
        # get language guesses
        languageGuesses = self.getLanguageGuesses(stopWords, corpus, languages)

        # get most probable language
        try:
            language = languageGuesses.pop(0)[0]
        except IndexError:
            language = 'english'
            
        return language
