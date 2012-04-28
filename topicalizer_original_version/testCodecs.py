import codecs

try:
    codecs.lookup('utf-8')
except LookupError:
    print 'bla'
