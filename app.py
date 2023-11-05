import warnings
import dashboard
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
warnings.filterwarnings('ignore')

st.set_page_config(layout='wide')

# Header
dashboard.header()

# Option Menu
st.markdown('#')
option=dashboard.option_container()

if option == 'Home':
    st.markdown('#')
    dashboard.home()

elif option == 'Analysis':
    st.markdown('#')
    dashboard.analysis()

elif option == 'Geo':
    st.markdown('#')
    dashboard.geo()