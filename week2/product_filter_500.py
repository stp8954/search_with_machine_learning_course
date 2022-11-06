import pandas as pd
import os
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
general = parser.add_argument_group("general")
general.add_argument("--input", help="input file")
general.add_argument("--output", help="output file")

args = parser.parse_args()

rows = []
with open(args.input, 'r') as file:
    for line in file:
        cols = line.split(' ')
        rows.append((cols[0], ' '.join(cols[1:])))


df = pd.DataFrame(rows, columns=['label','text'])
counts = df.groupby('label',  as_index=False).count()
candidates = counts[counts['text'] >= 500]
data = pd.merge(df, candidates['label'], on= ['label'])

with open(args.output,'w') as out:
    for _ , row in data.iterrows():
        out.write('{} {}'.format(row['label'], row['text']))
