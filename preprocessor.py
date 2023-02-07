import string
import nltk
import nltkmodules
#from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
#from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


def clean_text(text):
    '''
    Preprocesses text. It can be used for cleaning all descriptions
    or to clean answers from users in the frontend
    '''
    text = text.strip()

    text = text.lower()

    for punct in string.punctuation:
        text = text.replace(punct, "")

    text = "".join(char for char in text if not char.isdigit())

    english_sw = nltk.corpus.stopwords.words("english")
    english_sw.append('wine')
    tokenized = nltk.tokenize.word_tokenize(text)

    text = " ".join(word for word in tokenized if word not in english_sw)

    lemmatizer = nltk.stem.WordNetLemmatizer()
    tokenized = nltk.tokenize.word_tokenize(text)
    lemma_verb = [lemmatizer.lemmatize(word, pos="v") for word in tokenized]
    lemma_noun = [lemmatizer.lemmatize(word, pos="n") for word in lemma_verb]

    text = " ".join(word for word in lemma_noun)

    return text
