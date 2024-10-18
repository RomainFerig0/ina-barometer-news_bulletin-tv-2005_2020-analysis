#%% Imports
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time
from bokeh.plotting import figure

#%% Extraction of the data

data = pd.read_csv(r"C:\Users\papel\DATA\App\data\barometre_2005_2020.csv", delimiter=";", header=0, encoding='latin-1')

#%% Extraction of the "MOIS" data of object type, conversion to datetime, extraction of the month and year number. 

data['date_parsed'] = pd.to_datetime(data['MOIS'].apply(lambda x: '1 ' + x.replace('-', ' ')), format='%d %B %y')

data['month_number'] = data['date_parsed'].dt.month
data['year_number'] = data['date_parsed'].dt.year

#Deletion of null data
data.dropna()

#%% Set page layout session and variables

st.set_page_config(page_title="Advanced Analysis", page_icon="📈")

#Declare show/hide status for sections
if "show_evol_news_coverage" not in st.session_state:
    st.session_state.show_evol_news_coverage = False

if "show_repart_themes" not in st.session_state:
    st.session_state.show_repart_themes = False
    
#Declare axis labels for months and channels
month_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12]
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
channels = ['TF1', 'France 2', 'France 3', 'Canal +', 'Arte', 'M6']
    
st.sidebar.header("Performing advanced analysis on the data at hand.")
st.sidebar.markdown("""
On this page, you can look at multiple analysis methods sporting different aggregations of data and types of graphs,
along with detailed observations and explanations of the meaning behind the identifiable trends.
""")
st.sidebar.header("Sections: ")
st.sidebar.markdown(
"""
[Analysis of the evolution of news coverage from 2005 to 2020](#analysis-of-the-evolution-of-news-coverage-from-2005-to-2020)  
                                                               
[Analysis of News Coverages per Theme, per Channel, and Contribution to Total](#conclusion)  
                                                                                  """
   )
                    
st.title(":blue[A straightforward, in-depth analysis.]")
st.markdown(
    """
On this page, we will conduct advanced analysis of the data. We will focus on 3 core aspects:  
    
- The **observation** of the temporal evolution on various metrics.  

- The **identification** of trends.  

- The **synthesis** and **explanation** of our findings.
""")

st.markdown("## Analysis of the Evolution of Total News Coverage, from 2005 to 2020")
    
button_evol_news_coverage = "Hide Section" if st.session_state.show_evol_news_coverage else "Show Section"

if st.button(button_evol_news_coverage, key="evol_news_coverage_button"):
    st.session_state.show_evol_news_coverage = not st.session_state.show_evol_news_coverage

