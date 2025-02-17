import streamlit as st
import numpy as np
import pandas as pd
from src.data_management import load_house_price_data, load_pkl_file

def page_house_price_prediction_body():
    
    # load files needed for predicting house prices 
	version = 'v1'
	pipeline = load_pkl_file(f"outputs/predict_price/{version}/best_gb_model.pkl")
	best_features = (pd.read_csv(f"outputs/predict_price/{version}/X_train.csv")
							.columns
							.to_list()
							)

	# load inherited houses data
	df = pd.read_csv("inputs/datasets/raw/house-price-20211124T154130Z-001/house-price/inherited_houses.csv")
	
	# predict prices of inherited houses with ML pipeline from PredictSalePrice notebook	
	st.write("### House sale prices from client's inherited houses")
	st.write(
        f"* The table below shows the four inherited houses profile"
	)