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
st.write('You searched:', user_input)

#Work on the output area, the input will be 'user_input'
df = import_df()
prediction, similarity = pred(user_input)

# LINK TO THE CSS FILE
with open("style.css")as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#SEARCH RESULTS (using metrics in streamlit)
if type(prediction) == list:
    col1, col2, col3, col4= st.columns([3,3,1.5,0.3])
    col1.metric(label="Wine Name", value=str(df["designation"].iloc[prediction[0]]))
    col2.metric(label="Variety", value=str(df["variety"].iloc[prediction[0]]))
    col3.metric(label="Province", value=str(df["province"].iloc[prediction[0]]))
    with col4:
        st.write("""
    \U0001F947
     """)
    with st.expander("Wanna know more details of this wine"):
        st.write(str(df["description"].iloc[prediction[0]]))

    col1, col2, col3,col4 = st.columns([3,3,1.5,0.3])
    col1.metric(label="Wine Name", value=str(df["designation"].iloc[prediction[1]]))
    col2.metric(label="Variety", value=str(df["variety"].iloc[prediction[1]]))
    col3.metric(label="Province", value=str(df["province"].iloc[prediction[1]]))
    with col4:
        st.write("""
    \U0001F948
     """)
    with st.expander("Wanna know more details of this wine"):
        st.write(str(df["description"].iloc[prediction[1]]))

    col1, col2, col3,col4 = st.columns([3,3,1.5,0.3])
    col1.metric(label="Wine Name", value=str(df["designation"].iloc[prediction[2]]))
    col2.metric(label="Variety", value=str(df["variety"].iloc[prediction[2]]))
    col3.metric(label="Province", value=str(df["province"].iloc[prediction[2]]))
    with col4:
        st.write("""
    \U0001F949
     """)
    with st.expander("Wanna know more details of this wine"):
        st.write(str(df["description"].iloc[prediction[2]]))

else:
    col1, col2, col3,col4 = st.columns(4)
    col1.metric("Wine Name", "Waiting for input")
    col2.metric("Variety", "Waiting for input")
    col3.metric("Province", "Waiting for input")
    col4.metric("Wine Recommendation", "Waiting for input")
