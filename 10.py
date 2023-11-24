#    understand dictionary
# gensim,lda,

from gensim.corpora import Dictionary

# Sample document
document = ["apple", "banana", "apple", "orange", "apple", "orange"]

# Create a Dictionary (mapping words to unique IDs)
dictionary = Dictionary([document])
print(dictionary)

# Convert document to bag-of-words format
bow_corpus = [dictionary.doc2bow(document)]

print(bow_corpus)
