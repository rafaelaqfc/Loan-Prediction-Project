# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
This project has the goal to explore and analyze a dataset about loan in order to understand which group of applicants and co-applicants are more likely to be approved when requesting a loan to a financial institution. After interpreting de dataset, making EDA, cleaning and preprocessing the data, we aimed to create a machine learning model to make loan predictions based on the dataset available and, finally, deploy it to the cloud.

## Hypothesis
Before having any contact with the dataset, we generated some hypothesis from our problem statement and research-question (*Which group of applicants are more likely to be approved to get a loan?*) in order to analyze some of them while we were doing EDA. ven thought we created beforehand 9 hypothesis to be tested, only 3 were analyzed at this moment, such as: if applicants or co-applicants were moslty male, married, with a high-level of education and living in property areas with growth perspectives. As part of our results, we noticed that, altghout the dataset is significate biased in some of the variables that it contains, the group most likely to get a loan is composed of males, who are married, living in semiurban areas and not necessarily graduated. More research is needed in the area though as this dataset is not balanced and, therefore, the results are not accurate.

## EDA Process (Data Exploration, Cleaning and Processing)
During the EDA, we explored the distribution of some variables, such as the applicant and co-applicant income and we noticed that they didn't follow a normal distribution. Processing steps wuch as the log was applied to both variables which were feature enginneered in a new one called 'Total_Income'. 
Besides this, most of this dataset is composed of categorical variables. Therefore, each one of them was explored with the use of visualizations and pivot tables, and, after that, converted to numerical types with different techniques. 
From these results, we could extract the basic demographics from our customers of this dataset. Also, we could see that the dataset is biased towards genre (male), civil status (married) and education (graduate) as there is a larger count of these values in comparison with the others. 
After the EDA, we moved forward to clean the data and these were the steps performed: 
- Missing values were analyzed and filled out with different statistical metrics;
- Extreme values were interpreted and excluded from the dataset with the log transformation applied to some variables (such as loan amount, applicant income and co-applicat income variables).

## Machine Learning Model and Results
Then, with the dataset cleaned, prepared and preprocessed, we created 2 base line models (Logistic Regressor and Random Forest) to classifify the applicants more likely to receive the loan. As Logistic Regressor gave us better evaluation metrics, we used this model to build our final pipeline. 
Finally, our model was deployed in the cloud with Flask (web application) and it has constantly being updated to get better results. 

## Challenges 
One of the main challenges of this project was the time to complete all the steps of data analysis before building the machine learning model, testing it and deploying it in a short time. In addition to that, as we are still making some changes in the application as this is an iterative process, another challenges faced were: 
- How to choose which features can offer better preformance to our model;
- How to balance a dataset biased toward some variables to make ethical and more trustworthy decisions;
- How to make flask work with an API;
- How to deploy the model in AWS (step still in process to be concluded).

## Future Goals
If we had more time, more time would have been spent in the EDA and feature engineering before moving forward in building a base line model. For example, during the EDA, it was noted that the amount of loan status approval was significative bigger than the number of decline, but we didn't have the time to explore this information and its consequences to our machine learning model further. 

## What is included in this repository
In this repository, you can find the following files:
- The original dataset used for the analysis called 'original_customer_dataset.csv' (in 'data' folder);
- The final dataset, cleaned and preprocessed, which was used for the training and testing set called 'df_customer_cleaned_and_processed (in 'data' folder);
- The notebook used for the project called 'notebook_of_loan_prediction' (in 'notebook_and_app' folder);
- The machine learning model created to predict loan applications called 'logistic_regression_model_tunned.p' (in 'notebook_and_app' folder);
- The file created to run the app deployment locally of our model called 'app.py' (in 'notebook_and_app' folder);
- The file created to run the model deployment in AWS called 'app_AWS.py' (in 'notebook_and_app' folder);
- The notebook created to test the deployment of the model in the cloud called 'test_AWS_B' (in 'notebook_and_app' folder);
- The image of our pipeline in the .html format called 'main_pipeline.htmail' (in 'images' folder);
- The presentation file in the .pptx format called 'Presentation.pptx' (in 'images' folder).
