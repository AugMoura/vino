import pickle
import pandas as pd
from nltk.tokenize import word_tokenize
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from vino_scripts.ml_logic.preprocessor import clean_text
import functools as ft
import pandas as pd

#answer = ""

def import_df():
    """
    Imports the dataset
    """
    df = pd.read_csv("../vino/datasets/clean_dataset_v3.csv")

    return df


def pred(answer: str):
    """
    Runs predictive model based on the entire dataset
    """
    model_imported = pickle.load(open('../vino/notebooks/model_v1.pkl','rb'))
    clean_answer = word_tokenize(clean_text(answer))
    #answer_doc2vec_v1 = str(input("Describe the type of wine you're looking for (the more details, the better): "))
    #clean_answer = word_tokenize(clean_text(answer_doc2vec_v1))
    test_doc_vector_v1 = model_imported.infer_vector(clean_answer)

    idx = []
    idx_sim = []

    for i, row in enumerate(model_imported.dv.most_similar(positive = [test_doc_vector_v1], topn=10000)):
        idx.append(row[0])
        idx_sim.append(row[1])

    return idx, idx_sim


def filter_flavor(df, *args):
    """
    Filters dataset as per flavors selected in the frontend
    """
    dfs = []
    for col in args[0]:
        df_subset = df[df[col] != "0"].reset_index(drop=True)
        df_subset = df_subset[['title',
                               'description',
                               'clean_description_2',
                               'country',
                               'variety',
                               'Red',
                               'Ruby',
                               'White',
                               'Rosé',
                               'Gold',
                               'Western Europe',
                               'Eastern Europe',
                               'America',
                               'Oceania',
                               'Rest of World',
                               col]]
        dfs.append(df_subset)

    df_final = ft.reduce(lambda left, right: pd.merge(left, right, how = "outer"), dfs)
    return df_final.drop_duplicates().reset_index(drop=True)


def filter_color(df, *args):
    """
    Filters dataset as per flavors selected in the frontend
    """
    dfs = []
    for col in args[0]:
        df_subset = df[df[col] != "0"].reset_index(drop=True)
        df_subset = df_subset[['title',
                               'description',
                               'clean_description_2',
                               'country',
                               'variety',
                               'Western Europe',
                               'Eastern Europe',
                               'America',
                               'Oceania',
                               'Rest of World',
                               col]]
        dfs.append(df_subset)

    df_final = ft.reduce(lambda left, right: pd.merge(left, right, how = "outer"), dfs)
    return df_final.drop_duplicates().reset_index(drop=True)


def filter_region(df, *args):
    """
    Filters dataset as per flavors selected in the frontend
    """
    dfs = []
    for col in args[0]:
        df_subset = df[df[col] != "0"].reset_index(drop=True)
        df_subset = df_subset[['title',
                               'description',
                               'clean_description_2',
                               'country',
                               'variety']]

        dfs.append(df_subset)

    df_final = ft.reduce(lambda left, right: pd.merge(left, right, how = "outer"), dfs)
    return df_final.drop_duplicates().reset_index(drop=True)







def filter_one(df, *args):
    #print(args[0])

    dfs = []
    for col in args[0]:
        # print('='*50, col, '='*50)
        df_subset = df[df[col] != "0"].reset_index(drop=True)
        df_subset = df_subset[['title',
                               'description',
                               'clean_description_2',
                               'country',
                               'variety',
                               'designation',
                               'province',
                               col]]
        # print(df_subset)
        dfs.append(df_subset)

    df_final = ft.reduce(lambda left, right: pd.merge(left, right, how = "outer"), dfs)
    return df_final.drop_duplicates().reset_index(drop=True)



def filter_color_region(df, *args):
    #print(args[0])

    dfs = []
    for col in args[0]:
        # print('='*50, col, '='*50)
        df_subset = df[df[col] != "0"].reset_index(drop=True)
        df_subset = df_subset[['title',
                               'description',
                               'clean_description_2',
                               'country',
                               'variety',
                               'designation',
                               'province',
                               'America',
                               'Western Europe',
                               'Eastern Europe',
                               'Oceania',
                               'Rest of World',
                               col]]
        # print(df_subset)
        dfs.append(df_subset)

    df_final = ft.reduce(lambda left, right: pd.merge(left, right, how = "outer"), dfs)
    return df_final.drop_duplicates().reset_index(drop=True)


def filter_flavor_region(df, *args):
    #print(args[0])

    dfs = []
    for col in args[0]:
        # print('='*50, col, '='*50)
        df_subset = df[df[col] != "0"].reset_index(drop=True)
        df_subset = df_subset[['title',
                               'description',
                               'clean_description_2',
                               'country',
                               'variety',
                               'designation',
                               'province',
                               'America',
                               'Western Europe',
                               'Eastern Europe',
                               'Oceania',
                               'Rest of World',
                               col]]
        # print(df_subset)
        dfs.append(df_subset)

    df_final = ft.reduce(lambda left, right: pd.merge(left, right, how = "outer"), dfs)
    return df_final.drop_duplicates().reset_index(drop=True)


def filter_flavor_color(df, *args):
    #print(args[0])

    dfs = []
    for col in args[0]:
        # print('='*50, col, '='*50)
        df_subset = df[df[col] != "0"].reset_index(drop=True)
        df_subset = df_subset[['title',
                               'description',
                               'clean_description_2',
                               'country',
                               'variety',
                               'designation',
                               'province',
                               'Red',
                               'Ruby',
                               'White',
                               'Gold',
                               'Rosé',
                               col]]
        # print(df_subset)
        dfs.append(df_subset)

    df_final = ft.reduce(lambda left, right: pd.merge(left, right, how = "outer"), dfs)
    return df_final.drop_duplicates().reset_index(drop=True)


def filter_flavor_color_region(df, *args):
    #print(args[0])

    dfs = []
    for col in args[0]:
        # print('='*50, col, '='*50)
        df_subset = df[df[col] != "0"].reset_index(drop=True)
        df_subset = df_subset[['title',
                               'description',
                               'clean_description_2',
                               'country',
                               'variety',
                               'designation',
                               'province',
                               'Red',
                               'Ruby',
                               'White',
                               'Gold',
                               'Rosé',
                               'America',
                               'Western Europe',
                               'Eastern Europe',
                               'Oceania',
                               'Rest of World',
                               col]]
        # print(df_subset)
        dfs.append(df_subset)

    df_final = ft.reduce(lambda left, right: pd.merge(left, right, how = "outer"), dfs)
    return df_final.drop_duplicates().reset_index(drop=True)


def filter_three_color_region(df, *args):
    #print(args[0])

    dfs = []
    for col in args[0]:
        # print('='*50, col, '='*50)
        df_subset = df[df[col] != "0"].reset_index(drop=True)
        df_subset = df_subset[['title',
                               'description',
                               'clean_description_2',
                               'country',
                               'variety',
                               'designation',
                               'province',
                               'America',
                               'Western Europe',
                               'Eastern Europe',
                               'Oceania',
                               'Rest of World',
                               col]]
        # print(df_subset)
        dfs.append(df_subset)

    df_final = ft.reduce(lambda left, right: pd.merge(left, right, how = "outer"), dfs)
    return df_final.drop_duplicates().reset_index(drop=True)
