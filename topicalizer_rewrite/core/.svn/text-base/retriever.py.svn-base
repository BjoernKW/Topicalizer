import re

# Stop words class
class StopWords:
    def __init__(self):
    	self.commentPattern = re.compile('\s\|.*')
    	self.commentAtBeginning = re.compile('^\|')
    	self.blankSpaces = re.compile('\s')
    	self.tailingSpaces = re.compile('\s$')

    # get stop word list for language
    def getStopWordList(self, language):
    	# initialise stop word list
    	stopWordList = []
    
    	# open stop word file
    	stopWordFile = open('core/stopwords_utf-8/stop-' + language + '.txt', 'r')
    
    	# iterate over file
    	for line in stopWordFile:
    	    # codify line
    	    # line = unicode(line, 'iso-8859-1', 'replace')
    	    line = unicode(line, 'utf-8', 'replace')
    
    	    # remove comments and empty lines
    	    line = self.commentPattern.sub('', line)
    	    line = self.blankSpaces.sub('', line)
    	    if line == '' or self.commentAtBeginning.findall(line):
        		pass
    	    else:
        		stopWordList.append(line)
    
    	# close stop word file
    	stopWordFile.close()
    
    	# make set of stopWordList
    	stopWordList = set(stopWordList)
    
    	# return stop word list
    	return stopWordList

    # get stop words as string for language
    def getStopWordString(self, language):
    	# initialise stop word string and list
    	stopWords = ''
    	stopWordList = []
    
    	# open stop word file
    	stopWordFile = open('core/stopwords_utf-8/stop-' + language + '.txt', 'r')
    
    	# iterate over file
    	for line in stopWordFile:
    	    # codify line
    	    # line = unicode(line, 'iso-8859-1', 'replace')
    	    line = unicode(line, 'utf-8', 'replace')
    
    	    # remove comments and empty lines
    	    line = self.commentPattern.sub('', line)
    	    line = self.blankSpaces.sub('', line)
    	    if line == '' or self.commentAtBeginning.findall(line):
        		pass
    	    else:
        		stopWordList.append(line)
    
    	# close stop word file
    	stopWordFile.close()
    
    	# join stop words
    	stopWords = ' '.join(stopWordList)
    
    	# remove tailing space
    	stopWords = self.tailingSpaces.sub('', stopWords)
    
    	# return stop word string
    	return stopWords

# URL retriever class
class URLRetriever:
    def __init__(self):
    	self.corpus = ''

    def retrieveURL(self, url):
    	import httplib, codecs, urllib, urllib2, cherrypy, os, datetime
        from topicalizer.model import client

        # get number of requests from current IP address
        today = datetime.datetime.today()
        ip_address = os.environ.get('HTTP_X_FORWARDED_FOR', os.environ.get('REMOTE_ADDR', ''))
        if (ip_address == ''):
            ip_address = cherrypy.request.headerMap.get('Remote-Addr')
        day = str(today.day)
        month = str(today.month)
        year = str(today.year)
        hour = str(today.hour)
        minute = str(today.minute)
        second = str(today.second)
        clients = list(client.select("""client.ip_address='""" + ip_address + \
                                     """' AND DAY(access_time)='""" + day + \
                                     """' AND MONTH(access_time)='""" + month + \
                                     """' AND YEAR(access_time)='""" + year + \
                                     """' AND HOUR(access_time)='""" + hour + """'"""))

        # raise IOException, if too many requests per IP
        if len(clients) > 9:
            raise IOError, 'Error: Too many requests per IP.'
        
        # new client
        client(ip_address = ip_address,
               access_time = year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second)

    	# initialise charset
    	charset = ''
    
    	# compile patterns for prohibiting self-referencing
    	selfReferencingPattern = re.compile('http\:\/\/.*topicalizer\.com')
    
    	# compile patterns for script elements
    	scriptPatterns = re.compile('}$|;$|{$|^\/\/|^\<\!|--\>$')
    
    	# see, if entered value contains http://, if not, prepend it
    	if re.findall(r'http://', url):
    	    pass
    	else:
    	    url = 'http://' + url
    
    	# raise IOException, if malformed URL
    	if selfReferencingPattern.findall(url):
    	    raise IOError, 'Error: Self-referencing attempt.'
    
    	# compile regular expressions for filtering comments, <script>, <style> content etc.
    	filter = re.compile(r'document\.write')
    	invalidTags = re.compile(r'<\/(.*?)\\\\\\>')
    	invalidScriptTags = re.compile(r'<\/SCR\'\ \+\ \'IPT.*')
    
    	# compile regular expression for recognising charset
    	metaTagPattern = re.compile(r'.*\<meta.*', re.I)
    	charsetPattern = re.compile(r'.*charset\=(.*?)\".*', re.I)

        # decode url
        url = urllib.unquote(url)

    	# open and read remote file as corpus
    	request = urllib2.Request(url)
    	request.add_header('User-agent', 'Mozilla/5.0 (compatible; Topicalizer/www.topicalizer.com)')
    	try:
    	    remoteFile = urllib2.urlopen(request)
    	except httplib.InvalidURL:
    	    raise IOError, 'Error: Invalid URL.'
    
    	# process file
    	corpus = ''
    	corpusList = []
    	for line in remoteFile:
    	    # correct invalid tags
    	    line = invalidTags.sub('<\/\1>', line)
    	    line = invalidScriptTags.sub('', line)
    
    	    # remove strings to be filtered
    	    line = filter.sub('', line)
    
    	    # add line to corpus, if it does not contain script elements
    	    if scriptPatterns.findall(line):
        		pass
    	    else:
        		corpusList.append(line)
    
    	    # try to recognise ISO-8859 encoding
    	    if metaTagPattern.search(line) and charsetPattern.search(line):
        		charsetGroups = charsetPattern.match(line)
        		charset = charsetGroups.group(1)
    
    	# close remote file
    	remoteFile.close()
    
    	# join corpus
    	corpus = ''.join(corpusList)
    
    	# set charset
    	if charset != '':
    	    pass
    	else:
    	    charset = 'utf-8'
    
    	# look up codec
    	try:
    	    codecs.lookup(charset)
    	except LookupError:
    	    charset = 'utf-8'
    
    	# codify results
    	corpus = unicode(corpus, charset, 'replace')
    
    	# build return dictionary
    	returnDict = dict(corpus = corpus,
                          charset = charset)
    	
    	# return corpus and charset
    	return returnDict

