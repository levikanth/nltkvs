
from sklearn.feature_extraction.text import TfidfVectorizer
# BAG OF WORDS

from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
documents = [
    "I love programming programming",
    "Programming is fun",
    "NLP is interesting"
]

# Create a CountVectorizer instance
vectorizer = CountVectorizer()

# Fit and transform the documents to obtain the BoW representation
X = vectorizer.fit_transform(documents)

# Get the feature names (words)
feature_names = vectorizer.get_feature_names_out()

# Convert the BoW matrix to an array for easier visualization
bow_array = X.toarray()

# Display the BoW representation
print("Bag-of-Words Representation:")
print(feature_names)
print(bow_array)
# In this example, CountVectorizer is used to convert a collection of text documents to a matrix of token counts. The resulting matrix represents the frequency of words in the documents.

# BINARY TERM FREQUENCY


# Sample documents
documents = [
    "I love  programming programming",
    "Programming is fun",
    "NLP is interesting"
]

# Create a CountVectorizer instance with binary=True
vectorizer = CountVectorizer(binary=True)

# Fit and transform the documents to obtain the Binary Term Frequency representation
X_binary = vectorizer.fit_transform(documents)

# Get the feature names (words)
feature_names = vectorizer.get_feature_names_out()

# Convert the Binary Term Frequency matrix to an array for easier visualization
btf_array = X_binary.toarray()

# Display the Binary Term Frequency representation
print("Binary Term Frequency Representation:")
print(feature_names)
print(btf_array)

# term frequency


# Sample documents
documents = [
    "I love programming programming",
    "Programming is fun",
    "NLP is interesting"
]

# Create a CountVectorizer instance
vectorizer = CountVectorizer()

# Fit and transform the documents to obtain the Term Frequency representation
X_tf = vectorizer.fit_transform(documents)

# Get the feature names (words)
feature_names = vectorizer.get_feature_names_out()

# Convert the Term Frequency matrix to an array for easier visualization
tf_array = X_tf.toarray()

# Display the Term Frequency representation
print("Term Frequency (TF) Representation:")
print(feature_names)
print(tf_array)

# TF-IDF


# Sample documents
documents = [
    "I love PROGRAMMING programming",
    "Programming  is fun",
    "NLP is interesting"
]

# Create a TF-IDF Vectorizer instance
vectorizer = TfidfVectorizer()

# Fit and transform the documents to obtain the TF-IDF representation
X_tfidf = vectorizer.fit_transform(documents)

# Get the feature names (words)
feature_names = vectorizer.get_feature_names_out()

# Convert the TF-IDF matrix to an array for easier visualization
tfidf_array = X_tfidf.toarray()

# Display the TF-IDF representation
print("TF-IDF Representation:")
print(feature_names)
print(tfidf_array)
