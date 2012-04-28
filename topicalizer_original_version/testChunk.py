from nltk_lite.parse import chunk

chunkParser = chunk.RegexpChunk()
print chunkParser.parse(['This', 'is', 'a', 'test'])
