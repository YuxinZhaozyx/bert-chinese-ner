import pandas as pd 
import codecs
import re

train_df = pd.read_csv("./data/Train_Data.csv")
test_df = pd.read_csv("./data/Test_Data.csv")

train_df = train_df[~train_df['unknownEntities'].isnull()]

print(train_df)

with codecs.open('./data/train.txt', 'w', encoding='utf-8') as up:
    for row in train_df.iloc[:-200].itertuples():
        text_label = row.text
        entities = str(row.unknownEntities).split(';')
        for entity in entities:
            text_label = text_label.replace(entity, 'Ё' + (len(entity) - 1) * 'Ж')

        for c1, c2 in zip(row.text, text_label):
            if c2 == 'Ё':
                up.write('{0} {1}\n'.format(c1, 'B-ORG'))
            elif c2 == 'Ж':
                up.write('{0} {1}\n'.format(c1, 'I-ORG'))
            else:
                up.write('{0} {1}\n'.format(c1, 'O'))

        up.write('\n')


with codecs.open('./data/dev.txt', 'w', encoding='utf-8') as up:
    for row in train_df.iloc[-200:].itertuples():
        text_label = row.text
        entities = str(row.unknownEntities).split(';')
        for entity in entities:
            text_label = text_label.replace(entity, 'Ё' + (len(entity) - 1) * 'Ж')

        for c1, c2 in zip(row.text, text_label):
            if c2 == 'Ё':
                up.write('{0} {1}\n'.format(c1, 'B-ORG'))
            elif c2 == 'Ж':
                up.write('{0} {1}\n'.format(c1, 'I-ORG'))
            else:
                up.write('{0} {1}\n'.format(c1, 'O'))

        up.write('\n')

with codecs.open('./data/test.txt', 'w', encoding='utf-8') as up:
    for row in test_df.iloc[:].itertuples():
        text_label = row.text
        for c1 in row.text:
            up.write('{0} {1}\n'.format(c1, 'O'))
        
        up.write('\n')