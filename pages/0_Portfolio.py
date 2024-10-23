#%% Imports
import streamlit as st

st.set_page_config(page_title="About Me", page_icon="📈")

st.title(":blue[About the author.]")

st.markdown("""
                    Student in fourth year of engineering studies at EFREI Paris,
                    specializing in data science & data engineering, I am the
                    author of this dataframe.  
                    
                    ### Formation
                    
                    Engineering studies at [EFREI Paris](https://www.efrei.fr/)  
                    2021-Ongoing  
                    Master in Data Engineering
                    """)
st.sidebar.header("Websites: ")
st.sidebar.markdown(
"""
[LinkedIn](https://fr.linkedin.com/in/romain-ferigo-043b09221)  
                                                               
[Project Github](https://github.com/RomainFerig0/ina-barometer-news_bulletin-tv-2005_2020-analysis)  
                                                                               
   """
   ) 

col1, col2 = st.columns([5, 5])

with col1:
    st.markdown("""
                ### Langues (Niveau):   
                 - Anglais (C1)  
                 - Espagnol (B1)  
                 - Français (Affaires)  
                 
                ### Soft skills
                 - Curieux  
                 - Ponctuel  
                 - Sérieux
                """)
                
with col2:
    st.markdown("""
                ### Web & Multimédia:  
                - JavaScript, HTML, CSS  
                - Machine learning  
                - Python, C, Java  
                - SQL  
                - Montage (vidéo & image)  
                - Excel
                """)