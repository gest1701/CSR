import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
st.title('CO2 calculator!')
st.write('Welkom op de CO2 calculator!')

categories = ['T-shirt','Hoody','Trousers','Jacket','Socks']
compositions = ['Cotton','Wool','Polyester','Viscose','Acrylic']
printtypes = ['Zeefdruk','Anders...']
transports = ['Air','Boat','Truck']
countries = ['China','Vietnam','Bangladesh','India','Turkey','Portugal']

col1, col2, col3, col4, col5 = st.columns(5)

category = col1.selectbox('Category:', categories)

# Compositie
composition1 = col2.selectbox('Composition',compositions)
percentage1 = col2.number_input('Percentage',min_value=0.0,max_value=100.0,step=5.0,format='%.2f')
composition2 = col2.selectbox('Composition',compositions,key='composition2')
percentage2 = col2.number_input('Percentage',min_value=0.0,max_value=100.0,step=5.0,format='%.2f',key='percentage2')
col2.write(f'Totaal {percentage1+percentage2}%')
if (percentage1+percentage2) < 100:
    col2.error('Totaal minder dan 100%')
elif (percentage1+percentage2) > 100:
    col2.error('Totaal meer dan 100%')

printtype = col3.selectbox('Print type',printtypes,key='printtype')
transport = col4.selectbox('Mode of transport',transports,key='transport')
country = col5.selectbox('Country',countries)



st.write(f'You have selected combination:')
st.write(f'{category} made from {composition1} made in {country}')

# st.balloons()
# st.snow()
if composition1 == 'Wool':
    st.toast('Wol is een verstandige keus!!')
# st.error('Error message')
# st.warning('Warning message')
# st.info('Info message')
# st.success('Success message')
#st.exception(e)



