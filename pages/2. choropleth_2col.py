import matplotlib.pyplot as plt
import streamlit as st
import geopandas as gpd
# import seaborn as sns
import pandas as pd

#layout setting
st.set_page_config(layout="wide")
#Load your grids shapefile data
grids = gpd.read_file('input/gridsGEO_m.shp', driver='ESRI Shapefile')

# join three column data
def join_geom(file, geom = grids, **kwargs):
    data = pd.read_csv(file, sep = '\t', header = None, names = ['gridID', 'value'])
    data = geom.merge(data, on = 'gridID', how = 'right')
    return data

col1, col2 = st.columns([1,4])
with col1:
    uploaded_file = st.file_uploader(label = 'Choose file to plot', type = ['txt', 'csv'], accept_multiple_files=False)
    if uploaded_file is not None:
        data = join_geom(uploaded_file)
        check = data['geometry'].isnull().values.all()
        if check:
            st.subheader('Error: Expecting 2 columns input, 3 columns found.')

    # define color scheme
    colorScheme = st.selectbox('Select color palette', ('viridis_r','plasma_r', 'inferno_r', 'magma_r', 'cividis_r', 'RdYlGn_r'))
    # define color scheme
    classScheme = st.selectbox('Select classification scheme', ('std_mean', 'equal_interval', 'fisher_jenks', 
                                                                # 'fisher_jenks_sampled', 'headtail_breaks', 'jenks_caspall', 
                                                                # 'jenks_caspall_forced', 'jenks_caspall_sampled', 'max_p_classifier', 
                                                                'maximum_breaks', 'quantiles', 
                                                                'percentiles', 'natural_breaks'))

    numClass = st.selectbox('Select number of classes', (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

    confirmButton = st.button('Confirm')

with col2:
    if confirmButton:
        tab1, tab2 = st.tabs(['plot', 'raw data'])
        with tab1:
            fig, ax = plt.subplots(1, 1, figsize=(4, 4))
            data.plot(ax=ax,
                column="value",  # Data to plot
                scheme=classScheme,  # Classification scheme
                cmap=colorScheme,  # Color palette
                k=numClass,
                legend=True,  # Add legend
                # legend_kwds={"fmt": "{:.0f}"},  # Remove decimals in legend
            )
            plt.axis('off')
            plt.legend(['Legend'], loc='upper left')
            plt.xlim(-1300000, -800000)
            plt.ylim(7290000, 7850000)
            plt.title(uploaded_file.name)
            st.pyplot(fig)
            
        with tab2:
            st.write(data)
