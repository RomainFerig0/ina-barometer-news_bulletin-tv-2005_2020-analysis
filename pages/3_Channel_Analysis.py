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

#Deletion of null data.
data.dropna()

#%%

st.set_page_config(page_title="Channel Analysis", page_icon="📈")

#Declare axis labels for years, months and channels
years = list(range(2005, 2021))
month_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12]
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
channel_list = ['TF1', 'France 2', 'France 3', 'Canal +', 'Arte', 'M6']

st.title(":blue[Performing advanced analysis on the channels !]")
st.markdown("On this page, you will be able to **target** and **visualize** trends regarding specific channels.")

if "show_mean" not in st.session_state:
    st.session_state.show_mean = False


with st.sidebar:
    st.title('🏂 Channel Data Dashboard')
    
    selected_channel = st.selectbox('Select a TV channel', channel_list)
    
    selected_year = st.selectbox('Select a Year', years)
    selected_year = int(selected_year)
    
    button_show_mean = "Hide Total" if st.session_state.show_mean else "Show Total"

    if st.button(button_show_mean, key="show_mean_button"):
        st.session_state.show_mean = not st.session_state.show_mean

yearly_totals = data.groupby('year_number')['Totaux'].sum().reset_index()
monthly_totals = data.groupby('month_number')['Totaux'].sum().reset_index()
theme_totals = data.groupby('THEMATIQUES')['Totaux'].sum().reset_index()
        
data_channel_theme = data[['THEMATIQUES', selected_channel]]
data_channel_yearly = data[(data['year_number'] == selected_year)]
data_channel_theme_yearly = data_channel_yearly[['THEMATIQUES', selected_channel]]
theme_coverage = data_channel_theme_yearly.groupby('THEMATIQUES')[selected_channel].sum().reset_index()
theme_coverage_total = data_channel_theme.groupby('THEMATIQUES')[selected_channel].sum().reset_index()

data_channel = data[[selected_channel, 'year_number']]
yearly_totals_channel = data_channel.groupby('year_number')[selected_channel].sum().reset_index()
data_channel_m = data[(data[f'{selected_channel}']) & (data['year_number'] == selected_year)]
monthly_totals_channel = data_channel_m.groupby('month_number')['Totaux'].sum().reset_index()


st.markdown(f"### Total TV Coverage per Year for {selected_channel}, from 2005 to 2020")

plt.figure(figsize=(10,6))
if st.session_state.show_mean:
    plt.plot(yearly_totals['year_number'], yearly_totals['Totaux'], color='green', alpha = 0.4, label = 'Total Coverage')

plt.plot(yearly_totals_channel['year_number'], yearly_totals_channel[selected_channel], marker='o', label = 'Coverage by TF1')
plt.xlabel('Year')
plt.ylabel('Coverage')
plt.legend()
plt.title(f"Total TV Coverage per Year for {selected_channel}, from 2005 to 2020")
plt.grid(True)
plt.show()
st.pyplot(plt)

st.markdown(f"### Let's zoom in on year {selected_year} for {selected_channel}...")

plt.figure(figsize=(10,6))
plt.plot(monthly_totals_channel['month_number'], monthly_totals_channel['Totaux'], marker='o', label = f'Total coverage per month on {selected_channel}')
if st.session_state.show_mean:
    plt.plot(monthly_totals['month_number'], monthly_totals['Totaux'], alpha = 0.4, color = 'green', label = 'Total evolution per month')
plt.xlabel('Month')
plt.ylabel('Coverage')
plt.grid(True)
plt.xticks(ticks=month_numbers, labels=month_labels)
plt.legend()
plt.title(f'Evolution of Total TV Coverage on {selected_channel}, for {selected_year}', fontsize=14)
plt.show()
st.pyplot(plt)

st.markdown(f"### Total Coverage Repartition & Contribution per Theme, on {selected_channel}, for {selected_year}")

plt.figure(figsize=(10,6))
if st.session_state.show_mean:
    plt.bar(theme_coverage_total['THEMATIQUES'], theme_coverage_total[selected_channel], color='green', alpha = 0.4, label = 'Total Coverage from 2005 to 2020')
plt.bar(theme_coverage['THEMATIQUES'], theme_coverage[selected_channel], label = f'Coverage by {selected_channel}')
plt.xlabel('Theme')
plt.ylabel('Coverage')
plt.legend()
plt.title(f"Total Coverage Repartition & Contribution per Theme, on {selected_channel}, for {selected_year}")
plt.xticks(rotation=45)
plt.show()
st.pyplot(plt)
