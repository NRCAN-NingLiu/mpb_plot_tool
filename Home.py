import streamlit as st
#layout setting
st.set_page_config(layout="wide")

st.header('Exploratory visualization tools for MPB project')

st.info('''Should you have requests or comments, please feel free to report [issues](https://github.com/NRCAN-NingLiu/mpb_plot_tool/issues) or 
        [pull requests](https://github.com/NRCAN-NingLiu/mpb_plot_tool/pulls) to the [GitHub repository](https://github.com/NRCAN-NingLiu/mpb_plot_tool)
        ''')

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.subheader('choropleth map')
    st.write('takes two columns input like:')
    st.image('img/input2col.png', width=120)
    st.write('Map will be plotted on a open street basemap, potential to change/add basemap, make request if needed.')
    st.image("img/choropleth1.JPG")

with col2:
    st.subheader('first time plots')
    st.write('takes three columns input like:')
    st.image('img/input3col.JPG', width=150)
    st.markdown('''
                To plot the maps of a site being *treated or infested*, or becoming *detectable or spreading propagules*
                 ''')
    st.image("img/all1st.JPG")    


with col3:
    st.subheader('plot by period')
    st.write('takes three columns input like:')
    st.image('img/input3col.JPG', width=150)   
    st.write('After plotting, you may lick on the legend to show plot of each period') 
    st.image("img/pbp_all.png")
    st.image("img/pbp_2.jpg")

with col4:
    st.subheader('charts')
    st.write('takes three columns input like:')
    st.image('img/input3col.JPG', width=150)
    st.write('Plotting treatment frequency chart currently. ')
    st.image("img/chart.JPG")


