import streamlit as st
#layout setting
st.set_page_config(layout="wide")

st.header('Exploratory visualization tools for MPB project')

st.info('''Should you have requests or comments, please feel free to report [issues](https://github.com/NRCAN-NingLiu/mpb_plot_tool/issues) or 
        [pull requests](https://github.com/NRCAN-NingLiu/mpb_plot_tool/pulls) to the [GitHub repository](https://github.com/NRCAN-NingLiu/mpb_plot_tool)
        ''')

col1, col2 = st.columns(2)
with col1:
    st.markdown('To get a choropleth map, please click on :green[choropleth_2columns] on the sidebar. ')
    st.image("input/choropleth1.jpg")

with col2:
    st.markdown('''
                To plot the maps of a site being *treated or infested*, or becoming *detectable or spreading propagules*, please click on :green[first_time_able] on the sidebar. ''')
    st.image("input/v1st.jpg")    


with col1:
    st.markdown('For visualizing data of multiple periods, please click on :green[plot_by_period] on the sidebar. ')
    st.image("input/pbp_1.jpg")

with col2:
    st.markdown('To check the treatment frequency chart, please click on :green[charts] on the sidebar')
    st.image("input/chart.jpg")


