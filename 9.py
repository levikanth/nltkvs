import nltk
import gensim
from gensim import corpora
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Sample documents
documents = [
    "I love programming. Programming is fun.",
    "Natural language processing is an interesting field.",
    "Python is a popular programming language for data science."
]

# Tokenization and preprocessing
stop_words = set(stopwords.words('english') + list(string.punctuation))
tokenized_documents = [word_tokenize(doc.lower()) for doc in documents]
filtered_documents = [[word for word in doc if word not in stop_words]
                      for doc in tokenized_documents]

# print(f"filtered words: ", filtered_documents)

# Create a dictionary representation of the documents
dictionary = corpora.Dictionary(filtered_documents)
for i in range(0, len(dictionary)):
    print(f" dictionaryy wordds", list[i])
# print(f"dictionary words: ", dictionary)

# Create a corpus (bag of words representation)
corpus = [dictionary.doc2bow(doc) for doc in filtered_documents]
# print(f"corpus words: ", corpus)


# Train the LDA model
lda_model = gensim.models.LdaModel(
    corpus, num_topics=1, id2word=dictionary, passes=0)

# Print the topics and their corresponding words
for topic_id, topic in lda_model.print_topics():
    print(f'Topic {topic_id + 1}: {topic}\n')
