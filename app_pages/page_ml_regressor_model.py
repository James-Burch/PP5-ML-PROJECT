import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file



def page_ml_regressor_model_body():
    """ Streamlit page to display ML model details and evaluation. """

    # Define model version
    version = 'v1'
    best_pipeline = load_pkl_file(f"outputs/predict_price/{version}/best_pipeline.pkl")

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
        f"* Our model achieves R² score of **0.87** on the train set ✅. \n"
        f"* Our model also achieves an R² score of **0.77** on the test set ✅"
    )
    st.write("---")

    # Display ML Pipeline
    st.subheader("📌 ML Pipeline")
    st.write(best_pipeline)
    st.write("---")

    # Extract the model from the pipeline
    best_model = best_pipeline.named_steps['model']
    df = pd.read_csv("outputs/datasets/collection/housing_data_cleaned.csv")
    feature_names = ['OverallQual', 'GrLivArea', 'TotalBsmtSF']

    # Feature Importance Plot
    st.subheader("🔍 Feature Importance")
    feature_importance = best_model.feature_importances_
    importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance}).sort_values(by='Importance', ascending=False)

    st.write(X_train.columns.to_list())
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=importance_df['Importance'], y=importance_df['Feature'], palette='coolwarm', ax=ax)
    ax.set_title("Feature Importance")
    ax.set_xlabel("Importance Score")
    ax.set_ylabel("Feature")
    st.pyplot(fig)

    st.subheader("Table to show the correlation of each value with each other")
    st.write(df[['SalePrice', 'OverallQual', 'GrLivArea', 'TotalBsmtSF']].corr())
    st.warning("* We can see that 'TotalBsmtSF' has the lowest correlation with sale price and the rest of the features.")
    st.warning("* Ignore the correlation value '1' as they cannot have a correlation with the same feature")

    # Predictions
    y_train_pred = best_pipeline.predict(X_train)
    y_test_pred = best_pipeline.predict(X_test)

    # Scatterplots: Predicted vs Actual
    st.subheader("Predicted vs. Actual Sale Price Scatter Plots")
    st.info("* For the predictions on houses worth less than £400,000 they follow the black dashed line meaning the predicted follows the actual price.  \n")
    st.warning("* Our model may not be able to predict prices accurately when a house price is higher than £400,000.  \n")

    def plot_predicted_vs_actual(y_actual, y_pred, title):
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(x=y_actual, y=y_pred, alpha=0.5, ax=ax)
        ax.plot([y_actual.min(), y_actual.max()], [y_actual.min(), y_actual.max()], '--', color='black')  # Perfect Prediction
        ax.set_xlabel("Actual Sale Price")
        ax.set_ylabel("Predicted Sale Price")
        ax.set_title(title)
        return fig

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Train Set**")
        st.pyplot(plot_predicted_vs_actual(y_train, y_train_pred, "Train Set: Predicted vs Actual Sale Price"))

    with col2:
        st.write("**Test Set**")
        st.pyplot(plot_predicted_vs_actual(y_test, y_test_pred, "Test Set: Predicted vs Actual Sale Price"))

    st.write(
        "These plots compare the predicted vs actual sale prices. "
        "The **black dashed line** represents perfect predictions."
    )