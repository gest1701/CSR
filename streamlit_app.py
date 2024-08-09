import streamlit as st
from streamlit_tags import st_tags
import pandas as pd

st.set_page_config(layout="wide")
st.title('CO2 calculator!')
st.write('Welkom op de CO2 calculator!')

categories = ['T-shirt','Hoody','Trousers','Jacket','Socks']
compositions = ['Cotton','Wool','Polyester','Viscose','Acrylic']
printtypes = ['Zeefdruk','Anders...']
transports = ['Air','Boat','Truck']
countries = ['China','Vietnam','Bangladesh','India','Turkey','Portugal','Netherlands']

col1, col2, col3, col4, col5,col6,col7,col8 = st.columns(8)

category = col1.selectbox('Category:', categories)

# Compositie
composition1 = col2.selectbox('Composition',compositions)
percentage1 = col2.number_input('Percentage',min_value=0.0,max_value=100.0,step=5.0,format='%.2f')
composition2 = col2.selectbox('Composition',compositions,key='composition2')
percentage2 = col2.number_input('Percentage',min_value=0.0,max_value=100.0,step=5.0,format='%.2f',key='percentage2')
if (percentage1+percentage2) != 100:
    col2.write(f'Totaal {percentage1+percentage2}% ({100-percentage1+percentage2}% over)')
else:
    col2.success(f'Totaal {percentage1 + percentage2}%')
if (percentage1+percentage2) < 100:
    col2.error('Totaal minder dan 100%')
elif (percentage1+percentage2) > 100:
    col2.error('Totaal meer dan 100%')

printtype = col3.selectbox('Print type',printtypes,key='printtype')
country = col4.selectbox('Country',countries)
transport = col5.selectbox('Mode of transport',transports,key='transport')
if (country == 'China' and transport == 'Truck'):
    col5.warning('Are you sure transport is Truck from China?')



st.write(f'You have selected combination:')
st.write(f'{category} made from {composition1} made in {country}')

if composition1 == 'Wool':
    st.toast('Wol is een verstandige keus!!')


#df_all = pd.read_csv('./carbon-intensity-electricity.csv',index_col='Entity') #How to do this online?
url = 'https://big8.nl/data/carbon-intensity-electricity.csv'
df_all = pd.read_csv(url,index_col='Entity')
df_all['Uitstoot gram C02/kWh'] = df_all['Carbon intensity of electricity - gCO2/kWh'].astype(int).astype(str) + ' gram C02/kWh'
df_all['Year'] = df_all['Year'].astype(str)
df_shortlist = df_all[df_all.index.isin(countries)]
st.dataframe(df_shortlist[['Code','Year','Uitstoot gram C02/kWh']])
# df_short = df_all[(df_all.index.isin(countries)) & (df_all.Year==2022)]
# df_short['Jaar'] = df_short['Year'].astype(str)
# df_short['Uitstoot gram C02/kWh'] = df_short['Carbon intensity of electricity - gCO2/kWh'].astype(int).astype(str) + ' gram C02/kWh'
#
# st.dataframe(df_short[['Code','Jaar','Carbon intensity of electricity - gCO2/kWh','Uitstoot gram C02/kWh']],hide_index=False)
#
# chart_data = df_short[['Carbon intensity of electricity - gCO2/kWh']]
# st.bar_chart(chart_data)


# st.balloons()
# st.snow()
# st.error('Error message')
# st.warning('Warning message')
# st.info('Info message')
# st.success('Success message')
#st.exception(e)




uitleg = 'To tackle the impact on the environment, the EU wants to reduce textile waste and increase the life cycle and recycling of textiles. This is part of the plan to achieve a circular economy by 2050.'
st.info(uitleg)

# keywords = st_tags(
#     label='Enter Keywords:',
#     text='Press enter to add more',
#     value=['Zero', 'One', 'Two'],
#     suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four','Rob van Gestel'],
#     maxtags=5,
#     key="aljnf")



st.write('versie 0.4')



