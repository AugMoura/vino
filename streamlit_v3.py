import streamlit as st
import pandas as pd

# Little title
st. markdown('Streamlit Vino Demo 1.2.0')

# Main Title
st.title('Vino - Wine Finder')

# Subtitle
st.header('What wine do you like?')

# Filter-based recommender
col1, col2, col3 = st.columns(3)

# Flavor filter

with col1:

    flavor = pd.DataFrame({'labels':['Apple','Pineapple','Cherry']})
    flavorSelect = st.multiselect(
    'What are your favorite wine flavors',
      options=list(flavor['labels']), # convert to list
      default=['Cherry'])

# Color filter

with col2:

    color = pd.DataFrame({'labels':['Ruby','Purple','Garnet','Salmon','Amber','Gold','Yellow']})
    colorSelect = st.multiselect(
    'What are your favorite wine colors',
      options=list(color['labels']), # convert to list
      default=['Ruby'])

# Origin filter

with col3:

    origin = pd.DataFrame({'labels':['France','Italy','Spain','Australia','United States','New Zeland']})
    originSelect = st.multiselect(
    'What are your favorite wine origins',
      options=list(origin['labels']), # convert to list
      default=['France'])
