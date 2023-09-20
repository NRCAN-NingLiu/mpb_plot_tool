import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import seaborn as sns

st.set_page_config(layout="wide")

#Load your x-y data - path 
xcoord = pd.read_csv('input/x_coord.txt', sep = '\t', header = None, names = ['gridID', 'x'])
ycoord = pd.read_csv('input/y_coord.txt', sep = '\t', header = None, names = ['gridID', 'y'])
xcoord = xcoord.merge(ycoord, on = 'gridID', how = 'left')

# joining geometry with NodeID - value format input 
def join_geom(file, geom = xcoord, **kwargs):
    data = pd.read_csv(file, sep = '\t', header = None, names = ['gridID', 'period', 'value'])
    data = geom.merge(data, on = 'gridID', how = 'right')
    return data

def get_color(cmap, iter):
    palette = list(reversed(sns.color_palette(cmap, iter).as_hex()))
    return palette

col1, col2 = st.columns([1,3], gap="small")
with col1:
    uploaded_file = st.file_uploader(label = 'select files', type = ['txt', 'csv'], accept_multiple_files=False)
    if uploaded_file is not None:
        raw = join_geom(uploaded_file)
        check = raw['value'].isnull().values.all()
        if check:
            st.subheader('Error: Expecting 3 columns input, only 2 columns found.')
    # define color scheme
    colorScheme = st.selectbox('Select color palette', ('set1', "dark2", 'set2','viridis', 'turbo'))

    confirmButton = st.button('Confirm')

with col2:
    st.subheader('You may click on :blue[legend] to display plot of one specific period :sunglasses:')
    if confirmButton:
        tab1, tab2 = st.tabs(['plot', 'raw data'])

        with tab1:
            data = raw.sort_values(by='period', ascending=False)
            selection = alt.selection_point(fields=['period'])
            color = alt.condition(
                selection,
                alt.Color('period:O').legend(None).scale(scheme=colorScheme),
                alt.value('lightgray'),
            )
            opacity = alt.condition(
                selection,
                alt.value(1),
                alt.value(0.1)
            )

            periods = alt.Chart(data).mark_point(filled=True).encode(
                alt.X('x').scale(domain=(-1300000, -800000)).axis(labels=False), 
                alt.Y('y').scale(domain=(7290000, 7850000)).axis(labels=False),
                color=color,
                opacity=opacity,
                size=alt.Size('value:Q', legend=None, scale=alt.Scale(range=[10, 100]))
            ).properties(
                width=600,
                height=500
            )
            legend = alt.Chart(data).mark_point(size=60).encode(
                alt.Y('period:O').axis(orient='right'),
                color=color,
                opacity=opacity
            ).add_params(
                selection
            )

            full_chart = legend | periods
            st.altair_chart(full_chart) #, use_container_width=True

        with tab2:
            st.write(raw)
