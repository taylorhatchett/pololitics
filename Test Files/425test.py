import csv
import re

def col_selector(table, column_key):
    return [row[column_key] for now in table]

with open("csvJokes.csv","r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    table = [row for row in reader]
    foo_col = col_selector(table, "JOKE")
    bar_col = col_selector(table, "jokeID")
