import streamlit as st
import pandas as pd
import numpy as np
import string
import pickle
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# markdown
st.markdown('Streamlit Vin Demo 1.1.1')

# 设置网页标题
st.title('Vino - Wine Finder')

# 展示一级标题
st.header('What wine do you like?')

#txt = st.text_area('Describe the wine you like, as if discusing to a friend! Example: "I like sweet sparkling wines, specialy when paired with fruity deserts"', '''
#    I like sweet sparkling wines, specialy when paired with fruity deserts
#    ''')
#st.success("search completed")

#df = pd.read_csv("../datasets/winemag-data-130k-v2.csv")
#df_clean_description = pd.read_csv("../datasets/clean_description.csv")
#df_clean_description = df_clean_description.drop(columns="Unnamed: 0")
#df.index = df_clean_description.index
#df = pd.concat([df, df_clean_description], axis=1)

def clean_text(text):
    '''
    Preprocesses text
    '''
    text = text.strip()

    text = text.lower()

    for punct in string.punctuation:
        text = text.replace(punct, "")

    text = "".join(char for char in text if not char.isdigit())

    english_sw = stopwords.words("english")
    english_sw.append('wine')
    tokenized = word_tokenize(text)

    text = " ".join(word for word in tokenized if word not in english_sw)

    lemmatizer = WordNetLemmatizer()
    tokenized = word_tokenize(text)
    lemma_verb = [lemmatizer.lemmatize(word, pos="v") for word in tokenized]
    lemma_noun = [lemmatizer.lemmatize(word, pos="n") for word in lemma_verb]

    text = " ".join(word for word in lemma_noun)

    return text
#df["clean_description"] = df["clean_description"].apply(clean_text)

user_input = st.text_input('user input', "type here what you like")
answer = user_input+"_answer"
st.write('you searched', answer)

#Work on the output area, the input will be 'user_input'

col1, col2, col3 = st.columns(3)
col1.metric("Wine Name", "Lacoste", "France")
col2.metric("Matching %", "90%", "very confident")
col3.metric("Wine Type", "Bordeaux", "Red")

#model_imported = pickle.load(open('model_v1.pkl','rb'))
#clean_answer = word_tokenize(clean_text(question))
#test_doc_vector_v1 = model_imported.infer_vector(clean_answer)
#idx = []
#for i, row in enumerate(model_imported.dv.most_similar(positive = [test_doc_vector_v1])[:5]):
#    idx.append(row[0])
#idx
#df.iloc[idx]
