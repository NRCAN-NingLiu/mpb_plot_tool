import streamlit as st
import geopandas as gpd
import pandas as pd
import numpy as np
# import folium
# from streamlit_folium import st_folium
import leafmap.foliumap as leafmap

#layout setting
st.set_page_config(layout="wide")
#Load your grids shapefile data
geom = gpd.read_file('input/gridsGEO.shp', driver='ESRI Shapefile')
# geom = pd.read_csv('input/nodesGEOM.txt', sep='\t', header=0)
center = [55.83, -113.68]

# join three column data
def join_geom(file, geom = geom, **kwargs):
    data = pd.read_csv(file, sep = '\t', header = None, names = ['gridID', 'value'])
    for col in data.columns:
        if data[col].isnull().values.all():
            data.drop(labels=col, axis=1, inplace=True)
    data = geom.merge(data, on = 'gridID', how = 'right')
    return data


uploaded_file = st.file_uploader(label = 'Choose file to plot', type = ['txt', 'csv'], accept_multiple_files=False)
if uploaded_file is not None:
    data = join_geom(uploaded_file)
    # dataGJ = data.__geo_interface__

confirmButton = st.button('Confirm')

if confirmButton:
    tab1, tab2 = st.tabs(['plot', 'raw data'])
    with tab1:
        m = leafmap.Map(location=center, zoom_start=6)
        m.add_gdf(data, layer_name = uploaded_file.name)
        m.to_streamlit(height=700)
    with tab2:
        st.write(data)     

    

