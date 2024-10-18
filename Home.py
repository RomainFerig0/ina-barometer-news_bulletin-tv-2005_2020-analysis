#%% Imports
import streamlit as st

#%%

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

st.sidebar.markdown("""
                    Welcome to this dashboard !
                    """)
st.sidebar.success("Select a section above.")


st.markdown(
    """
# Dashboard : Analysis of the INA Thematic Barometer for French News Bulletins (2005 - 2020)

## Project description

This dashboard hosts a complete collection of both linear, detailed insight and interactive visualizations
on the subject of news coverage along 6 french news channels, between the years 2005 and 2020.
Given the size of the data and the many details and information hidden inside the dataset,
we wish here to not only to provide an in-depth analysis of the data, but also give an opportunity for
the users to test their own analysis skills.

## About the data

The data was extracted from the French government's official [data.gouv.fr](https://www.data.gouv.fr) website, and
pre-processed by our means in order to make the data readable by data analysis programs.  
"""
)

st.image("logo-social.png")

st.markdown("""
            
Both datasets can be found in the *Download The Data* section.
            
## How do I use this dashboard ?

#### - Requirements : 
If you read this, it means all the technical requirements are met !

#### - Navigation :
This dashboard contains multiple pages :
    
- The **Dataframe Analysis** page provides information on the general structure of the data, sampling and features.
It also helps to shine a light on possible inconsistencies in the dataframe, and thus it is heavily
recommended to consult it before anything else.

- The **Linear Analysis** page offers a linear analysis, following specific trends and creating
a story through the observation of variations in the data.

- The **Channel Analysis** page offers an **interactive** dashboard for conducting your
own analysis on specific channels.

- The **Thematic Analysis** page offers an **interactive** dashboard for conducting your
own analysis on specific themes.

- The **Comparative Analysis** page mixes up the channel and thematic analysis to offer a 
broader view of the data, allowing for comparative analysis of data for all channels and all themes.

## Warnings (to read before usage) :

**Due to defaults in the construction of the original .CSV file rendering it unexploitable (header split between the 1st and 2nd rows),
some modifications had to be conducted via Excel, which can not be replicated through Python.**  
  
**It is highly advised to conduct any kind of further analysis with the pre-processed file instead of the source.**

## Credits
Coding/Data Cleaning/Data Analysis : *Romain Ferigo* 


"""
)
