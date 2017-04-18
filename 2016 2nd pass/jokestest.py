from monkeylearn import MonkeyLearn
import csv

ml = MonkeyLearn('18fd81bba9c8c872dc0c0cb4d336df78fc50927c')
with open('/Users/thatchett/Dropbox/Jokes Analysis/2016 2nd pass/onecolumnjokes.csv', 'r') as f:
  reader = csv.reader(f)
  list = list(reader)
module_id = 'ex_isnnZRbS'
res = ml.extractors.extract(module_id, list)
