from nltk.tokenize import sent_tokenize
import spacy
import xlsxwriter
workbook = xlsxwriter.Workbook('Jokes - xlsx.xlsx')
worksheet = workbook.add_worksheet()
row=0
col=0
nlp = spacy.load('en_core_web_sm')
f=open("cdata.txt").read()
s=sent_tokenize(f)

for sent in sent_tokenize(f):
    worksheet.write(row, col, sent)
    doc=nlp(unicode(sent))
    print(type(doc))
    for tok in doc:
        if tok.dep_=='nsubj':
             print(type(tok))
             worksheet.write(row,col+1,str(tok._orth_))
