import streamlit as st
from src.snsplot import plot_histogram_and_boxplot
from src.data_management import load_house_price_data

def page_hypothesis_body():

    df = load_house_price_data()

    st.write("## 🏡 Project Hypothesis and Validation")

    # conclusions taken from HouseSalePrices notebook 
    st.success(
        f"* Suspect that there is few high sales prices in the dataset.  \n"
        f"* The boxplot and histogram below confirms that the histogram extends to the right.  \n"
        f"* The sales price values beyond the average range are called outliers and shown as dots.  \n"
        f"* These dots correspond to sales prices above £466,075.  \n"
    )     

    # Add boxplot and histogram to show the sale price distribution
    df2=df.filter(['SalePrice'])
    plot_histogram_and_boxplot(df2) 
   
    st.info(
        f"* The models created may not be able to predict house prices accurately or at all for values above £400,000.  \n"
        f"* This will be shown in scatterplots on the ML model page.  \n"
        f"* This could be connected to the outliers mentioned above (with sale prices above £466,075), "
        f"we took some steps to improve the model for predicting higher prices, the sale price variable was transformed to make the distribution more symmetrical but more work will be needed.  \n"
    )

    st.success(
        f"* Suspect that although the prediction model takes 3 features to predict the price 'TotalBsmtSF'"
        "does not make a massive differnce to sale price 'OverallQual' and 'GrLivArea' have more importance to predict the price.  \n"
    )

    st.info(
        f"* Please see 'ML Regressor Model' page for the conclusion and evidence backing up this hypothesis."
    )