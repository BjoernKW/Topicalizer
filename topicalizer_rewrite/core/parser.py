import re, HTMLParser

# link extractor class
class LinkExtractor(HTMLParser.HTMLParser):
    def __init__(self, minimumLength = 3):
    	self.reset()
    	self.urlInfo = {}
    	self.terms = []
    	self.fed = []
    	self.blockData = 0
    	self.tag = ''
    	self.url = ''
    	self.href = ''
    	self.minimumLength = minimumLength

    def handle_starttag(self, t, attrs):
    	# get current tag
    	self.tag = t
    
    	# get 'href' attribute
    	for k, v in attrs:
    	    if k == 'href':
        		self.href = v
    
    	# handle 'a' tags
    	if self.href != '':
    	    self.blockData = 0
    	    self.url = self.href
    	else:
    	    self.blockData = 1

    def handle_endtag(self, t):
    	# block data and reset 'href' value after
    	# processing of a tag
    	self.blockData = 1
    	self.href = ''

    def handle_data(self, d):
    	# compile regular expression for filtering non-XML-safe characters
    	ampersand = re.compile(r'\&')
    	lessThan = re.compile(r'\<')
    	greaterThan = re.compile(r'\>')
    	quote = re.compile(r'\"')
    
    	# compile regular expression for matching special characters
    	specialCharacters = re.compile(r'\&.+\;')
    
    	# compile regular expression for matching foot notes
    	footNote = re.compile(r'\[\d+\]')
    
    	# compile regular expression for matching special Wikipedia links
    	special = re.compile(r':|\/w\/')
    
    	# compile regular expression for matching URLs
    	urlMatcher = re.compile(r'http:')
    
    	# get token length
    	tokenLength = len(d)
    
    	# see, if token contains special character
    	specialCharacterMatches = specialCharacters.findall(d)
    
    	# see, if token is foot note
    	footNoteMatches = footNote.findall(d)
    
    	# see, if token is special link
    	specialMatches = special.findall(self.url)
    
    	# see, if token contains a URL
    	contentIsURLMatches = urlMatcher.findall(d)
    
    	# see, if token is Wikipedia-external
    	wikipediaExternalMatches = urlMatcher.findall(self.url)
    
    	# reduce special characters to size one
    	if specialCharacterMatches:
    	    for match in specialCharacterMatches:
        		tokenLength -= (len(match) - 1)
    		
    	# if token is smaller than minimum length
    	if tokenLength < self.minimumLength:
    	    self.blockData = 1
    
    	# if token is no content link
    	if footNoteMatches or specialMatches or contentIsURLMatches or wikipediaExternalMatches:
    	    self.blockData = 1
    
    	# block everything that does not meet our conditions
    	if self.blockData == 1:
    	    pass
    
    	# handle link content
    	else:
    	    # handle non-XML-safe characters
    	    d = ampersand.sub('&amp;', d)
    	    d = lessThan.sub('&lt;', d)
    	    d = greaterThan.sub('&gt;', d)
    	    d = quote.sub('&quot;', d)
    
    	    # append
    	    self.fed.append(d)
    	    self.terms.append(dict(url = self.url,
                                   text = d))
    
    def handle_entityref(self, d):
    	# compile regular expressions
    	blankSpace = re.compile(r'nbsp')
    	ss = re.compile(r'szlig')
    	ae = re.compile(r'auml')
    	oe = re.compile(r'ouml')
    	ue = re.compile(r'uuml')
    	AE = re.compile(r'Auml')
    	OE = re.compile(r'Ouml')
    	UE = re.compile(r'Uuml')
    	lt = re.compile(r'lt')
    	gt = re.compile(r'gt')
    	amp = re.compile(r'amp')
    	middot = re.compile(r'middot')
    
    	# handle blank spaces
    	if blankSpace.findall(d):
    	    self.fed.append('&' + d + ';')
    
    	# handle 'lt'
    	elif lt.findall(d):
    	    pass
    
    	# handle 'gt'
    	elif gt.findall(d):
    	    pass
    
    	# handle 'amp'
    	elif amp.findall(d):
    	    pass
    
    	# handle 'middot'
    	elif middot.findall(d):
    	    pass
    
    	# handle other entities
    	else:
    	    self.fed.append('&' + d + ';')

    def handle_comment(self, d):
    	pass

    def getStripped(self):
    	return ''.join(self.fed)

    def getTerms(self):
    	return (self.terms)

