## Dataset Content

* The App live link is: <https://house-price-prediction-pp5-615997f77e23.herokuapp.com/>

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## Business Requirements

As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

## Hypothesis and how to validate?

1. Suspect that the sale price distribution is skewed to the right (upper quantile), which may lead to outliers and cause issues when predicting the sale price of the four inherited properties.

* To be able to validate this project hypothesis about the distribution we will plot a combined histogram/boxplot of the sales price data.

2. Suspect that although the prediction model takes 3 features to predict the price 'TotalBsmtSF' does not make a massive differnce to sale price 'OverallQual' and 'GrLivArea' have more importance to predict the price.

* To be able to validate this project hypothesis about the importance of specific features to the predicted sales price we will plot a feature importance plot on the ML regressor model page to show that 'TotalBsmtSF' is least important.

## Rationale to map the business requirements to the Data Visualisations and ML tasks

### Business Requirement 1: Data Visualization and Correlation study

1 - As a client I want to be able to visualise the house records data so that I am able to see which variables are important to the sale price of a house.

2 - As as client I want to be able to show a heatmap of the correlation coefficients so that I can order the features by their importance to the sales price.

3 - As a client I want to be able to plot the most important features and how much the variable is correlated with the sales price.

### Business Requirement 2: Classification, Regression and Data Analysis

1 - As a client I want to be able to view and display the inherited houses records data so that I can find a house feature.

2 - As a client I want to use a custom ML model so that I can predict the sale price of my 4 inherited houses.

3 - As a client I want to use that ML model so that I am able to also predict the sale price of any house in the same area.

## ML Business Case

1. What are the business requirements?
* The client is interested in discovering how house attributes correlate with sale prices. Therefore, the client expects data visualizations of the correlated variables against the sale price.
* The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.
2. Is there any business requirement that can be answered with conventional data analysis?
* Yes, we can use conventional data analysis to investigate how house attributes are correlated with the sale prices.
3. Does the client need a dashboard or an API endpoint?
* The client needs a dashboard
4. What does the client consider as a successful project outcome?
* A study showing the most relevant variables correlated to sale price.
Also, a capability to predict the sale price for the 4 inherited houses, as well as any other house in Ames, Iowa.
5. Can you break down the project into Epics and User Stories?
* Information gathering and data collection.
* Data visualization, cleaning, and preparation.
* Model training, optimization and validation.
* Dashboard planning, designing, and development.
* Dashboard deployment and release.
6. Ethical or Privacy concerns?
* No. The client found a public dataset.
7. Does the data suggest a particular model?
* The data suggests a regressor where the target is the sale price.
8. What are the model's inputs and intended outputs?
* The inputs are house attribute information and the output is the predicted sale price.
9. What are the criteria for the performance goal of the predictions?
* We agreed with the client an R2 score of at least 0.75 on the train set as well as on the test set.
10. How will the client benefit?
* The client will maximize the sales price for the inherited properties.

## Dashboard Design

  1. The home page has a summary of the project dataset and outlines the business requirements.
  2. The second page states the project hypothesis' and how I validated them across the project. It shows the distribution of house sale price, a paragraph about the limitations of the model made to predict the sale price and how it is linked to the project hypothesis'.
  3. The third page will show my findings to fullfill the first business requirement. This page consists of the business requirement itself followed by:
      * A tablular view of the dataset.
      * A heatmap of the top correlated coefficients that influence sale price.
      * Scatterplots of the correlated variables against the sale price to visualise the correlation.
      * General conclusion of the findings
  4. The fourth page will show the findings to fullfill the second business requirement. This page consists of a table to show the clients inherited house data, the predicted sales price of each respective property and the sum total of the sale prices. It also has an input with widgets which allow the user to change the input to predict the sale price for a property with those given values base on the new input.
  5. The fifth page has a general conclusions about the ML model performance at the start. Next the pipeline steps are then shown followed by a plot of the importance of each feature in the train set. Finally the R2 score of the ML model and displaying actual sale price against predicted sale price from the model.

## Unfixed Bugs

* There are currently no unfixed bugs

## Deployment

### Heroku

* The App live link is: <https://house-price-prediction-pp5-615997f77e23.herokuapp.com/>
* Set the .python-version Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* numpy==1.26.1
* pandas==2.1.1
* matplotlib==3.8.0
* seaborn==0.13.2
* plotly==5.17.0
* streamlit==1.40.2
* feature-engine==1.6.1
* imbalanced-learn==0.11.0
* scikit-learn==1.3.1
* xgboost==1.7.6

* I used Seaborn to create the heatmap for correlated features and Pandas Profiling to explore the dataset, removing two features due to 90% missing data. 

* I used Matplotlib to create scatterplots comparing predicted and actual prices.

## Credits

* I have used the Code Insitute Template for this project which gave me all the majority of the file structure needed and the readme template to start with.
* I also referred to multiple Code Institute lessons, including the scikit-learn modules and followed the Churnometer walkthrough to improve my understanding.
* I also used youtube videos by 'codebasics' to view other ways of writing the code when I got stuck, I did not use any code copied from these videos but they inspired me to write my own a different way.
* Thanks to my mentor for guiding me in the right direction and to the support channel on Slack for helping me identify the issue causing my error.
* Thanks to my fellow students for sharing their knowledge, time and assisting me when I encountered errors or was unsure how to proceed.

### Content

* I wrote the text for the streamlit dashboard, drawing heavy inspiration from the Churnometer project, as it was the most recent piece of content I worked on. 
* I have used some emoji icons on the streamlit dashboard as I have a MacBook I can implement these via my keyboard

