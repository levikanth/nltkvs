
#Sentiment Analysis , Lemmatization and Stemming in NLTK
import nltk
# nltk.download('wordnet')
# nltk.download('vader_lexicon')

demowords = ['playing','doing','cried', 'smile','ran','have','sang','tied','jumped','code']



#              ***import Stemming,SentimentAnalysis and lemmitizition ***
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
stemmer = PorterStemmer()
Lemmatizer= WordNetLemmatizer()



#               orginalword , stemmedword , Lemmitizedword
for word in demowords:
    print(word, stemmer.stem(word,), Lemmatizer.lemmatize(word,'v'))



#              sentiment analyzer(get the emotion score)

sia=SentimentIntensityAnalyzer()
polarityscore=sia.polarity_scores("NLTK is a great library for natural language processing!")
print(polarityscore)