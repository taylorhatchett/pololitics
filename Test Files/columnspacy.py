import spacy
import pandas as pd

df = pd.read_csv('csvJokes.csv', encoding = 'latin1')
df['JOKE']

nlp = spacy.load('en_core_web_sm')
df['Parsed'] = df['JOKE'].apply(nlp)



'''for parsed_doc in nlp.pipe(iter(df['JOKE']), batch_size=1, n_threads=4):
    print (parsed_doc[0].text, parsed_doc[0].tag_)
'''
