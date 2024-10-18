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

#%%
st.set_page_config(page_title="Advanced Analysis", page_icon="📈")

#Declare axis labels for years and months.
years = list(range(2005, 2021))
month_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12]
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#Set show/hide status for all channels
if "show_TF1" not in st.session_state:
    st.session_state.show_TF1 = False

if "show_F2" not in st.session_state:
    st.session_state.show_F2 = False
    
if "show_F3" not in st.session_state:
    st.session_state.show_F3 = False
    
if "show_canal" not in st.session_state:
    st.session_state.show_canal = False

if "show_Arte" not in st.session_state:
    st.session_state.show_Arte = False
    
if "show_M6" not in st.session_state:
    st.session_state.show_M6 = False
    
if "show_total" not in st.session_state:
    st.session_state.show_total = False
    
with st.sidebar: #Set show/hide buttons for every channel
    st.title('🏂 Compared Analysis Dashboard')
    
    button_show_TF1 = "Hide TF1" if st.session_state.show_TF1 else "Show TF1"
    if st.button(button_show_TF1, key="show_TF1_button"):
        st.session_state.show_TF1 = not st.session_state.show_TF1
        
    button_show_F2 = "Hide France 2" if st.session_state.show_F2 else "Show France 2"
    if st.button(button_show_F2, key="show_F2_button"):
        st.session_state.show_F2 = not st.session_state.show_F2
        
    button_show_F3 = "Hide France 3" if st.session_state.show_F3 else "Show France 3"
    if st.button(button_show_F3, key="show_F3_button"):
        st.session_state.show_F3 = not st.session_state.show_F3
        
    button_show_canal = "Hide Canal +" if st.session_state.show_canal else "Show Canal +"
    if st.button(button_show_canal, key="show_canal_button"):
        st.session_state.show_canal = not st.session_state.show_canal
        
    button_show_Arte = "Hide Arte" if st.session_state.show_Arte else "Show Arte"
    if st.button(button_show_Arte, key="show_Arte_button"):
        st.session_state.show_Arte = not st.session_state.show_Arte
        
    button_show_M6 = "Hide M6" if st.session_state.show_Arte else "Show M6"
    if st.button(button_show_M6, key="show_M6_button"):
        st.session_state.show_M6 = not st.session_state.show_M6
        
    button_show_total = "Hide Total" if st.session_state.show_total else "Show Total"
    if st.button(button_show_total, key="show_total_button"):
        st.session_state.show_total = not st.session_state.show_total

    selected_year = st.selectbox('Select a Year', years) #Input year
    selected_year = int(selected_year)
    
#Yearly coverages for all channels/total

data_yearly = data[data['year_number'] == selected_year]
yearly_totals = data.groupby('year_number')['Totaux'].sum().reset_index()

data_TF1 = data[['TF1', 'year_number']]
yearly_totals_TF1 = data_TF1.groupby('year_number')['TF1'].sum().reset_index()

data_F2 = data[['France 2', 'year_number']]
yearly_totals_F2 = data_F2.groupby('year_number')['France 2'].sum().reset_index()

data_F3 = data[['France 3', 'year_number']]
yearly_totals_F3 = data_F3.groupby('year_number')['France 3'].sum().reset_index()

data_canal = data[['Canal +', 'year_number']]
yearly_totals_canal = data_canal.groupby('year_number')['Canal +'].sum().reset_index()

data_Arte = data[['Arte', 'year_number']]
yearly_totals_Arte = data_Arte.groupby('year_number')['Arte'].sum().reset_index()

data_M6 = data[['M6', 'year_number']]
yearly_totals_M6 = data_M6.groupby('year_number')['M6'].sum().reset_index()

#Sum of all coverages for all channels/total, for an input year

data_selected_year_TF1 = data_yearly[['TF1', 'month_number']]
data_selected_year_totals_TF1 = data_selected_year_TF1.groupby('month_number')['TF1'].sum().reset_index()

data_selected_year_F2 = data_yearly[['France 2', 'month_number']]
data_selected_year_totals_F2 = data_selected_year_F2.groupby('month_number')['France 2'].sum().reset_index()

