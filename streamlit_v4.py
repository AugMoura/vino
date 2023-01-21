import streamlit as st
import pandas as pd
from vino_scripts.interface.main import import_df, pred

# little title
st.markdown('Streamlit Vino Demo 4.1.1')

# Main Title
st.title('Vino - Wine Finder')

# Subtitle
st.header('What wine do you like?')

prediction = None

# Filter-based recommender
col1, col2, col3 = st.columns(3)

# Flavor filter

with col1:

    flavor = pd.DataFrame({'labels':['Apple','Pineapple','Cherry']})
    flavorSelect = st.multiselect(
    'What are your favorite wine flavors?',
      options=list(flavor['labels']), # convert to list
      default=['Cherry'])

# Color filter

with col2:

    color = pd.DataFrame({'labels':['Ruby','Purple','Garnet','Salmon','Amber','Gold','Yellow']})
    colorSelect = st.multiselect(
    'Preference for a wine color?',
      options=list(color['labels']), # convert to list
      default=['Ruby'])

# Texture filter

with col3:

    origin = pd.DataFrame({'labels':['France','Italy','Spain','Australia','United States','New Zeland']})
    originSelect = st.multiselect(
    'Preference for a wine texture?',
      options=list(origin['labels']), # convert to list
      default=['France'])

#TEXT INPUT FOR USERS + Search Result Banner
user_input = st.text_input('Can you describe even better the wine you want?', "Type it here")
answer = user_input
st.write('You searched:', answer)

#Work on the output area, the input will be 'user_input'
df = import_df()
prediction, similarity = pred(df, answer)

#SEARCH RESULTS (using metrics in streamlit)
if type(prediction) == pd.DataFrame:
    col1, col2, col3 = st.columns(3)
    col1.metric("Wine Name", str(prediction["title"].iloc[0]), "From "+str(prediction["country"].iloc[0]))
    col2.metric("Similarity %", round((similarity[0]*100), 2), "very confident")
    col3.metric("Wine Description", str(prediction["variety"].iloc[0]), str(prediction["description"].iloc[0]))

    col1, col2, col3 = st.columns(3)
    col1.metric("Wine Name", str(prediction["title"].iloc[1]), "From "+str(prediction["country"].iloc[1]))
    col2.metric("Similarity %", round((similarity[1]*100), 2), "very confident")
    col3.metric("Wine Description", str(prediction["variety"].iloc[1]), str(prediction["description"].iloc[1]))

    col1, col2, col3 = st.columns(3)
    col1.metric("Wine Name", str(prediction["title"].iloc[2]), "From "+str(prediction["country"].iloc[2]))
    col2.metric("Similarity %", round((similarity[2]*100), 2), "very confident")
    col3.metric("Wine Description", str(prediction["variety"].iloc[2]), str(prediction["description"].iloc[2]))

else:
    col1, col2, col3 = st.columns(3)
    col1.metric("Wine Name", "Waiting for input")
    col2.metric("Matching %", "Waiting for input")
    col3.metric("Wine Description", "Waiting for input")
