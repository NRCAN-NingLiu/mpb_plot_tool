import leafmap.foliumap as leafmap
import streamlit as st
import geopandas as gpd
# import seaborn as sns
import pandas as pd

#layout setting
st.set_page_config(layout="wide")
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #3182bd;
    color:#ffffff;
}
</style>""", unsafe_allow_html=True)

#Load your grids shapefile data
grids = gpd.read_file('input/gridsGEO.shp', driver='ESRI Shapefile')
center = [55.83, -113.68]

# join three column data
def join_geom(file, geom = grids, **kwargs):
    data = pd.read_csv(file, sep = '\t', header = None, names = ['gridID', 'value'])
    data = geom.merge(data, on = 'gridID', how = 'right')
    return data

uploaded_file = st.file_uploader(label = 'Choose a file to plot', type = ['txt', 'csv'], accept_multiple_files=False)
if uploaded_file is not None:
    data = join_geom(uploaded_file)
    check = data['geometry'].isnull().values.all()
    if check:
        st.subheader('Error: Expecting 2 columns input, 3 columns found.')

col1, col2, col3, col4 = st.columns([0.6, 0.8, 0.6, 0.6])
with col1:
    # define color scheme
    colorScheme = st.selectbox('Color palette', ('viridis_r','plasma_r', 'inferno_r', 'magma_r', 'cividis_r', 'RdYlGn_r'))
with col2:
    # define color scheme
    classScheme = st.selectbox('Classification scheme', ('FisherJenks', 'BoxPlot', 'EqualInterval', 
                                                         'NaturalBreaks', 'Quantiles', 'Percentiles', 'StdMean'))
with col3:
    numClass = st.selectbox('Number of classes', (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
with col4:
    confirmButton = st.button(label="Confirm")

if confirmButton:
    tab1, tab2 = st.tabs(['plot', 'raw data'])
    with tab1:
        m = leafmap.Map(
            location=center, 
            width=600,
            height=600,
            draw_control=False,
            measure_control=False,
            fullscreen_control=False)
        data0 = data.copy()
        m.add_data(data0, 
            column='value',
            scheme=classScheme,
            cmap=colorScheme,
            k=numClass,
            legend_title=uploaded_file.name,
            layer_name=uploaded_file.name)
        m.to_streamlit(height=700)
        
    with tab2:
        st.write(data)
