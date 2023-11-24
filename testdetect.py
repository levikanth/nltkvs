import nltk

                    # lang detection 

from langdetect import detect
from langdetect import DetectorFactory
DetectorFactory.seed = 0

# Sample texts in different languages
text1 = "Hello, how are you?"
text2 = "Hola, ¿cómo estás?"
text3 = "Bonjour, comment ça va?"


# Detect the language for each text
lang1 = detect(text1)
lang2 = detect(text2)
lang3 = detect(text3)

# Print the detected languages
print(f"Text 1 is in {lang1} language.")
print(f"Text 2 is in {lang2} language.")
print(f"Text 3 is in {lang3} language.")
import nltk
from nltk.corpus import stopwords

# Download NLTK stopwords if not already downloaded
# nltk.download('stopwords')

# Sample text for language detection
text_to_detect = "Bonjour, comment ça va?"

# Tokenize the text and check the presence of stopwords for different languages
words = set(word.lower() for word in nltk.word_tokenize(text_to_detect))
languages = set()
for lang in stopwords.fileids():
    stopwords_set = set(stopwords.words(lang))
    if any(word in stopwords_set for word in words):
        languages.add(lang)

# Display detected languages
print("Detected Languages:", languages)




#         #   using function for lang detection



# from langdetect import detect

# def detect_language(text):
#     try:
#         language = detect(text)
#         return language
#     except Exception as e:
#         print(f"Error during language detection: {e}")
#         return None

# # Sample texts in different languages
# text1 = "Hello, how are you?"
# text2 = "Hola, ¿cómo estás?"
# text3 = "Bonjour, comment ça va?"
# text4= "thinnava ra srujana"

# # Detect language for each text
# lang1 = detect_language(text1)
# lang2 = detect_language(text2)
# lang3 = detect_language(text3)
# lang4 = detect_language(text4)

# # Print the detected languages
# print(f"Text 1 is in {lang1} language.")
# print(f"Text 2 is in {lang2} language.")
# print(f"Text 3 is in {lang3} language.")