data_selected_year_F3 = data_yearly[['France 3', 'month_number']]
data_selected_year_totals_F3 = data_selected_year_F3.groupby('month_number')['France 3'].sum().reset_index()

data_selected_year_canal = data_yearly[['Canal +', 'month_number']]
data_selected_year_totals_canal = data_selected_year_canal.groupby('month_number')['Canal +'].sum().reset_index()

data_selected_year_Arte = data_yearly[['Arte', 'month_number']]
data_selected_year_totals_Arte = data_selected_year_Arte.groupby('month_number')['Arte'].sum().reset_index()

data_selected_year_M6 = data_yearly[['M6', 'month_number']]
data_selected_year_totals_M6 = data_selected_year_M6.groupby('month_number')['M6'].sum().reset_index()

#Sum of all thematic coverages for all channels/total

data_channel_theme_TF1 = data_yearly[['THEMATIQUES', 'TF1']]
theme_coverage_TF1 = data_channel_theme_TF1.groupby('THEMATIQUES')['TF1'].sum().reset_index()

data_channel_theme_F2 = data_yearly[['THEMATIQUES', 'France 2']]
theme_coverage_F2 = data_channel_theme_F2.groupby('THEMATIQUES')['France 2'].sum().reset_index()

data_channel_theme_F3 = data_yearly[['THEMATIQUES', 'France 3']]
theme_coverage_F3 = data_channel_theme_F3.groupby('THEMATIQUES')['France 3'].sum().reset_index()

data_channel_theme_canal = data_yearly[['THEMATIQUES', 'Canal +']]
theme_coverage_canal = data_channel_theme_canal.groupby('THEMATIQUES')['Canal +'].sum().reset_index()

data_channel_theme_arte = data_yearly[['THEMATIQUES', 'Arte']]
theme_coverage_arte = data_channel_theme_arte.groupby('THEMATIQUES')['Arte'].sum().reset_index()

data_channel_theme_M6 = data_yearly[['THEMATIQUES', 'M6']]
theme_coverage_M6 = data_channel_theme_M6.groupby('THEMATIQUES')['M6'].sum().reset_index()

data_channel_theme_totals = data_yearly[['THEMATIQUES', 'Totaux']]
theme_coverage_totals = data_channel_theme_totals.groupby('THEMATIQUES')['Totaux'].sum().reset_index()

st.title(":blue[Getting a broader view]")
st.markdown("On this page, you will be able to conduct more **general** analysis and to study the **relationship** between the data via a comparative analysis.")
         
#Plot compared evolution of TV Coverage per Year from 2005 to 2020

st.markdown("### Compared Evolution of TV Coverage per Year, from 2005 to 2020")

plt.figure(figsize=(10,6))
if st.session_state.show_TF1:
    plt.plot(yearly_totals_TF1['year_number'], yearly_totals_TF1['TF1'], marker='o', color='blue', alpha = 0.7,label = 'TF1')
if st.session_state.show_F2:
    plt.plot(yearly_totals_F2['year_number'], yearly_totals_F2['France 2'], marker='o', color='cyan', alpha = 0.7, label = 'France 2')
if st.session_state.show_F3:
    plt.plot(yearly_totals_F3['year_number'], yearly_totals_F3['France 3'], marker='o', color='red', alpha = 0.7, label = 'France 3')
if st.session_state.show_canal:
    plt.plot(yearly_totals_canal['year_number'], yearly_totals_canal['Canal +'], marker='o', color='black', alpha = 0.7, label = 'Canal +')
if st.session_state.show_Arte:
    plt.plot(yearly_totals_Arte['year_number'], yearly_totals_Arte['Arte'], marker='o', color='yellow', alpha = 0.7, label = 'Arte')
if st.session_state.show_M6:
    plt.plot(yearly_totals_M6['year_number'], yearly_totals_M6['M6'], marker= 'o', color='magenta', alpha = 0.7, label = 'M6')
if st.session_state.show_total:
    plt.plot(yearly_totals['year_number'], yearly_totals['Totaux'], marker= 'o', color='green', alpha = 0.7, label = 'Totals')

plt.xlabel('Year')
plt.ylabel('Total Coverage')
plt.grid(True)
plt.title('Compared Evolution of TV Coverage per Year, from 2005 to 2020')
plt.legend()
plt.show()
st.pyplot(plt)

