import streamlit as st
import pandas as pd
import numpy as np
import joblib

# load house price data
@st.cache_data
def load_house_price_data():
    df = pd.read_csv("outputs/datasets/collection/HousePricesRecords.csv")
    return df

# load correlation coefficients
def load_corr():
    df = pd.read_csv("outputs/house_prices_study/v1/corr_mrg.csv")
    return df

# load pkl file
def load_pkl_file(file_path):
    return joblib.load(filename=file_path)