import spacy
#nlp = spacy.cli.download("en_core_web_md")
nlp = spacy.load('en_core_web_md')

import os

workingDir = os.getcwd()
print("current working directory: " + workingDir)

insideDir = os.listdir(workingDir)
print("inside this directory are the following files AND directories: " + str(insideDir))

CollPath = os.path.join(workingDir, 'textCollection')
print(CollPath)

def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        readFile = f.read()


        stringFile = str(readFile)
        lengthFile = len(readFile)
        print(lengthFile)

        tokens = nlp(stringFile)
        vectors = tokens.vector


        wordOfInterest = nlp(u'cole')

        highSimilarityDict = {}
        for token in tokens:
            if (token and token.vector_norm):

                if wordOfInterest.similarity(token) > .3:
                    highSimilarityDict[token] = wordOfInterest.similarity(token)
        print("This is a dictionary of words most similar to the word " + wordOfInterest.text + " in this file.")

        highSimilarityReduced = {}
        for key, value in highSimilarityDict.items():
            if value not in highSimilarityReduced.values():
                highSimilarityReduced[key] = value
        print(highSimilarityReduced)
        print(len(highSimilarityReduced.items()), " vs ", len(highSimilarityDict.items()))

#for file in os.listdir(CollPath):
    if file.endswith(".txt"):
        filepath = f"{CollPath}/{file}"
        print(filepath)
        readTextFiles(filepath)