if st.session_state.show_evol_news_coverage:
    yearly_totals = data.groupby('year_number')['Totaux'].sum().reset_index()

    st.markdown("### Representation of channels in news coverage")

    channel_coverage = data[channels].sum()
    plt.figure(figsize=(10, 6))
    plt.pie(channel_coverage, labels=channels, autopct='%1.1f%%', startangle=90, colors = ['blue', 'cyan', 'red', 'grey', 'yellow', 'magenta'])
    plt.title('Proportion of news coverages for each channel, from 2005 to 2020 ')
    st.pyplot(plt)
    
    st.write("""We can notice that Arte and Canal+ are heavily under-represented in the total
             population of news coverage. The reason for this can be found in the complementary
             information in the dataframe analysis : Arte and Canal+ are specialized channels
             (educative and sports/cinema respectively), and as such feature a smaller amount
             of news coverage programs (like news bulletins).  
             
             But does this affirmation ring true for the entire span of the data ?
             """)
    
    st.markdown("### Total TV Coverage per Year, from 2005 to 2020")

    plt.figure(figsize=(10,6))
    plt.plot(yearly_totals['year_number'], yearly_totals['Totaux'], marker='o')
    plt.xlabel('Year')
    plt.ylabel('Coverage')
    plt.grid(True)
    plt.title('Total TV Coverage per Year, from 2005 to 2020')
    plt.show()
    st.pyplot(plt)
    st.write("""We can notice a steep decrease in total TV coverage from 2012 on.
             This might be due to an error in sampling (as we have already seen the year 2020 is faulty in its sampling),
             or more probably a change
             in programming, resulting in less news coverage on certain channels.   
             
             To  be sure, let's analyze the local evolution of news coverage on each channel.
             """)
             
    st.markdown("### Total TV Coverage per Year on TF1, from 2005 to 2020")
    
    data_TF1 = data[['TF1', 'year_number']]
    yearly_totals_TF1 = data_TF1.groupby('year_number')['TF1'].sum().reset_index()
    plt.figure(figsize=(10,6))
    plt.plot(yearly_totals_TF1['year_number'], yearly_totals_TF1['TF1'], marker='o')
    plt.xlabel('Year')
    plt.ylabel('Coverage')
    plt.grid(True)
    plt.title('Total TV Coverage per Year on TF1, from 2005 to 2020')
    plt.show()
    st.pyplot(plt)

    st.markdown("### Total TV Coverage per Year on France 2, from 2005 to 2020")
    
    data_F2 = data[['France 2', 'year_number']]
    yearly_totals_F2 = data_F2.groupby('year_number')['France 2'].sum().reset_index()
    plt.figure(figsize=(10,6))
    plt.plot(yearly_totals_F2['year_number'], yearly_totals_F2['France 2'], marker='o')
    plt.xlabel('Year')
    plt.ylabel('Coverage')
    plt.grid(True)
    plt.title('Total TV Coverage per Year on France 2, from 2005 to 2020')
    plt.show()
    st.pyplot(plt)

    st.markdown("### Total TV Coverage per Year on France 3, from 2005 to 2020")
    data_F3 = data[['France 3', 'year_number']]
    yearly_totals_F3 = data_F3.groupby('year_number')['France 3'].sum().reset_index()
    plt.figure(figsize=(10,6))
    plt.plot(yearly_totals_F3['year_number'], yearly_totals_F3['France 3'], marker='o')
    plt.xlabel('Year')
    plt.ylabel('Coverage')
    plt.grid(True)
    plt.title('Total TV Coverage per Year on France 3, from 2005 to 2020')
    plt.show()
    st.pyplot(plt)

    st.markdown("### Total TV Coverage per Year on Canal +, from 2005 to 2020")
    data_canal = data[['Canal +', 'year_number']]
    yearly_totals_canal = data_canal.groupby('year_number')['Canal +'].sum().reset_index()
    plt.figure(figsize=(10,6))
    plt.plot(yearly_totals_canal['year_number'], yearly_totals_canal['Canal +'], marker='o')
    plt.xlabel('Year')
    plt.ylabel('Coverage')
    plt.grid(True)
    plt.title('Total TV Coverage per Year on Canal +, from 2005 to 2020')
    plt.show()
    st.pyplot(plt)
    
    st.write("""Compared to other channels, we can see that the decrease of news coverage by Canal+ was far less progressive,
             featuring a sudden drop in 2016. This can be explained by the programmation history of Canal+'s most known
             news bulletins, 'Le Grand Journal' and 'Le Petit Journal'. The first was the major news bulletin of the channel
             before opting for an alleviated format in 2016 after a drop in audiences, with 'Le Petit Journal' being cancelled the same year.
             """)
    
    st.markdown("### Total TV Coverage per Year on Arte, from 2005 to 2020")
    data_Arte = data[['Arte', 'year_number']]
    yearly_totals_Arte = data_Arte.groupby('year_number')['Arte'].sum().reset_index()
    plt.figure(figsize=(10,6))
    plt.plot(yearly_totals_Arte['year_number'], yearly_totals_Arte['Arte'], marker='o')
    plt.xlabel('Year')
    plt.ylabel('Coverage')
    plt.grid(True)
    plt.title('Total TV Coverage per Year on Arte, from 2005 to 2020')
    plt.show()

    st.pyplot(plt)

    st.markdown("### Total TV Coverage per Year on M6, from 2005 to 2020")
    data_M6 = data[['M6', 'year_number']]
    yearly_totals_M6 = data_M6.groupby('year_number')['M6'].sum().reset_index()
    plt.figure(figsize=(10,6))
    plt.plot(yearly_totals_M6['year_number'], yearly_totals_M6['M6'], marker='o')
    plt.xlabel('Year')
    plt.ylabel('Total Coverage')
    plt.grid(True)
    plt.title('Total TV Coverage per Year on M6, from 2005 to 2020')
    plt.show()
    st.pyplot(plt)
    st.write("""For M6, we can notice that it is the only channel to present an overall
             increase before the later decrease in news coverage, starting in 2006. This is easily explained
             as further researches demonstrate that 'Le 1245', M6's midday news broadcast, didn't start airing
             until 2006. We can also notice an acceleration in the coverage increase starting 2009, 
             which can be explained by the beginning of 'Le 1945' the same year. It constitutes the evening equivalent of 'Le 1245'
             """)
             
    st.markdown("### Compared Evolution of TV Coverage per Year, from 2005 to 2020")
    
    plt.figure(figsize=(10,6))
    plt.plot(yearly_totals['year_number'], yearly_totals['Totaux'], marker='o', color='green', alpha = 0.3, label = 'Total')
    plt.plot(yearly_totals_TF1['year_number'], yearly_totals_TF1['TF1'], marker='o', color='blue', alpha = 0.7,label = 'TF1')
    plt.plot(yearly_totals_F2['year_number'], yearly_totals_F2['France 2'], marker='o', color='cyan', alpha = 0.7, label = 'France 2')
    plt.plot(yearly_totals_F3['year_number'], yearly_totals_F3['France 3'], marker='o', color='red', alpha = 0.7, label = 'France 3')
    plt.plot(yearly_totals_canal['year_number'], yearly_totals_canal['Canal +'], marker='o', color='black', alpha = 0.7, label = 'Canal +')
    plt.plot(yearly_totals_Arte['year_number'], yearly_totals_Arte['Arte'], marker='o', color='yellow', alpha = 0.7, label = 'Arte')
    plt.plot(yearly_totals_M6['year_number'], yearly_totals_M6['M6'], marker= 'o', color='magenta', alpha = 0.7, label = 'M6')
    plt.xlabel('Year')
    plt.ylabel('Total Coverage')
    plt.grid(True)
    plt.title('Compared Evolution of TV Coverage per Year, from 2005 to 2020')
    plt.show()
    st.pyplot(plt)
           
    st.markdown("""
    ## Conclusion  
                
    We can see that every channel in the database sports a more or less **progressive decrease** in news coverage with time,
    and a general **downward trend**.  
    This trend starting in the years **between 2010 and 2013**. The rate of the decrease has different reasons depending
    on the channel at hand, but the global trend can be explained by **the rise of 24-hour news channels**, like BFMTV or LCI, which are
    unfortunately not featured in the data presented in this dashboard. With information becoming more accessible at all times on specialized
    channels, more generalist channels decided to opt for **more alleviated news bulletins**, discussing only the most relevant and essential news.  
    
    Regarding the **steep drop** that can commonly be observed on most graphs **between 2019 and 2020**, we know thanks to the dataframe analysis
    conducted earlier that the samples for the year 2020 are truncated of about 25%, as **no data is featured beyond September 2020**. Thus,
    the only meaning behind this steep drop is the **natural imbalance in the dataset**.
    """
    )
    
