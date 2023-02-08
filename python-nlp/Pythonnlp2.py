import spacy
#nlp = spacy.cli.download("en_core_web_md")
nlp = spacy.load('en_core_web_md')
import os

workingDir = os.getcwd()
print("current working directory: " + workingDir)

insideDir = os.listdir(workingDir)
print("inside this directory are the following files AND directories: " + str(insideDir))

CollPath = os.path.join(workingDir, 'txt-files')
print(CollPath)

for file in os.listdir(CollPath):
    if file.endswith(".txt"):
        filepath = f"{CollPath}/{file}"
        print(filepath)
        #readTextFiles(filepath)