from gensim.summarization import keywords
import warnings

# Sample text
text = """
Natural Language Processing (NLP) is a field of AI that focuses on enabling computers to understand, 
interpret, and generate human language. It involves various techniques and methods for text analysis 
and understanding. NLP applications include machine translation, sentiment analysis, and text summarization.
"""

# Suppress warnings for simplicity
warnings.filterwarnings("ignore")

# Extract keywords using TextRank algorithm from Gensim
kw = keywords(text)
print("Keywords using TextRank (Gensim):")
print(kw)