st.markdown(f"### Let's zoom in on year {selected_year}...")

plt.figure(figsize=(10,6))
if st.session_state.show_TF1:
    plt.plot(data_selected_year_totals_TF1['month_number'], data_selected_year_totals_TF1['TF1'], marker='o', color='blue', alpha = 0.7,label = 'TF1')
if st.session_state.show_F2:
    plt.plot(data_selected_year_totals_F2['month_number'], data_selected_year_totals_F2['France 2'], marker='o', color='cyan', alpha = 0.7, label = 'France 2')
if st.session_state.show_F3:
    plt.plot(data_selected_year_totals_F3['month_number'], data_selected_year_totals_F3['France 3'], marker='o', color='red', alpha = 0.7, label = 'France 3')
if st.session_state.show_canal:
    plt.plot(data_selected_year_totals_canal['month_number'], data_selected_year_totals_canal['Canal +'], marker='o', color='black', alpha = 0.7, label = 'Canal +')
if st.session_state.show_Arte:
    plt.plot(data_selected_year_totals_Arte['month_number'], data_selected_year_totals_Arte['Arte'], marker='o', color='yellow', alpha = 0.7, label = 'Arte')
if st.session_state.show_M6:
    plt.plot(data_selected_year_totals_M6['month_number'], data_selected_year_totals_M6['M6'], marker= 'o', color='magenta', alpha = 0.7, label = 'M6')

plt.xlabel('Month')
plt.ylabel('Coverage')
plt.grid(True)
plt.xticks(ticks=month_numbers, labels=month_labels)
plt.title(f'Compared Evolution of TV Coverage, for {selected_year}')
plt.legend()
plt.show()
st.pyplot(plt)

#Plot compared contribution to total coverage per theme

st.markdown(f"### Total Repartition of Coverage per Theme, and Contribution to Total Coverage, per Channel, in {selected_year}")

bar_width = 0.5
plt.figure(figsize=(10,6))
if st.session_state.show_total:
    plt.bar(theme_coverage_totals['THEMATIQUES'], theme_coverage_totals['Totaux'], label='Totaux', color='green', alpha =0.3)
if st.session_state.show_TF1:
    plt.bar(theme_coverage_TF1['THEMATIQUES'], theme_coverage_TF1['TF1'], label='TF1', color='blue')
if st.session_state.show_F2:
    plt.bar(theme_coverage_F2['THEMATIQUES'], theme_coverage_F2['France 2'], bottom=theme_coverage_TF1['TF1'], label='France 2', color='cyan')
if st.session_state.show_F3:
    plt.bar(theme_coverage_F3['THEMATIQUES'], theme_coverage_F3['France 3'], bottom=theme_coverage_TF1['TF1'] + theme_coverage_F2['France 2'], label='France 3', color='red')
if st.session_state.show_canal:
    plt.bar(theme_coverage_canal['THEMATIQUES'], theme_coverage_canal['Canal +'], bottom= theme_coverage_TF1['TF1'] + theme_coverage_F2['France 2'] + theme_coverage_F3['France 3'], label='Canal', color='black')
if st.session_state.show_Arte:
    plt.bar(theme_coverage_arte['THEMATIQUES'], theme_coverage_arte['Arte'], bottom=theme_coverage_TF1['TF1'] + theme_coverage_F2['France 2'] + theme_coverage_F3['France 3'] + theme_coverage_canal['Canal +'], label='Arte', color='yellow')
if st.session_state.show_M6:
    plt.bar(theme_coverage_M6['THEMATIQUES'], theme_coverage_M6['M6'], bottom =theme_coverage_TF1['TF1'] + theme_coverage_F2['France 2'] + theme_coverage_F3['France 3'] + theme_coverage_canal['Canal +'] + theme_coverage_arte['Arte'], label='M6', color='magenta')

plt.xlabel('Theme')
plt.ylabel('Coverage')
plt.xticks(rotation=45)
plt.legend()
plt.title(f'Total repartition of coverage per theme, and contribution to total coverage, per channel, in {selected_year}')
plt.show()
st.pyplot(plt)

