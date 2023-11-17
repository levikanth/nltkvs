import nltk
# nltk.download('stopwords')
# nltk.download('word_tokenize')

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

# Create a dictionary representation of the documents
dictionary = corpora.Dictionary(filtered_documents)

# Create a corpus (bag of words representation)
corpus = [dictionary.doc2bow(doc) for doc in filtered_documents]

# Train the LDA model
lda_model = gensim.models.LdaModel(
    corpus, num_topics=3, id2word=dictionary, passes=15)

# Print the topics and their corresponding words
for topic_id, topic in lda_model.print_topics():
    print(f'Topic {topic_id + 1}: {topic}\n')






# from gensim.summarization import keywords
# import warnings

# # Sample text
# text = """
# Natural Language Processing (NLP) is a field of AI that focuses on enabling computers to understand, 
# interpret, and generate human language. It involves various techniques and methods for text analysis 
# and understanding. NLP applications include machine translation, sentiment analysis, and text summarization.
# """

# # Suppress warnings for simplicity
# warnings.filterwarnings("ignore")

# # Extract keywords using TextRank algorithm from Gensim
# kw = keywords(text)
# print("Keywords using TextRank (Gensim):")
# print(kw)