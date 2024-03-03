import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
df = pd.read_csv('India.csv')
df.rename(columns = {'literacy rate': 'Literacy Rate', 'sex ratio': 'Sex Ratio'}, inplace = True)
list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')

st.sidebar.title('India Data Visualization')

selected_state = st.sidebar.selectbox('Select a State', list_of_states)
primary = st.sidebar.selectbox('Select a Primary Parameter', sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select a Secondary Parameter', sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')
if plot:
    # plot for India
    st.text('Size represents Primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude',size=primary,
                                color=secondary, zoom=6,size_max=35,hover_name='District',
                                mapbox_style='carto-positron', width=1200, height=700)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.text('Size represents Primary parameter')
        st.text('Color represents secondary parameter')
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary,
                                color=secondary, zoom=6, size_max=35, hover_name='District',
                                mapbox_style='carto-positron', width=1200, height=700)
        st.plotly_chart(fig, use_container_width=True)
