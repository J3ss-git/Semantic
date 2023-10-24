#=======Importing========
import spacy
nlp = spacy.load('en_core_web_md')

# Use the next words to find out the similarities between these words
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Printing the similarities between these three words:
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Working with vektors
'''Using two for loops to allow us to undertake a comparison of the words'''
tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

'''What interesting is that monkey and banana has more of similairtity than monkey and apple. And the cat and
the fruits have no significant similarities'''

'''The example file was runned under en_core_web_md and  en_core_web_sm. Diffrence is that en_core_web_sm
didnt do the full function off getting similarities between words as en_core_web_md'''
