import streamlit as st
import numpy as np
import pandas as pd


# dashboard title
st.title("Real-Time / Live Data Science Dashboard")


@st.cache(allow_output_mutation=True)
def load_data():    
    df_imp = pd.read_json('https://opendata.rdw.nl/resource/m9d7-ebf2.json?$limit=100000000')
    df_imp = df_imp.fillna(0)
    df_imp = df_imp.reset_index(drop=True)
    return df_imp

df = load_data() 

st.dataframe(df)
