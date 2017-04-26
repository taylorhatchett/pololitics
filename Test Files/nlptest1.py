import spacy
import pandas as pd
import numpy as np
nlp = spacy.load('en')

xlspath = 'Jokes - xlsx.xlsx'
texts = pd.read_excel(xlspath, index_col=None, na_values=['NA'], parse_cols = "A")

iter_texts = (texts[i % 3] for i in xrange(100000000))
for i, token in enumerate(nlp.pipe(iter_texts, batch_size=50, n_threads=4)):
    assert doc.is_parsed
    if i == 100:
        break
