"""

    Simple Streamlit webserver application for serving developed classification
    models.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Plase follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
    application. You are expected to extend the functionality of this script
    as part of your predict project.

    For further help with the Streamlit framework, see:

    https://docs.streamlit.io/en/latest/

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
#import spacy
#nlp= spacy.load('en')
#NLP Packages
#from wordcloud import WordCloud
#from textblob import TextBlob

# Vectorizer
#news_vectorizer = open("resources/tfidf_ndu.pkl","rb")
#tweet_cv = joblib.load(news_vectorizer) # loading your vectorizer from the pkl file
#Models
#def load_predictions_models(model_file):
    #load_prediction_models = joblib.load(open(os.path.join(model_file),"rb"))
    #return load_prediction_models

#creating dict keys for predictions
#def get_keys(val,my_dict):
    #for key,value in my_dict.items():
        #if val == value:
            #return key

# Load your raw data
#raw = pd.read_csv("resources/train.csv")

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
