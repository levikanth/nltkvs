import nltk
import matplotlib.pyplot as plt
nltk.download()
text="""my  name is levi kanth. i live in hyderabad. i finished my graduation."""

#                         #class -1

#word_tokenization(sentences into words)

from nltk.tokenize import word_tokenize
print(word_tokenize(text))
 


# #sent_tokenization[[paragraphs into sentences],[in array form]]

from nltk.tokenize import sent_tokenize
print(sent_tokenize(text))


# FreqDist()graph of Number of times/Frequency of words in a sentence or para

# from nltk.probability  import FreqDist
# fd=FreqDist(word_tokenized)
# print(fd.most_common(15))
# fd.plot(30, cumulative=False)
# plt.show()




