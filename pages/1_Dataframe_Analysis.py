#%% Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#%% Extraction of the data

data = pd.read_csv(r"C:\Users\papel\DATA\App\data\barometre_2005_2020.csv", delimiter=";", header=0, encoding='latin-1')

#%% Extraction of the "MOIS" data of object type, conversion to datetime, extraction of the month and year number. 

data['date_parsed'] = pd.to_datetime(data['MOIS'].apply(lambda x: '1 ' + x.replace('-', ' ')), format='%d %B %y')

data['month_number'] = data['date_parsed'].dt.month
data['year_number'] = data['date_parsed'].dt.year

#Deletion of null data
data.dropna()

#%% Set page layout session and variables  

st.set_page_config(page_title="Data Analysis", page_icon="📈")

#Declare show/hide status for sections
if "show_field_desc" not in st.session_state:
    st.session_state.show_field_desc = False
if "show_sample_analysis" not in st.session_state:
    st.session_state.show_sample_analysis = False

#Declare axis labels for years, months and channels
years = list(range(2005, 2021))
month_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
channels = ['TF1', 'France 2', 'France 3', 'Canal +', 'Arte', 'M6']
    
#Declare number of cells of the dataframe
size = data.size

st.sidebar.header("Getting to know the data dataframe, to help in further analysis.")
st.sidebar.markdown("""
                    On this page, you can find multiple technical informations regarding the data : 
                        the fields, their specificities, along with additional information in order
                        to create the right context for the following analysis to be as intelligible
                        as can be.
                    """)
st.sidebar.header("Sections: ")
st.sidebar.markdown(
"""
[Brief summary](#brief-summary)  
                                                               
[Dataframe Dimensions](#dataframe-dimensions)  
                                                                               
[Dataframe Fields](#dataframe-fields)
                   
[Field Descriptions](#field-descriptions)

[Sample Analysis](#sample-analysis)
   """
   ) 

st.title(":blue[Let's get to know the data !]")

st.markdown(
    """
## Brief summary  

**This dataframe offers information regarding news coverage by the first 6 channels of public french television, sorted by thematics, from 2005 to 2020.** 
It was compiled by INA, the French National Institute of the Audio-Visual
            
"""
)

st.image("logo-ina.jpg")

st.markdown(f"## Dataframe Dimensions  \n#### Size of the dataframe: { size } cells")

#Declare number of rows in the dataframe
entries = data[data.columns[0]].count()
st.markdown(f"#### Total number of entries: { entries } rows")

#Declare type of each column
st.markdown("## Dataframe Fields")
data.dtypes

st.markdown("## Field Descriptions")
button_field_desc = "Hide Section" if st.session_state.show_field_desc else "Show Section"
    
if st.button(button_field_desc, key="field_desc_button"):
    st.session_state.show_field_desc = not st.session_state.show_field_desc

if st.session_state.show_field_desc:
    st.markdown(
        """
    ### MOIS  
    Temporal indicator of the month and year for the data in a given row.

    ### THEMATIQUES  
    Thematic indicator for the data in a given row. They can take any of
    14 fixed values.

    ### TF1  
    Number of occurences on the channel TF1.
    It is the first French TV channel in terms of scores.  
    Its programmation is generalist.  
    [Link here](https://fr.wikipedia.org/wiki/TF1)

    ### France 2
    Number of occurences on the channel France 2.  
    Its programmation is generalist, varying between TV drama, news broadcasts, movies and sports retransmissions.  
    [Link here](https://fr.wikipedia.org/wiki/France_2)

    ### France 3
    Number of occurences on the channel France 3.  
    Its programmation is generalist, but is segmented between numerous regional channels offering exclusive regional news broadcasts.  
    [Link here](https://fr.wikipedia.org/wiki/France_3)

    ### Canal +
    Number of occurences on the channel Canal +.  
    It is the only private channel in the list. Its programmation is centered around movies and sports.  
    [Link here](https://fr.wikipedia.org/wiki/Canal%2B)

    ### Arte
    Number of occurences on the channel Arte.  
    It is a binational channel focused on educative and art-related programs.  
    [Link here](https://fr.wikipedia.org/wiki/Arte)

    ### M6
    Number of occurences on the channel M6.  
    Its programmation is generalist, but mostly focused on entertainment and occasional news broadcasts at key periods of the day.  
    [Link here](https://fr.wikipedia.org/wiki/M6)

    ### Totaux
    Number of total occurences.

    ### date_parsed
    Temporal indicator of the month and year for the data in a given row, after parsing to datetime.

    ### month_number
    Number designing the month for the data in a given row.

    ### year_number
    Number designing the year for the data in a given row.

    """
    )

