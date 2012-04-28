from model import token_by_category, co_occurrence

# text category
textCategory = 'a'

# initialise co-occurrence entity list
coOccurrenceEntities = []

# get token information from database
tokenEntity = token_by_category.select("""token_by_category.token='court' AND token_by_category.category='a'""")

# get five most frequent co-occurences from database
coOccurrenceEntities[:5] = co_occurrence.select("""co_occurrence.co_occurs_with='""" + tokenEntity.id + """'""", orderBy = co_occurrence.q.count).reversed()

# get coOccurrences for each token
for coOccurrenceEntity in coOccurrenceEntities[:5]:
    print coOccurrenceEntity.token
