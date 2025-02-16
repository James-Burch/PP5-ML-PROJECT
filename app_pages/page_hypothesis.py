import streamlit as st
from src.snsplot import plot_histogram_and_boxplot
from src.data_management import load_house_price_data

def page_hypothesis_body():

    df = load_house_price_data()

    st.write("## Project Hypothesis and Validation")

    # conclusions taken from HouseSalePrices notebook 
    st.success(
        f"Test"
    )     
   
    st.info(
        f"Test"
    )