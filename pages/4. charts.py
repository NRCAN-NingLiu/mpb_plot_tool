import altair as alt
import streamlit as st
import seaborn as sns
import pandas as pd
#layout setting
st.set_page_config(layout="wide")

col1, col2 = st.columns([1,3], gap="small")
with col1:
    uploaded_file = st.file_uploader(label = 'select files', type = ['txt', 'csv'], accept_multiple_files=False)
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file, sep = '\t', header = None, names = ['gridID', 'period', 'value'])
        check = data['value'].isnull().values.all()
        if check:
            st.subheader('Error: Expecting 3 columns input, only 2 columns found.')

    ylim = st.slider('Select y axis display range', 0.01, 0.1, 0.05)

    spread = st.number_input('Set min spreading threshold', value=0.02, format="%.4f")
    detect = st.number_input('Set min detectable threshold', value=0.008, format="%.4f")

    confirmButton = st.button('Confirm')

    showData = st.checkbox('show data')
    if showData:
        st.write(data)

with col2:
    if confirmButton:
        chart = alt.Chart(data).mark_point().encode(
            alt.X('period'), 
            alt.Y('value').scale(domain=(0, ylim)),
            tooltip=['gridID', 'period', 'value']
        )
        
        detectLine = alt.Chart(pd.DataFrame({'y': [0.008]})).mark_line().encode(
            y='y',
            # color='g'
        )
        spreadLine = alt.Chart(pd.DataFrame({'y': [0.02]})).mark_line().encode(
            y='y',
            # color='m'
        ).properties(
            width=600,
            height=600
        )
        full_chart = chart + detectLine + spreadLine
        st.altair_chart(full_chart)

