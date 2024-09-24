#Make graphics
import pandas as pd

df_visu = pd.read_csv('population_country_columns.csv')
df_visu = df_visu.drop(columns = ['Unnamed: 0'])

import streamlit as st
#Define the Figure title
st.title('Population plot')

#Define a selector (columns to draw)
columns = st.multiselect('Countries: ',(df_visu.drop(columns = ['year'])).columns)

#Plot the line chart
st.line_chart(df_visu,x = 'year', y = columns, y_label = 'Population',x_label = 'Year')
