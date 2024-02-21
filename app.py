
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# (Note: Streamlit is imported twice in the provided code, which is redundant.)
import streamlit as st
import random
from PIL import Image
import altair as alt


image_dog = Image.open('dog.png')

st.image(image_nyu, width=100)

st.title("Happy Happy Happy")

st.sidebar.header("Dashboard")
st.sidebar.markdown("---")
app_mode = st.sidebar.selectbox('🔎 Select Method',['Meditation'])
select_dataset =  st.sidebar.selectbox('💾 Select Dataset',["cost"])
df = pd.read_csv("cafe.csv")
list_variables = df.columns
select_variable =  st.sidebar.selectbox('🎯 Select Variable to Predict',list_variables)


if app_mode == 'Visualization':
    st.markdown("## Visualization")
    symbols = st.multiselect("Select two variables", list_variables, ["cost", "low_fat"])
    width1 = st.sidebar.slider("plot width", 1, 25, 10)
    tab1, tab2 = st.tabs(["Line Chart", "📈 Correlation"])
    tab1.subheader("Line Chart")
    st.line_chart(data=df, x=symbols[0], y=symbols[1], width=0, height=0, use_container_width=True)
    st.bar_chart(data=df, x=symbols[0], y=symbols[1], use_container_width=True)
    tab2.subheader("Correlation Tab 📉")
    fig, ax = plt.subplots(figsize=(width1, width1))
    sns.heatmap(df.corr(), cmap=sns.cubehelix_palette(8), annot=True, ax=ax)
    tab2.write(fig)

    st.markdown("### Pairplot")
    df2 = df

    fig3 = sns.pairplot(df2)
    st.pyplot(fig3)
