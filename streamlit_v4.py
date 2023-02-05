import streamlit as st
import pandas as pd
from vino_scripts.interface.main import import_df, pred, filter_flavor, filter_color, filter_region, filter_one, filter_color_region, filter_flavor_region, filter_flavor_color, filter_flavor_color_region, filter_three_color_region

# little title
st.markdown('Streamlit Vino Demo 4.1.1')

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
    'What are your favorite wine flavors?',
      options=list(flavor['labels']), # convert to list
      default=['Fruity'])


# Color filter

with col2:

    color = pd.DataFrame({'labels':['Red', 'White', 'Ruby', 'White', 'Rosé', 'Gold']})
    colorSelect = st.multiselect(
    'Preference for a wine color?',
      options=list(color['labels']), # convert to list
      default=['Red'])

# Texture filter

with col3:

    region = pd.DataFrame({'labels':['Western Europe', 'Eastern Europe', 'America', 'Oceania', 'Rest of World']})
    regionSelect = st.multiselect(
    'Preference for a region?',
      options=list(region['labels']), # convert to list
      default=['Western Europe'])

#TEXT INPUT FOR USERS + Search Result Banner
user_input = st.text_input('Can you describe even better the wine you want?', "Type it here")
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

#st.write("Filter content:", flavor_filters, color_filters)




#SEARCH RESULTS (using metrics in streamlit)
if type(prediction) == list:
    col1, col2, col3 = st.columns(3)
    col1.metric("Wine Name", str(df["title"].iloc[0]), "From "+str(df["country"].iloc[0]))
    col2.metric("Similarity %", round((similarity[0]*100), 2), "very confident")
    col3.metric("Wine Description", str(df["variety"].iloc[0]), str(df["description"].iloc[0]))

    col1, col2, col3 = st.columns(3)
    col1.metric("Wine Name", str(df["title"].iloc[1]), "From "+str(df["country"].iloc[1]))
    col2.metric("Similarity %", round((similarity[1]*100), 2), "very confident")
    col3.metric("Wine Description", str(df["variety"].iloc[1]), str(df["description"].iloc[1]))

    col1, col2, col3 = st.columns(3)
    col1.metric("Wine Name", str(df["title"].iloc[2]), "From "+str(df["country"].iloc[2]))
    col2.metric("Similarity %", round((similarity[2]*100), 2), "very confident")
    col3.metric("Wine Description", str(df["variety"].iloc[2]), str(df["description"].iloc[2]))

else:
    col1, col2, col3 = st.columns(3)
    col1.metric("Wine Name", "Waiting for input")
    col2.metric("Matching %", "Waiting for input")
    col3.metric("Wine Description", "Waiting for input")
