import streamlit as st
import pandas as pd
from vino_scripts.interface.main import import_df, pred, filter_one, filter_color_region, filter_flavor_region, filter_flavor_color, filter_flavor_color_region, filter_three_color_region

# little title
st.markdown('Streamlit Vino Demo 6.1.1')

# Main Title
st.title('Vino - Wine Finder')

# Subtitle
st.header('What wine do you like?')

prediction = None
df = import_df()

# Filter-based recommender
col1, col2, col3 = st.columns(3)

# Flavor filter

with col1:

    flavor = pd.DataFrame({'labels':['Fruity', 'Earthy', 'Floral', 'Sweet', 'Herbal', 'Meaty', 'Coffee', 'Mineral', 'Oaky', 'Spicy']})
    flavorSelect = st.multiselect(
    'Preference for flavor? (Select 1)',
      options=list(flavor['labels']), # convert to list
      default=['Fruity'])

# Color filter

with col2:

    color = pd.DataFrame({'labels':['Red', 'White', 'Ruby', 'White', 'Rosé', 'Gold']})
    colorSelect = st.multiselect(
    'Preference for color? (Select 1)',
      options=list(color['labels']), # convert to list
      default=['Red'])

# Texture filter

with col3:

    region = pd.DataFrame({'labels':['Western Europe', 'Eastern Europe', 'America', 'Oceania', 'Rest of World']})
    regionSelect = st.multiselect(
    'Preference for region? (Select 1)',
      options=list(region['labels']), # convert to list
      default=['Western Europe'])

#TEXT INPUT FOR USERS + Search Result Banner
user_input = st.text_input('Not enough? Let us know more about the wine you are looking for:', "Type it here")
st.write('You searched:', user_input)

#Work on the output area, the input will be 'user_input'
prediction, similarity = pred(user_input)

#Control flow
flavor_filters = flavorSelect
color_filters = colorSelect
region_filters = regionSelect

if flavor_filters == [] and color_filters == [] and region_filters == [] and user_input == "":
    df = df
elif flavor_filters == [] and color_filters == [] and region_filters == [] and user_input != "":
    df = df.iloc[prediction]
elif flavor_filters == [] and color_filters == [] and region_filters != [] and user_input != "":
    df = filter_one(df.iloc[prediction], region_filters)
elif flavor_filters == [] and color_filters != [] and region_filters == [] and user_input != "":
    df = filter_one(df.iloc[prediction], color_filters)
elif flavor_filters != [] and color_filters == [] and region_filters == [] and user_input != "":
    df = filter_one(df.iloc[prediction], flavor_filters)
elif flavor_filters == [] and color_filters != [] and region_filters != [] and user_input != "":
    df = filter_color_region(df.iloc[prediction], color_filters)
    df = filter_one(df, region_filters)
elif flavor_filters != [] and color_filters == [] and region_filters != [] and user_input != "":
    df = filter_flavor_region(df.iloc[prediction], flavor_filters)
    df = filter_one(df, region_filters)
elif flavor_filters != [] and color_filters != [] and region_filters == [] and user_input != "":
    df = filter_flavor_color(df.iloc[prediction], flavor_filters)
    df = filter_one(df, color_filters)
elif flavor_filters != [] and color_filters != [] and region_filters != [] and user_input != "":
    df = filter_flavor_color_region(df.iloc[prediction], flavor_filters)
    df = filter_three_color_region(df, color_filters)
    df = filter_one(df, region_filters)
elif flavor_filters != [] and color_filters != [] and region_filters != [] and user_input == "":
    df = filter_flavor_color_region(df, flavor_filters)
    df = filter_three_color_region(df, color_filters)
    df = filter_one(df, region_filters)
elif flavor_filters != [] and color_filters != [] and region_filters == [] and user_input == "":
    df = filter_flavor_color(df, flavor_filters)
    df = filter_one(df, color_filters)
elif flavor_filters != [] and color_filters == [] and region_filters != [] and user_input == "":
    df = filter_flavor_region(df, flavor_filters)
    df = filter_one(df, region_filters)
elif flavor_filters == [] and color_filters != [] and region_filters != [] and user_input == "":
    df = filter_color_region(df, color_filters)
    df = filter_one(df, region_filters)
elif flavor_filters == [] and color_filters == [] and region_filters != [] and user_input == "":
    df = filter_one(df, region_filters)
elif flavor_filters == [] and color_filters != [] and region_filters == [] and user_input == "":
    df = filter_one(df, color_filters)
elif flavor_filters != [] and color_filters == [] and region_filters == [] and user_input == "":
    df = filter_one(df, flavor_filters)
else:
    df = df

# LINK TO THE CSS FILE
with open("style.css")as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#SEARCH RESULTS (using metrics in streamlit)
if type(prediction) == list:
    col1, col2, col3, col4= st.columns([3,3,1.5,0.3])
    col1.metric(label="Wine Name", value=str(df["designation"].iloc[0]))
    col2.metric(label="Variety", value=str(df["variety"].iloc[0]))
    col3.metric(label="Province", value=str(df["province"].iloc[0]))
    with col4:
        st.write("""
    \U0001F947
     """)
    with st.expander("Wanna know more details of this wine"):
        st.write(str(df["description"].iloc[0]))

    col1, col2, col3,col4 = st.columns([3,3,1.5,0.3])
    col1.metric(label="Wine Name", value=str(df["designation"].iloc[1]))
    col2.metric(label="Variety", value=str(df["variety"].iloc[1]))
    col3.metric(label="Province", value=str(df["province"].iloc[1]))
    with col4:
        st.write("""
    \U0001F948
     """)
    with st.expander("Wanna know more details of this wine"):
        st.write(str(df["description"].iloc[1]))

    col1, col2, col3,col4 = st.columns([3,3,1.5,0.3])
    col1.metric(label="Wine Name", value=str(df["designation"].iloc[2]))
    col2.metric(label="Variety", value=str(df["variety"].iloc[2]))
    col3.metric(label="Province", value=str(df["province"].iloc[2]))
    with col4:
        st.write("""
    \U0001F949
     """)
    with st.expander("Wanna know more details of this wine"):
        st.write(str(df["description"].iloc[2]))

else:
    col1, col2, col3,col4 = st.columns(4)
    col1.metric("Wine Name", "Waiting for input")
    col2.metric("Variety", "Waiting for input")
    col3.metric("Province", "Waiting for input")
    col4.metric("Wine Recommendation", "Waiting for input")
