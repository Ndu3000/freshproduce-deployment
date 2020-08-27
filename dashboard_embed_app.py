"""

    Simple Streamlit webserver application for serving developed embedding
    a dashboard visualisation in streamlit.

"""
# Streamlit dependencies
import streamlit as st
import joblib,os
from sklearn.feature_extraction.text import CountVectorizer
# Data dependencies
import pandas as pd
import numpy as np
#import pprint
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
# Set plot style for data visualisation
sns.set()
from PIL import Image


# Vectorizer


#creating dict keys for predictions


# Load your raw data
#raw = pd.read_...

# The main function where we will build the actual app
def main():
    """Dashboard with Streamlit """

    # Creates a main title and subheader on your page -
    # these are static across all pages
    st.title("Dashboard Test")

    # Using PIL

    # Creating sidebar with selection box -
    # you can create multiple pages this way
    options = ["Data Studio", "Power BI"]
    selection = st.sidebar.selectbox("Choose Option", options)

    # Building out the "Information" page
    if selection == "Data Studio":
        #image = Image.open('img5.png')
        #st.image(image, caption=None, use_column_width=True)
        #st.info("General Information")
        # You can read a markdown file from supporting resources folder
        st.subheader("Google Data Studio")
        st.subheader("==========================================================")
        st.subheader("Dashboard embedding test")
        st.subheader("==========================================================")
        st.markdown("""
        <iframe width="1100" height="1000" src="https://datastudio.google.com/embed/reporting/1uYIXuUFbGwMA8Y8R2JFenPNG3fjuCaGG/page/mpeW" frameborder="0" style="border:0" allowfullscreen></iframe>
        """, unsafe_allow_html=True)

    if selection == "Power BI":
        #image = Image.open('img5.png')
        #st.image(image, caption=None, use_column_width=True)
        #st.info("General Information")
        # You can read a markdown file from supporting resources folder
        st.subheader("Power BI")
        st.subheader("==========================================================")
        st.subheader("Dashboard embedding test")
        st.subheader("==========================================================")
        st.markdown("""
        <iframe width="900" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiZDFkMTdmYTgtZmNhOS00YzNhLWEzOTktMzliYzM3NDU1MzRjIiwidCI6IjM0MTgzODVmLTVhNjMtNDg3Ny04MDNkLTMzMjg4MjhmZTc3ZiJ9" frameborder="0" style="border:0" allowfullscreen></iframe>
        """, unsafe_allow_html=True)








# Required to let Streamlit instantiate our web app.
if __name__ == '__main__':
    main()
