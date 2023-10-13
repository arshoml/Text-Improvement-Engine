#!/usr/bin/env python
# coding: utf-8

# In[11]:


from transformers import DistilBertTokenizer, DistilBertModel
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk import ngrams
import pandas as pd
import torch

stop_words = set(stopwords.words('english'))

tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained('distilbert-base-uncased')

standardized_phrases = pd.read_csv('Standardised terms.csv', names=['phrases'])
standardized_phrases = standardized_phrases['phrases'].tolist()

def input_text():
    text = ''
    option = input('Choose an option:\n1. Enter text\n2. Open file\n')
    
    if option == '1':
        text = input('Enter the text:\n')

    elif option == '2':
        file_path = input('Enter the file path:\n')
        
        try:
            with open(file_path, 'r') as file:
                text = file.read()
                
        except FileNotFoundError:
            print('File not found.')
            text = input_text()
    else:
        print('Error: You can type only 1 or 2')
        text = input_text()
        
    return text

def get_embeddings(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).detach().numpy()
    return embeddings

standardized_embeddings = [get_embeddings(phrase) for phrase in standardized_phrases]

def analyze_text(text):
    words = [word for word in text.split() if word not in stop_words]
    phrases = [' '.join(grams) for grams in ngrams(words, 2)]
    phrase_embeddings = [get_embeddings(phrase) for phrase in phrases]

    for i, phrase_embedding in enumerate(phrase_embeddings):
        similarities = [cosine_similarity(phrase_embedding, standardized_embedding) for standardized_embedding in standardized_embeddings]

        max_index = similarities.index(max(similarities))

        if similarities[max_index] > 0.85:
            print(f"\nSuggestion: Replace '{phrases[i]}' with '{standardized_phrases[max_index]}' (Similarity: {similarities[max_index][0][0]})")

analyze_text(input_text())

