from nltk_lite import tokenize, tag
from nltk_lite.corpora import brown, set_basedir
from stdwn import impl
import analyser

# set text categories
textCategories = dict(pressReportage = 'a',
		      pressEditorial = 'b',
		      pressReviews = 'c',
		      religion = 'd',
		      skillsAndHobbies = 'e',
		      popularLore = 'f',
		      bellesLettres = 'g',
		      miscellaneousGovernmentAndHouseOrgans = 'h',
		      learned = 'j',
		      fictionGeneral = 'k',
		      fictionMystery = 'l',
		      fictionScience = 'm',
		      fictionAdventure = 'n',
		      fictionRomance = 'p',
		      humour = 'r')

# set corpus basedir
set_basedir('./topicalizer/corpora')

# create tokenizer
tokenizer = analyser.Tokenizer()

# train tagging model
model = tag.Bigram()
model.train(brown.tagged([textCategories['pressReportage'], textCategories['pressEditorial'], textCategories['pressReviews'], textCategories['skillsAndHobbies'], textCategories['popularLore']]))

# tag text
text = 'I want to buy a camera'
tokens = list(tokenizer.processWhitespacesWithoutStopWords(text, 1))
taggedTokens = list(model.tag(tokens))
print tokens
print taggedTokens

# get WordNet information for each noun
for taggedToken in taggedTokens:
    if taggedToken[1] == 'nn' or taggedToken[1] == None:
	# get synsets
	synsets = impl.lookupSynsetsByForm(taggedToken[0])

	# print gloss
	for synset in synsets:
	    # go through synonyms
	    print '--------------------------------------------------------------'
	    for synonym in synset.synonyms:
		print synonym.form

	    # go through hyponyms
	    print '- Hyponyms ------------------------------------------------------------'
	    for hyponym in synset.hyponyms():
		for hypoSynonym in hyponym.synonyms:
		    print synonym.form, hypoSynonym.form

	    # go through hypernyms
	    print '- Hypernyms -----------------------------------------------------------'
	    for hypernym in synset.relations('@'):
		for hyperSynonym in hypernym.synonyms:
		    print synonym.form, hyperSynonym.form
