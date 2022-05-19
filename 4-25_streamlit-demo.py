#Import libraries
#from re import X
import streamlit as st
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

#Load and clean data
data = sns.load_dataset('penguins')
data['bill_length_mm'].fillna(data['bill_length_mm'].mean(), inplace=True)
data['bill_depth_mm'].fillna(data['bill_depth_mm'].mean(), inplace=True)
data['flipper_length_mm'].fillna(data['flipper_length_mm'].mean(), inplace=True)
data['body_mass_g'].fillna(data['body_mass_g'].mean(), inplace=True)
data['sex'].fillna(data['sex'].value_counts().index[0], inplace=True)
data = data.astype({"bill_length_mm":'int', "bill_depth_mm":'int', "flipper_length_mm":'int', "body_mass_g":'int'}) 

#Creating more user-friendly option labels
data.rename(columns = 
    {"flipper_length_mm": "flipper length", 
    "bill_length_mm":"bill length",
    "bill_depth_mm":"bill depth",
    "body_mass_g":"body mass"},
    inplace = True)
featureset = ['flipper length', 'bill length', 'bill depth', 'body mass', 'island', 'sex', 'species']
graphset = ["Histogram", "Box Plot", "Enhanced Box Plot", "Strip Plot", "Violin Plot", "Swarm Plot"]

#Give out dashboard a title
st.title('Customer dashboard')

#Show the raw data
st.subheader('Raw data')
st.write(data)

#Let the user choose graph, features, etc.
st.subheader('Visualization')
col1, col2 = st.columns(2)
with col1: 
    st.subheader('Choices')
    title = st.text_input('Enter a title for the chart')
    kind1 = st.selectbox('Pick plot for left side', graphset, key="pl")
    x = st.selectbox("Feature for x:", featureset, key="f1l")
    if kind1 != "Histogram":
        y = st.selectbox("Feature for y:", featureset, key="f2l")
        hue = st.selectbox("Feature for hue:", (featureset), key="h2l")
    if kind1 == "Histogram": 
        kde = st.selectbox("Do you want to add a kde?", (True, False), key="k1")
        color1 = st.color_picker('Pick a color for Plot 1', key="c1")
#Then view the graph
with col2:
    fig = plt.figure(figsize=(7, 5))
    if kind1 == "Histogram": sns.histplot(data = data, x = x, kde = kde, color = color1)
    if kind1 == "Box Plot": sns.boxplot(data = data, x = x, y = y, hue = hue)
    if kind1 == "Enhanced Box Plot": sns.boxenplot(data = data, x = x, y = y, hue = hue)
    if kind1 == "Strip Plot": sns.stripplot(data = data, x = x, y = y, hue = hue)  
    if kind1 == "Violin Plot": sns.violinplot(data = data, x = x, y = y, hue = hue)
    if kind1 == "Swarm Plot": sns.swarmplot(data = data, x = x, y = y, hue = hue)
#User can input a title for the graph
    plt.title(title)
    st.pyplot(fig)
