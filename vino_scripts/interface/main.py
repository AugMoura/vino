import pickle
import pandas as pd
from nltk.tokenize import word_tokenize
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from vino_scripts.ml_logic.preprocessor import clean_text

answer = ""

def import_df():
    df = pd.read_csv("../vino/datasets/clean_dataset.csv")

    return df

def pred(df: pd.DataFrame, answer):
    model_imported = pickle.load(open('../vino/notebooks/model_v1.pkl','rb'))
    clean_answer = word_tokenize(clean_text(answer))
    #answer_doc2vec_v1 = str(input("Describe the type of wine you're looking for (the more details, the better): "))
    #clean_answer = word_tokenize(clean_text(answer_doc2vec_v1))
    test_doc_vector_v1 = model_imported.infer_vector(clean_answer)

    idx = []
    idx_sim = []

    for i, row in enumerate(model_imported.dv.most_similar(positive = [test_doc_vector_v1])[:5]):
        idx.append(row[0])
        idx_sim.append(row[1])

    return df[["title", "country", "description", "price", "variety"]].iloc[idx], idx_sim

#print(pred(df))
