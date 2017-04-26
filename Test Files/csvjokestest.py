import spacy
import csv

nlp = spacy.load('en_core_web_sm')

jokefile = csv.reader(open('csvJokes.csv','rb'), delimiter=',', quotechar='"')
joke_decode = jokefile.decode('utf-8')
