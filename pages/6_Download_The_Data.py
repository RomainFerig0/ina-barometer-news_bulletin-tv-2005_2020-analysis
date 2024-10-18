#%% Imports
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

#%% Extraction of the data

data = pd.read_csv(r"C:\Users\papel\DATA\App\data\barometre_2005_2020.csv", delimiter=";", header=0, encoding='latin-1')

#%% Extraction of the "MOIS" data of object type, conversion to datetime, extraction of the month and year number. 

data['date_parsed'] = pd.to_datetime(data['MOIS'].apply(lambda x: '1 ' + x.replace('-', ' ')), format='%d %B %y')
data['month_number'] = data['date_parsed'].dt.month
data['year_number'] = data['date_parsed'].dt.year

#%% Deletion of null data.
data.dropna()

#%% Convert dataframe to CSV
@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("latin-1")

#%%
st.set_page_config(page_title="Download The Data", page_icon="📈")

st.sidebar.header("Download the data to conduct your own analysis !")
st.sidebar.markdown("""
                    On this page, you can find a download link for the pre-processed data,
                    along with a link to the original .csv file from the official french
                    website.
                    """)

data_size = data.memory_usage(deep=True).sum() / (1024 * 1024) # Compute size of the dataframe in memory.

st.image("9205302.png")

st.markdown(
    f"""
    ## Option 1 - Download the pre-processed data  
    File size : 177 Ko  
    Dataframe size (in memory) : { data_size } MB
    """
    )

csv = convert_df(data) # Call function to convert dataframe into CSV
st.download_button(
    label="Download **barometer_2005_2020.csv**",
    data=csv,
    file_name="barometer_2005_2020.csv",
    mime="text/csv",
)

st.markdown(
    """
    ## Option 2 - Download the source data on [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/classement-thematique-des-sujets-de-journaux-televises-janvier-2005-septembre-2020)
    """
    )