# ML tag stripper class
class MLStripper(HTMLParser.HTMLParser):
    def __init__(self):
    	self.reset()
    	self.fed = []
    	self.blockData = 0
    	self.tag = ''

    def handle_starttag(self, t, attrs):
    	# compile regular expression for filtering script and style sections
    	scriptContentOpen = re.compile(r'script')
    	styleContentOpen = re.compile(r'style')
    
    	# get current tag
    	self.tag = t
    
    	# handle comments enclosed in tags
    	if scriptContentOpen.findall(t) or styleContentOpen.findall(t):
    	    self.blockData = 1
    	else:
    	    self.blockData = 0

    def handle_data(self, d):
    	# compile regular expression for filtering comments enclosed in tags
    	mlComments = re.compile(r'!--')
    
    	# compile regular expression for filtering non-XML-safe characters
    	ampersand = re.compile(r'\&')
    	lessThan = re.compile(r'\<')
    	greaterThan = re.compile(r'\>')
    	quote = re.compile(r'\"')
    
    	# handle comments, scripts and styles enclosed in tags
    	if mlComments.findall(d) or self.blockData == 1:
    	    pass
    
    	# handle normal content
    	else:
    	    # handle non-XML-safe characters
    	    d = ampersand.sub('&amp;', d)
    	    d = lessThan.sub('&lt;', d)
    	    d = greaterThan.sub('&gt;', d)
    	    d = quote.sub('&quot;', d)
    
    	    # append
            self.fed.append(d)

    def handle_entityref(self, d):
    	# compile regular expressions
    	blankSpace = re.compile(r'nbsp')
    	ss = re.compile(r'szlig')
    	ae = re.compile(r'auml')
    	oe = re.compile(r'ouml')
    	ue = re.compile(r'uuml')
    	AE = re.compile(r'Auml')
    	OE = re.compile(r'Ouml')
    	UE = re.compile(r'Uuml')
    	lt = re.compile(r'lt')
    	gt = re.compile(r'gt')
    	amp = re.compile(r'amp')
    	middot = re.compile(r'middot')
    
    	# handle blank spaces
    	if blankSpace.findall(d):
    	    self.fed.append('&' + d + ';')
    
    	# handle 'lt'
    	elif lt.findall(d):
    	    pass
    
    	# handle 'gt'
    	elif gt.findall(d):
    	    pass
    
    	# handle 'amp'
    	elif amp.findall(d):
    	    pass
    
    	# handle 'middot'
    	elif middot.findall(d):
    	    pass
    
    	# handle other entities
    	else:
    	    self.fed.append('&' + d + ';')

    def handle_comment(self, d):
    	pass

    def getStripped(self):
    	return ''.join(self.fed)

# ML tag fallback class
class MLFallback:
    def __init__(self):
    	pass

    def getStripped(self, corpus):
    	# compile regular expressions for filtering tags
    	tagPattern = re.compile(r'<.+?>')
    	tagStart = re.compile(r'<')
    	tagEnd = re.compile(r'>')
    	blankSpace = re.compile(r'\&nbsp;')
    	ss = re.compile(r'\&szlig;')
    	ae = re.compile(r'\&auml;')
    	oe = re.compile(r'\&ouml;')
    	ue = re.compile(r'\&uuml;')
    	AE = re.compile(r'\&Auml;')
    	OE = re.compile(r'\&Ouml;')
    	UE = re.compile(r'\&Uuml;')
    	lt = re.compile(r'\&lt;')
    	gt = re.compile(r'\&gt;')
    	amp = re.compile(r'\&amp;')
    	middot = re.compile(r'\&middot;')
    	ampersand = re.compile(r'\&')
    
    	# substitute tags
    	corpus = tagPattern.sub('', corpus)
    	corpus = tagStart.sub('', corpus)
    	corpus = tagEnd.sub('', corpus)
    	corpus = blankSpace.sub(' ', corpus)
    	corpus = ss.sub('ss', corpus)
    	corpus = ae.sub('ae', corpus)
    	corpus = oe.sub('oe', corpus)
    	corpus = ue.sub('ue', corpus)
    	corpus = AE.sub('Ae', corpus)
    	corpus = OE.sub('Oe', corpus)
    	corpus = UE.sub('Ue', corpus)
    	corpus = lt.sub('', corpus)
    	corpus = gt.sub('', corpus)
    	corpus = amp.sub('', corpus)
    	corpus = middot.sub('', corpus)
    	corpus = ampersand.sub('', corpus)
    
    	# return stripped corpus
    	return corpus
