import streamlit as st
import pandas as pd

# Little title
st. markdown('Streamlit Vino Demo 1.2.0')

# Main Title
st.title('Vino - Wine Finder')

# Subtitle
st.header('What wine do you like?')

# Filter-based recommender
# Flavor filter
flavor = st.selectbox(
    'What is your favorite flavor?',
    ('Apple', 'Pineapple', 'Blackberry'))

st.write('You selected:', flavor)

# Moment filter
moment = st.selectbox(
    'At which moment do you drink the wine?',
    ('Tranquil night', 'Relaxng Weekend', 'Sunny holiday'))

st.write('You selected:', moment)

# Color filter
color = st.selectbox(
    'Which wine color do you like the best?',
    ('Ruby','Purple','Garnet','Salmon','Amber','Gold','Yellow'))

st.write('You selected:', color)
