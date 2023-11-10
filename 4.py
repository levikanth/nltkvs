import nltk
# nltk.download('wordnet2021')
from nltk.corpus import wordnet


newword="running"
syn= wordnet.synsets(newword)
print('\n')
print("printing synonyms  for word", newword, "\n" ,syn)
print('\n')
print('printing definition for ', newword, '\n' ,syn[0].definition())
print('\n')


                                # synonyms 
synonmys = []

for syn in wordnet.synsets(newword):
    for lemma in syn.lemmas():
       synonmys.append(lemma.name())
print('printing synonmys for', newword ,'\n ',  synonmys)
print('\n')



                                # antonyms
antonyms=[]
for syn in wordnet.synsets(newword):
   for lemma in syn.lemmas():
      if lemma.antonyms():
         antonyms.append(lemma.antonyms()[0].name())
print('\n')        
print('printing antonyms for' ,newword,'\n',antonyms)         
     
     
      
