import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')
df= pd.read_csv('census.csv')
list_states= list(df['State'].unique())
list_states.insert(0,'Overall India')

primary= list(df.columns[6:])

st.sidebar.title('Census Dashboard')
state= st.sidebar.selectbox('select state',list_states)

primary_selection= st.sidebar.selectbox('Select primary parameter',primary)
secondary_selection= st.sidebar.selectbox('Select Secondary Parameter',primary)

plot= st.sidebar.button('Plot Graph')

if plot:
    st.title('size indicates primary parameter')
    st.text('colour represents secondary parameter')
    if state == 'Overall India':
        fig= px.scatter_mapbox(df,lat='Latitude', lon='Longitude', zoom=3, hover_name='District',size=primary_selection, color=secondary_selection, mapbox_style= "open-street-map" )
        st.plotly_chart(fig)
    else:
        state_df= df[df['State']== state]

        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', zoom=6, hover_name='District',
                                size=primary_selection, color=secondary_selection, mapbox_style="open-street-map")
        st.plotly_chart(fig)