from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

import matplotlib.pyplot as plt
# nltk.download("stopwords")

text = "One  day a wolf was eating the flesh of an animal it had killed. A little bone got stuck in his throat, and he was unable to swallow it."
# demowords=["playing", "happiness","going", "doing", "yes", "no", "i", "having", "had","haved" ]


#                      get stopwords and set it
Stop_words = set(stopwords.words('english'))
print(Stop_words)


#                    tokinization of text

tokinized_word = word_tokenize(text)
# # print(word_tokenize(text))


#              identify and remove the stopwords in text
#                   (loop with if codition )

Tokinized_words_without_Stop_words = []
for word in tokinized_word:
    if word not in Stop_words:
        Tokinized_words_without_Stop_words.append(word)
print(Tokinized_words_without_Stop_words)


#              Get the removed stop_words from text
# print(set(tokinized_word) - set(Tokinized_words_without_Stop_words))


#               frequency of words in text
fd = FreqDist(Tokinized_words_without_Stop_words)
print(fd.most_common(10))

#               graph for frequency of words in text
fd.plot(30, cumulative=False)
plt.show()


# Sample documents
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Transform the documents into TF-IDF features
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# Get the feature names (words)
feature_names = tfidf_vectorizer.get_feature_names_out()

# Print TF-IDF values
for i, document in enumerate(documents):
    print(f"Document {i+1}:")
    for j, feature in enumerate(feature_names):
        tfidf_value = tfidf_matrix[i, j]
        if tfidf_value > 0:
            print(f"{feature}: {tfidf_value}")
    print("\n")
