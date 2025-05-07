import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import spacy
import joblib

classifier=joblib.load('models/classifier.joblib')

columns=['ID','Entity','Label','Text']
test_df=pd.read_csv('data/twitter_validation.csv',names=columns)
test_df.head()

nlp=spacy.load('en_core_web_sm')

def preprocessing(text):
    doc=nlp(text)
    filter_words=[]
    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        filter_words.append(token.lemma_)
    return " ".join(filter_words)

test_text_processed=test_df['Text'].apply(preprocessing)
test_text_processed

predictions = classifier.predict(test_text_processed)

classes = ['Irrelevant', 'Natural', 'Negative', 'Positive']

print(f"True Label: {test_df['Label'][10]}")
print(f'Predict Label: {classes[predictions[10]]}')