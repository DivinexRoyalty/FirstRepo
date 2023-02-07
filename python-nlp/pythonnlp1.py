# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import spacy
# Need line 8 the first time: Then comment it out after the first time you run it:
#nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')

MadaraSpeeches = open('Madara.txt', 'r', encoding='utf8')
words = MadaraSpeeches.read()
wordstrings = str(words)
print(wordstrings)

# count=0
# for w in words:
#     count += 1
#     print(count, ": ", w)

MadaraWords = nlp(wordstrings)
for token in MadaraWords:
    if token.pos_ == "NOUN":
        print(token.text, "---->", token.pos_, ":::::", token.lemma_)


# str1 = 'Madaras Speech'
# print(str1)
# str2 = ' Wake up to reality!'
# print(str2)
# str3 = 'Nothing ever goes as planned in this accursed world. '
# print(str3)
# str4 = 'The longer you live, the more you realize that the only things that truly exist in this reality are merely pain, suffering and futility. '
# print(str4)
# str5 = 'Listen, everywhere you look in this world, wherever there is light, there will always be shadows to be found as well. '
# print(str5)
# str6 = 'As long as there is a concept of victors, the vanquished will also exist. The selfish intent of wanting to preserve peace, initiates war and hatred is born in order to protect love. '
# print(str6)
# str7 = 'There are nexuses causal relationships that cannot be separated.'
# print(str7)
# str8 = 'By- Madara Uchiha'
# print(str8)
