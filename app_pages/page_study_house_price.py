import streamlit as st
from src.data_management import load_house_price_data, load_pkl_file, load_corr
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
import numpy as np

def page_study_house_price_body():

    # load housing data, correlation coefficients and a dictionary used in encoding
    # object variables
    df = load_house_price_data()
    df_corr = load_corr()
    dic = load_pkl_file('outputs/house_prices_study/v1/dic.pkl')

    # copied from HouseSalePrices study notebook
    strongly_correlated = ['OverallQual', 'GrLivArea', '2ndFlrSF', 'KitchenQual', 'YearBuilt', 'GarageArea', 'GarageFinish']
    moderately_correlated = ['GarageYrBlt', '1stFlrSF', 'TotalBsmtSF', 'YearRemodAdd', 'LotArea', 'LotFrontage', 'BsmtFinSF1']
    dtype_dict = {'OverallQual': 'object', 'GrLivArea': 'numeric', '2ndFlrSF': 'numeric', 'KitchenQual': 'object', 'YearBuilt': 'numeric', 'GarageArea': 'numeric', 'GarageFinish': 'object', 'GarageYrBlt': 'numeric', '1stFlrSF': 'numeric', 'TotalBsmtSF': 'numeric', 'YearRemodAdd': 'numeric', 'LotArea': 'numeric', 'LotFrontage': 'numeric', 'BsmtFinSF1': 'numeric'}

    st.write("## 🏡 Study of House Sales Price")
    st.info(
        f"* The client is interested in discovering how the house attributes correlate with the sale price."
        f" Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.")


    # display housing data dataframe
    if st.checkbox("Inspect housing records dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 15 rows.")
        
        st.write(df.head(15))

    st.write("---")


    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to find  "
        f"the most important variables that influence the sale price of houses.  \n"
        f"The seven most important variables are:  \n**{strongly_correlated}**.  \n\n"
    )

    # Meaning of variables: From README file
    st.info(
        f"Meaning of variables:  \n"
        f"* **{strongly_correlated[0]}**: Rates the overall material and finish of the house.  \n"
        f"* **{strongly_correlated[1]}**: Above grade (ground) living area square feet. \n"
        f"* **{strongly_correlated[2]}**: Second floor square feet. \n"
        f"* **{strongly_correlated[3]}**: Kitchen quality. \n"
        f"* **{strongly_correlated[4]}**: Original construction date. \n"
        f"* **{strongly_correlated[5]}**: Size of garage in square feet. \n"
        f"* **{strongly_correlated[6]}**: Rates the interior finish of the garage. \n"
    )

    st.write(
        f"Seven other variables that are still important but not as much: They show moderate correlation with the sale price:  \n"
        f"**{moderately_correlated}**.  \n"
    )

    # Meaning of variables: From README file
    st.info(
        f"Meaning of variables:  \n"
        f"* **{moderately_correlated[0]}**: Year garage was built.  \n"
        f"* **{moderately_correlated[1]}**: First Floor square feet. \n"
        f"* **{moderately_correlated[2]}**: Total square feet of basement area. \n"
        f"* **{moderately_correlated[3]}**: Remodel date (same as construction date if no remodeling or additions). \n"
        f"* **{moderately_correlated[4]}**: Lot size in square feet. \n"
        f"* **{moderately_correlated[5]}**: Linear feet of street connected to property. \n"
        f"* **{moderately_correlated[6]}**: Type 1 finished square feet of basement area. \n"
    )

    # Heatmap of correlation coefficients above 0.4
    if st.checkbox("Heatmap of the 14 variables in order of importance. We see that the two most important variables"
    " are 'Overall Quality' and 'Above Ground Living Area Square Feet'."):
        heatmap(df_corr)
        
    # Scatterplots of sale price against correlated variable
    if st.checkbox("Scatterplots for the seven most important attributes. They show how sale price increases with "
    "the value of the attribute, for example 'Overall Quality'."):
    
        st.success(
        f"* The plots below confirm the expectation that the stronger the correlation the clearer the trend.  \n"
    )
        st.success(
        f"* We also see that the spread in price increases with price.  \n"
    )
        st.write(f"* Plot Sale Price against attribute")
        scatterplot(df, dic, strongly_correlated, dtype_dict)

# Create a function to display the heatmap from the HouseSalesPriceCorrelation notebook
def heatmap(df):
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    fig, axes = plt.subplots(figsize=(12,5))
    annot_size = 8

    mask = np.zeros_like(df, dtype=np.bool_)
    mask[abs(df) < 0.4] = True

    sns.heatmap(data=df, annot=True, xticklabels=True, yticklabels=True, mask=mask, cmap='viridis', annot_kws={"size": annot_size}, ax=axes, linewidth=0.5)
    
    st.pyplot(fig)

# Create a function to displau the scatterplots from the HouseSalesPriceCorrelation notebook
def scatterplot(df, dic, strongly_correlated, dtype_dict):
    for col in strongly_correlated:
        if df[col].dtype == 'object':
            df1 = df[df[col]!='None']
            df2 = df1[df1[col].notnull()]
            df3[col] = df2[col].replace(dic[col])
        else:
            df1 = df[df[col]!=0]
            df3 = df1[df1[col].notnull()]
        if dtype_dict[col] == 'object':
            fig, axes = plt.subplots(figsize=(8, 5))
            sns.stripplot(data=df3, x=col, y='SalePrice')
            st.pyplot(fig)
        elif dtype_dict[col] == 'numeric':
            fig, axes = plt.subplots(figsize=(8, 5))
            sns.regplot(data=df, x=col, y='SalePrice', scatter_kws={'alpha':0.5}, line_kws={"color":"red"})
            sns.scatterplot(data=df3, x=col, y='SalePrice', alpha=0.5)
            st.pyplot(fig)