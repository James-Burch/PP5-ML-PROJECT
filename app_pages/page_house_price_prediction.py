import streamlit as st
import numpy as np
import pandas as pd
from src.data_management import load_house_price_data, load_pkl_file

def page_house_price_prediction_body():
    
    # load files needed for predicting house prices 
	version = 'v1'
	pipeline = load_pkl_file(f"outputs/predict_price/{version}/best_pipeline.pkl")
	best_features = (pd.read_csv(f"outputs/predict_price/{version}/X_train.csv")
							.columns
							.to_list()
							)
				

	# load inherited houses data
	df = pd.read_csv("inputs/datasets/raw/house-price-20211124T154130Z-001/house-price/inherited_houses.csv")
	
	# predict prices of inherited houses with ML pipeline from PredictSalePrice notebook	
	st.write("### 🏡 House sale prices from client's inherited houses")
	st.write(
        f"* The table below shows the inherited houses data"
	)
	st.write(df.head())
	df = df.filter(best_features)
	house_price_prediction = pipeline.predict(df).round(0)
	df['Predicted House Sale Price'] = house_price_prediction
	st.write(
        f"* The table below shows the predicted sale prices for the four houses, together with the house features used in the prediction, "
		"which are the two of the most important features we saw in the Study House Price page: 'Overall Quality' and 'Above Ground Living "
		"Area Square Feet', however when creating the prediction model it also uses 'Total Basement Size'."
	)
	st.write(df.head())

	# calculate sum of inherited houses predicted prices
	house_price_total = df['Predicted House Sale Price'].sum()
	st.write(
        f"* The sum of the predicted sale prices for the four houses is: &nbsp; &nbsp; &nbsp;{house_price_total}  \n"
	)

	st.write("---")

	# predict price of any other house in Ames, Iowa
	st.write("### Predict house sale prices in Ames, Iowa  \n")
	st.write("* Only the three house attributes 'Above Ground Living Area Sqft', 'Overall Quality' and 'Total Basement Sqft'"
	"are needed for the ML model to predict the price.")
	st.warning("The model has limitations for example the maximum input for the 'TotalBsmtSF' is '6500' "
	"and the maximum input for 'GrLivArea' is '5642' which means the model will not work for larger areas.")
	# create input fields for live data
	X_live = DrawInputsWidgets()
	# predict on live data
	if st.button("Run Predictive Analysis"):
		house_price_prediction = pipeline.predict(X_live.filter(best_features)).round(0)
		st.write(
			f"* The predicted sale price: &nbsp; &nbsp; &nbsp;{house_price_prediction[0]}  \n"
		)

def DrawInputsWidgets():

	# load dataset
	df = load_house_price_data()
	percentageMin, percentageMax = 0.5, 1.0

    # we create input widgets only for the two features we need	
	col1, col2, col3 = st.columns(3)


	# We are using these features to feed the ML pipeline
		
 	# create an empty DF which will keep the live data input
	X_live = pd.DataFrame([], index=[0]) 
	
    # create the widgets for data input

	with col1:
		feature = 'GrLivArea'
		st_widget = st.number_input(
	 		label= feature,
			min_value= df[feature].min()*percentageMin,
			max_value= df[feature].max()*percentageMax,
			value= df[feature].median()
			)
	X_live[feature] = st_widget

	with col2:
		feature = "OverallQual"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].sort_values(ascending=False).unique()
			)
	X_live[feature] = st_widget

	with col3:
		feature = 'TotalBsmtSF'
		st_widget = st.number_input(
	 		label= feature,
			min_value= df[feature].min()*percentageMin,
			max_value= df[feature].max()*percentageMax,
			value= df[feature].median()
			)
	X_live[feature] = st_widget

    # return the predicted sale price calculated from the input widgets

	return X_live        