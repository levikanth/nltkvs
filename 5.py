import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# Sample documents
documents = [
    "Machine learning is a subfield of artificial intelligence.",
    "Natural language processing is a branch of AI.",
    "Topic modeling is an unsupervised learning technique.",
    "NLTK is a popular library for NLP in Python.",
    "Latent Dirichlet Allocation is used for topic modeling."
]

# Step 1: Preprocess the documents
nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha()]
    return ' '.join(tokens)

preprocessed_documents = [preprocess(doc) for doc in documents]

# Step 2: Convert text data to a matrix of token counts
vectorizer = CountVectorizer(stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(preprocessed_documents)

# Step 3: Apply Latent Dirichlet Allocation (LDA)
lda = LatentDirichletAllocation(n_components=2, random_state=42)
lda.fit(X)

# Step 4: Print the top words for each topic
feature_names = vectorizer.get_feature_names_out()
for topic_idx, topic in enumerate(lda.components_):
    print(f"Topic #{topic_idx+1}:")
    top_words_indices = topic.argsort()[:-10-1:-1]  # Top 10 words
    top_words = [feature_names[i] for i in top_words_indices]
    print(', '.join(top_words))
    print("\n")
