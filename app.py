import streamlit as st
from data_checker import PATH, IEMOCAP, CLASS
import pandas as pd
import pickle

st.set_page_config(
     layout="wide"
)

Name='iemocap'

@st.cache()
def load_data(path):
    with open(path, 'rb') as f:
        data = pickle.load(f, encoding='latin1')
    return data

st.header(Name+'DataSet')
data=load_data(PATH[Name])

data=CLASS[Name](data)

st.table(pd.DataFrame(data.random_one()))

st.button('Change One')