import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file



def page_ml_regressor_model_body():
    """ Streamlit page to display ML model details and evaluation. """

    # Define model version
    version = 'v1'
    best_gb_model = load_pkl_file(f"outputs/predict_price/{version}/best_gb_model.pkl")

    # Load train and test datasets
    X_train = pd.read_csv(f"outputs/predict_price/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/predict_price/{version}/X_test.csv")
    y_train = pd.read_csv(f"outputs/predict_price/{version}/y_train.csv").squeeze()
    y_test = pd.read_csv(f"outputs/predict_price/{version}/y_test.csv").squeeze()

    # Page Title
    st.title("🏡 House Price Prediction - ML Model Evaluation")

    # Summary of model performance
    st.info(
        f"* The target R² score agreed with the client is **0.75+** on both train and test sets.  \n"
        f"* Our model achieves R² score of **0.84** on the test set ✅"
    )
    st.write("---")

    # Display ML Pipeline
    st.subheader("📌 ML Pipeline")
    st.write(best_gb_model)
    st.write("---")

    df = pd.read_csv("outputs/datasets/collection/housing_data_cleaned.csv")
    feature_names = ['OverallQual', 'GrLivArea']  # Top 2 most important features

    # Feature Importance Plot
    st.subheader("🔍 Feature Importance")
    feature_importance = best_gb_model.feature_importances_
    importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance}).sort_values(by='Importance', ascending=False)

    st.write(X_train.columns.to_list())
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=importance_df['Importance'], y=importance_df['Feature'], palette='coolwarm', ax=ax)
    ax.set_title("Feature Importance")
    ax.set_xlabel("Importance Score")
    ax.set_ylabel("Feature")
    st.pyplot(fig)