st.markdown("## Analysis of Total News Coverages per Theme, per Channel, and Contribution to Total")

button_repart_themes = "Hide Section" if st.session_state.show_repart_themes else "Show Section"

if st.button(button_repart_themes, key="repart_themes_button"):
    st.session_state.show_repart_themes = not st.session_state.show_repart_themes

if st.session_state.show_repart_themes:
    
    st.write("""We now know that, since 2012, TV channels that are not specialized in
             news bulletins have slowly started to include less of them in their programs.
             In this section, we will try to determine how exactly this phenomenon
             impacts the repartition of thematics in the news coverages of each channel.
             """)
             
    st.markdown("### Repartition of total coverages per theme")
    
    theme_totals = data.groupby('THEMATIQUES')['Totaux'].sum().reset_index()
    plt.figure(figsize=(10,6))
    plt.bar(theme_totals['THEMATIQUES'], theme_totals['Totaux'], color='skyblue')
    plt.xlabel('Theme')
    plt.ylabel('Total coverage')
    plt.xticks(rotation=45)
    plt.title('Repartition of total coverages per theme')
    plt.show()
    st.pyplot(plt)
    
    st.markdown("### Repartition of coverage per theme, and contribution to total coverage, on TF1")
    
    data2_TF1 = data[['THEMATIQUES', 'TF1']]
    theme_TF1 = data2_TF1.groupby('THEMATIQUES')['TF1'].sum().reset_index()
    plt.figure(figsize=(10,6))
    plt.bar(theme_TF1['THEMATIQUES'], theme_TF1['TF1'], color='skyblue')
    plt.bar(theme_totals['THEMATIQUES'], theme_totals['Totaux'], color='skyblue', alpha = 0.5)
    plt.xlabel('Theme')
    plt.ylabel('Coverage')
    plt.xticks(rotation=45)
    plt.title('Repartition of coverage per theme, and contribution to total coverage, on TF1')
    plt.show()
    st.pyplot(plt)
    
    st.markdown("### Repartition of coverage per theme, and contribution to total coverage, on France 2")
    
    data2_F2 = data[['THEMATIQUES', 'France 2']]
    theme_F2 = data2_F2.groupby('THEMATIQUES')['France 2'].sum().reset_index()
    plt.figure(figsize=(10,6))
    plt.bar(theme_F2['THEMATIQUES'], theme_F2['France 2'], color='skyblue')
    plt.bar(theme_totals['THEMATIQUES'], theme_totals['Totaux'], color='skyblue', alpha = 0.5)
    plt.xlabel('Theme')
    plt.ylabel('Coverage')
    plt.xticks(rotation=45)
    plt.title('Repartition of coverage per theme, and contribution to total coverage, on France 2')
    plt.show()
    st.pyplot(plt)
    
    st.markdown("### Repartition of coverage per theme, and contribution to total coverage, on France 3")
    
    data2_F3 = data[['THEMATIQUES', 'France 3']]
    theme_F3 = data2_F3.groupby('THEMATIQUES')['France 3'].sum().reset_index()
    plt.figure(figsize=(10,6))
    plt.bar(theme_F3['THEMATIQUES'], theme_F3['France 3'], color='skyblue')
    plt.bar(theme_totals['THEMATIQUES'], theme_totals['Totaux'], color='skyblue', alpha = 0.5)
    plt.xlabel('Theme')
    plt.ylabel('Coverage')
    plt.xticks(rotation=45)
    plt.title('Repartition of coverage per theme, and contribution to total coverage, on France 3')
    plt.show()
    st.pyplot(plt)
    
    st.markdown(
    """
    ### Partial conclusion : TF1, France 2 and France 3
                
    We can notice that **the repartition of themes on TF1, France 2 and France 3 follows the general trend very closely**, with
    **society, sports, international and economy** being the **most covered** topics. This tracks, as we already
    know from the preliminary dataframe analysis that TF1, France 2 and France 3 are **generalist channels**.
    Moreover, it seems that **all three channels contribute heavily to the total population of news coverage**
    on each topic. This can be explained by **news broadcasts being some of the core programs** of all three channels
    (The 'JT 20 Heures', the biggest news bulletin of the evening on TF1, has its equivalents on France 2 and France 3, 
     along with the 'JT 13 Heures', the midday news bulletin.)
    
    **Thus, all three channels follow the general trend as generalist channels, with their twice-daily news bulletins contributing
    heavily to the total news coverage.**
             
    """
    )  

    st.markdown("### Repartition of coverage per theme, and contribution to total coverage, on Canal +")
    data2_canal = data[['THEMATIQUES', 'Canal +']]
    theme_canal = data2_canal.groupby('THEMATIQUES')['Canal +'].sum().reset_index()
    plt.figure(figsize=(10,6))
    plt.bar(theme_canal['THEMATIQUES'], theme_canal['Canal +'], color='skyblue')
    plt.bar(theme_totals['THEMATIQUES'], theme_totals['Totaux'], color='skyblue', alpha = 0.5)
    plt.xlabel('Theme')
    plt.ylabel('Coverage')
    plt.xticks(rotation=45)
    plt.title('Repartition of coverage per theme, and contribution to total coverage, on Canal +')
    plt.show()
    st.pyplot(plt)
    st.write("""A surprising detail of this graph is the comparatively small proportion of sport-based
             coverages on Canal +, compared to total coverages as well as other topics on the channel :  
             
             """)
    
    st.markdown("### Repartition of coverage per theme, and contribution to total coverage, on Arte")
    data2_arte = data[['THEMATIQUES', 'Arte']]
    theme_arte = data2_arte.groupby('THEMATIQUES')['Arte'].sum().reset_index()
    plt.figure(figsize=(10,6))
    plt.bar(theme_arte['THEMATIQUES'], theme_arte['Arte'], color='skyblue')
    plt.bar(theme_totals['THEMATIQUES'], theme_totals['Totaux'], color='skyblue', alpha = 0.5)
    plt.xlabel('Theme')
    plt.ylabel('Coverage')
    plt.xticks(rotation=45)
    plt.title('Repartition of coverage per theme, and contribution to total coverage, on Arte')
    plt.show()
    st.pyplot(plt)
    st.write("""The most apparent detail observable on this graph is the colossal 
             proportion of "Histoire-hommages", or history-focused coverages on
             the channel Arte, taking nearly 1/3 of total coverages of the topic,
             followed by smaller participations in society-based and culture-based
             coverages.  
             As we already know, Arte is a channel focused on
             "educative and art-related programs", and the only one presented as such in
             the channels at hand. Thus, it is not surprising to find a specialized
             channel contribute in specific topic coverages.
             """)
    
    
    st.markdown("### Repartition of coverage per theme, and contribution to total coverage, on M6")
    data2_M6 = data[['THEMATIQUES', 'M6']]
    theme_M6 = data2_M6.groupby('THEMATIQUES')['M6'].sum().reset_index()
    plt.figure(figsize=(10,6))
    plt.bar(theme_M6['THEMATIQUES'], theme_M6['M6'], color='skyblue')
    plt.bar(theme_totals['THEMATIQUES'], theme_totals['Totaux'], color='skyblue', alpha = 0.5)
    plt.xlabel('Theme')
    plt.ylabel('Coverage')
    plt.xticks(rotation=45)
    plt.title('Repartition of coverage per theme, and contribution to total coverage, on M6')
    plt.show()
    
    st.pyplot(plt)
    
    st.markdown("### Compared repartition of coverage per theme, and contribution to total coverage, for all channels")

    bar_width = 0.5
    
    plt.figure(figsize=(10,6))
    plt.bar(theme_TF1['THEMATIQUES'], theme_TF1['TF1'], label='TF1', color='blue')
    plt.bar(theme_F2['THEMATIQUES'], theme_F2['France 2'], bottom=theme_TF1['TF1'], label='France 2', color='cyan')
    plt.bar(theme_F3['THEMATIQUES'], theme_F3['France 3'], bottom=theme_TF1['TF1'] + theme_F2['France 2'], label='France 3', color='red')
    plt.bar(theme_canal['THEMATIQUES'], theme_canal['Canal +'], bottom= theme_TF1['TF1'] + theme_F2['France 2'] + theme_F3['France 3'], label='Canal', color='black')
    plt.bar(theme_arte['THEMATIQUES'], theme_arte['Arte'], bottom=theme_TF1['TF1'] + theme_F2['France 2'] + theme_F3['France 3'] + theme_canal['Canal +'], label='Arte', color='yellow')
    plt.bar(theme_M6['THEMATIQUES'], theme_M6['M6'], bottom =theme_TF1['TF1'] + theme_F2['France 2'] + theme_F3['France 3'] + theme_canal['Canal +'] + theme_arte['Arte'], label='M6', color='magenta')
    
    plt.xlabel('Theme')
    plt.ylabel('Coverage')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()
    plt.title('Compared repartition of coverage per theme, for all channels, from 2005 to 2020')
    st.pyplot(plt)

    st.markdown(
    """
    ### Conclusion
             
    """
    )    

st.markdown(
"""
## What to do now ?
     
In this analysis section, we only showed a single story, a small part of the possible observations
with the informations present in this dataset. In the following sections, you will be able to conduct
your own visualizations, observing new tendencies and extracting new informations.
"""
)  