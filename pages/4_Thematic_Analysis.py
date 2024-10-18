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

st.set_page_config(page_title="Thematic Analysis", page_icon="📈")

#Declare axis labels for themes, years, channels and months.
theme_list = ['Catastrophes', 'Sport', 'Santé', 'Sciences et techniques', 'International', 'Justice', 'Politique France', 'Culture-loisirs', 'Economie', 'Education', 'Environnement', 'Faits divers', 'Société', 'Histoire-hommages']
years = list(range(2005, 2021))
channels = ['TF1', 'France 2', 'France 3', 'Canal +', 'Arte', 'M6']
month_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12]
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

st.title(":blue[Performing advanced analysis on the thematics !]")
st.markdown("On this page, you will be able to **target** and **visualize** trends regarding specific thematics.")

#Declare state to show/hide mean in graphs
if "show_mean" not in st.session_state:
    st.session_state.show_mean = False

with st.sidebar:
    st.title('Thematic Data Dashboard')
    
    selected_theme = st.selectbox('Select a Theme', theme_list) #Input theme
    selected_theme = str(selected_theme)
    
    selected_year = st.selectbox('Select a Year', years) #Input year
    selected_year = int(selected_year)
    
    button_show_mean = "Hide Mean" if st.session_state.show_mean else "Show Mean" #Show/hide mean in graphs

    if st.button(button_show_mean, key="show_mean_button"): #Alter title of the show/hide mean button
        st.session_state.show_mean = not st.session_state.show_mean
    
data_theme = data[data['THEMATIQUES'] == selected_theme] #All samples corresponding to input theme.
yearly_mean_theme = data_theme.groupby('year_number')['Totaux'].mean().reset_index() #Total yearly mean on all samples corresponding to input theme.
monthly_mean_theme = data_theme.groupby('month_number')['Totaux'].mean().reset_index() #Total mean on all samples corresponding to input theme and year.
yearly_totals_theme = data_theme.groupby('year_number')['Totaux'].sum().reset_index() #Total of all values corresponding to input year

yearly_theme = data[(data['THEMATIQUES'] == selected_theme) & (data['year_number'] == selected_year)]
yearly_theme_coverage = yearly_theme[channels].sum()
total_coverage = data[(data['THEMATIQUES'] == selected_theme)]
total_coverage_true = total_coverage[channels].sum()

data_theme_year = data[(data['THEMATIQUES'] == selected_theme) & (data['year_number'] == selected_year)]
monthly_totals_theme = data_theme_year.groupby('month_number')['Totaux'].sum().reset_index()
    
st.markdown(f"## Evolution of Total TV Coverage for '{selected_theme}', from 2005 to 2020.")

plt.figure(figsize=(10,6))
plt.plot(yearly_totals_theme['year_number'], yearly_totals_theme['Totaux'], marker='o', label = 'Total coverage per year')
if st.session_state.show_mean:
    plt.plot(yearly_mean_theme['year_number'], yearly_mean_theme['Totaux'], alpha = 0.4, color = 'green', label = 'Mean evolution per year')
plt.xlabel('Year')
plt.ylabel('Coverage')
plt.grid(True)
plt.legend()
plt.title(f'Evolution of total TV Coverage for "{selected_theme}", from 2005 to 2020, compared to the mean', fontsize=14)
plt.show()
st.pyplot(plt)
         
st.markdown(f"### Let's zoom in on year {selected_year} for '{selected_theme}'...")

plt.figure(figsize=(10,6))
plt.plot(monthly_totals_theme['month_number'], monthly_totals_theme['Totaux'], marker='o', label = 'Total coverage per month')
if st.session_state.show_mean:
    plt.plot(monthly_mean_theme['month_number'], monthly_mean_theme['Totaux'], alpha = 0.4, color = 'green', label = 'Mean evolution per month')
plt.xlabel('Month')
plt.ylabel('Coverage')
plt.grid(True)
plt.xticks(ticks=month_numbers, labels=month_labels)
plt.legend()
plt.title(f'Evolution of Total TV Coverage for "{selected_theme}", for 2005, compared to the mean', fontsize=14)
st.pyplot(plt)

st.markdown(f"### Repartition of news coverage for '{selected_theme}' in {selected_year}")

plt.figure(figsize=(10,6))
if st.session_state.show_mean:
    plt.bar(total_coverage_true.index, total_coverage_true.values, alpha = 0.4, color = 'green', label = 'Total coverage from 2005 to 2020')
plt.bar(yearly_theme_coverage.index, yearly_theme_coverage.values, label = f'Coverage for {selected_year}')
plt.xlabel('Channel')
plt.ylabel(f'Coverage for {selected_year}')
plt.xticks(rotation=45)
plt.legend()
st.pyplot(plt)