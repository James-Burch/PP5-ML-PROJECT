import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_hypothesis import page_hypothesis_body
# from app_pages.page_study_house_price import page_study_house_price_body
# from app_pages.page_house_price_prediction import page_house_price_prediction_body
# from app_pages.page_ml_regressor_model import page_ml_regressor_model_body

app = MultiPage(app_name= "House Prices in Ames, Iowa") # Create an instance of the app 

# Add app pages using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Project Hypothesis", page_hypothesis_body)
# app.add_page("House Price Study", page_study_house_price_body)
# app.add_page("Predict House Price", page_house_price_prediction_body)
# app.add_page("ML Regressor Model", page_ml_regressor_model_body)

app.run() # Run the app