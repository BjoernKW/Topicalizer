from stdwn import impl

# get synsets
synsets = impl.lookupSynsetsByForm('camera')

# print
for synset in synsets:
    for item in synset:
	print item