st.markdown("## Sample Analysis")

button_sample_analysis = "Hide Section" if st.session_state.show_sample_analysis else "Show Section"
    
if st.button(button_sample_analysis, key="sample_analysis_button"):
    st.session_state.show_sample_analysis = not st.session_state.show_sample_analysis

if st.session_state.show_sample_analysis:
    st.write(
    """
    One step to ensure the viability of the data we are going to analyze is to study
    the repartition of the samples, to ensure that the features are equally represented
    in the dataset. The first feature whose balance we need to verify is the year.
    """)
    st.markdown("### Number of samples per year")
    yearly_counts = data.groupby('year_number').size()
    plt.figure(figsize=(10, 6))
    yearly_counts.plot(kind='bar', color='skyblue')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Samples', fontsize=12)
    plt.title('Number of Samples per Year', fontsize=14)
    plt.show()

    st.pyplot(plt)
    st.write(
    """
    The graph shows that the samples are evenly distributed between years from 2005 to 2019.
    However, **the year 2020 lacks a significant amount of samples** in order for the set to be
    entirely balanced.  

    **We perform an analysis in detail of the samples for all months of all years, in order to identify the problem.** 
    """)

    selected_year = st.selectbox('Select a Year', years)
    selected_year = int(selected_year)

    st.markdown(f"### Number of samples per month, for {selected_year}")
    data_year = data[data['year_number'] == selected_year]
    monthly_counts_year = data_year.groupby('month_number').size()
    plt.figure(figsize=(10, 6))
    monthly_counts_year.plot(kind='bar', color='skyblue')
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Number of Samples', fontsize=12)
    plt.xticks(ticks=month_numbers, labels=month_labels)
    plt.title(f'Number of Samples per Month, for {selected_year}', fontsize=14)
    plt.show()

    st.pyplot(plt)
    
    if selected_year == 2020 :
        st.write("""This analysis clarifies the problem : **From September 2020 on, not a single sample is registered in the file**.""")
        st.markdown("""
        ### Partial conclusion :
        This issue is going to render any data analysis we might conduct beyond 2019 **inconclusive**, as **the data at hand
        does not fairly cover the entire period of the year 2020**.  
        """)
    
    st.write(
    """    
    A second feature that we need to study the repartition of are the thematics.
    """)
    
    st.markdown("### Number of samples per thematic")
    data_catastrophe = data[['THEMATIQUES', 'Totaux']]
    data_cata_group = data_catastrophe.groupby('THEMATIQUES').size()
    data_cata_group.plot(kind='bar', color='skyblue')
    plt.title('Repartition of thematics per sample size', fontsize=14)
    plt.xticks(rotation=45)
    plt.show()
    
    st.pyplot(plt)
    
    st.write(
    """    
    We can see that the repartition of the samples per thematic, unlike the repartition per period of time, is **even**.
    
    The last feature we need to study regarding the repartition of samples are the channels .
    """)
    
    st.markdown("### Channel representation")

    channel_coverage = data[channels].count()
    plt.figure(figsize=(10, 6))
    plt.bar(channel_coverage.index, channel_coverage.values, label = 'Total number of samples')
    plt.title('Number of samples per channel ')
    st.pyplot(plt)
    
    channel_coverage = data[channels].sum()
    plt.figure(figsize=(10, 6))
    plt.bar(channel_coverage.index, channel_coverage.values, label = 'Total coverage')
    plt.title('Sum of news coverages for each channel from 2005 to 2020 ')
    st.pyplot(plt)
    st.write(
    """    
    With this, we observe an even repartition of the samples even along the different channels. However,
    we can notice some tendencies on the aspect of total news coverage : Some channels are heavily
    under-represented in the overall news coverage, which we are going to investigate in the next part.
    """)
    st.markdown("""
    ### Conclusion :
    
    Although this database is supposed to cover the years from 2005 to 2020, we can see that a 'yearly'
    point of view is heavily faulted due to incomplete data on the last year. For this reason, we might
    see radical changes in the data starting 2020, and should not take it into account. For studying
    data on the year 2020 precisely, we will prefer to zoom in with a 'monthly' POV, in order to
    capture the true nature of the evolution of the data.
    """)
