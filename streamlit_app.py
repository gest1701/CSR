import streamlit as st
# from streamlit_tags import st_tags
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title('CO2 calculator!')
st.write('Welkom op de CO2 calculator!')

categories = ['T-shirt','Hoody','Trousers','Jacket','Socks']
compositions = ['Cotton','Wool','Polyester','Viscose','Acrylic']
printtypes = ['Zeefdruk','Anders...']
transports = ['Air','Boat','Truck']
countries = ['China','Vietnam','Bangladesh','India','Turkey','Portugal']
colors = ['Dark','Mid','Light']
#st.logo('logo.png')

co2_emissions = {
    "China": {
        "Rotterdam": {
            "Air": 2500,    # kg CO2 per ton
            "Boat": 150,    # kg CO2 per ton
            "Truck": 2000   # kg CO2 per ton
        }
    },
    "Vietnam": {
        "Rotterdam": {
            "Air": 2400,    # kg CO2 per ton
            "Boat": 120,    # kg CO2 per ton
            "Truck": 1800   # kg CO2 per ton
        }
    },
    "Bangladesh": {
        "Rotterdam": {
            "Air": 2300,    # kg CO2 per ton
            "Boat": 100,    # kg CO2 per ton
            "Truck": 1700   # kg CO2 per ton
        }
    },
    "India": {
        "Rotterdam": {
            "Air": 2000,    # kg CO2 per ton
            "Boat": 130,    # kg CO2 per ton
            "Truck": 1600   # kg CO2 per ton
        }
    },
    "Turkey": {
        "Rotterdam": {
            "Air": 1200,    # kg CO2 per ton
            "Boat": 80,     # kg CO2 per ton
            "Truck": 500    # kg CO2 per ton
        }
    },
    "Portugal": {
        "Rotterdam": {
            "Air": 400,     # kg CO2 per ton
            "Boat": 50,     # kg CO2 per ton
            "Truck": 300    # kg CO2 per ton
        }
    }
}


col1, col2, col3, col4, col5,col6,col7,col8 = st.columns(8)
category = col1.selectbox('Category of stuff:', categories)

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
embroidery_time = col4.number_input('Embroidery time (minutes)',min_value=0.0,max_value=60.0,step=1.0,value=5.0,format='%.2f',key='embroidery_time')
garment_weight = col5.number_input('Garment weight (gr)',min_value=0.0,max_value=100.0,step=1.0,value=5.0,format='%.2f',key='garment_weight')
buttons_qty = col6.number_input('Buttons qty',min_value=0,max_value=10,step=1,value=1,key='buttons_qty')
zippers_qty = col7.number_input('Zippers qty',min_value=0,max_value=10,step=1,value=1,key='zippers_qty')
color = col8.selectbox('Color',colors)


st.write('**Origin and transport to Rotterdam**')
col1, col2, col3, col4, col5,col6,col7,col8 = st.columns(8)
country = col1.selectbox('Country',countries)
transport = col2.selectbox('Mode of transport',transports,key='transport')

co2_transport = co2_emissions[country]['Rotterdam'][transport]
col3.write(' ')
#col3.write(' ')
col3.success(f'{co2_transport} kg C02 per ton')

if (country == 'China' and transport == 'Truck'):
    col4.warning('Are you sure transport is Truck from China?')
st.write(f'You have selected combination: **{category} made from {composition1} made in {country}**')

if composition1 == 'Wool':
    st.toast('Wol is een verstandige keus!!')


#df_all = pd.read_csv('./carbon-intensity-electricity.csv',index_col='Entity') #How to do this online?
st.subheader('CO2 output for electricty production')
gcol1, gcol2,gcol3, gcol4= st.columns(4)
url = 'https://big8.nl/data/carbon-intensity-electricity.csv'
df_all = pd.read_csv(url,index_col='Entity')
df_all['Uitstoot gram C02/kWh'] = df_all['Carbon intensity of electricity - gCO2/kWh'].astype(int).astype(str) + ' gram C02/kWh'
df_all['Year'] = df_all['Year'].astype(str)
df_shortlist = df_all[df_all.index.isin(countries)]
df_shortlist_2023 = df_shortlist[df_shortlist['Year']=='2023']
gcol1.write('Gram C02 per kWh in tabel')
gcol1.dataframe(df_shortlist_2023[['Code','Year','Uitstoot gram C02/kWh']])
gcol2.write('Gram C02 per kWh')
gcol2.bar_chart(df_shortlist_2023,x='Code',y=['Carbon intensity of electricity - gCO2/kWh'])
gcol3.write('Gram C02 per kWh vanaf 2013')
gcol3.line_chart(df_shortlist[df_shortlist['Year']>'2012'],x='Year',y=['Carbon intensity of electricity - gCO2/kWh'],color='Code')
# st.line_chart(df_shortlist,x='Year',y=['Carbon intensity of electricity - gCO2/kWh'])
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



st.write('versie 0.5.1')



