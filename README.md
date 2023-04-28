# Loan Prediction Project

## Introduction
We live in an unstable world full of economic inequalities, household challenges and financial disparities. Therefore, most of us rely on loans to pay our expenses or supply and optimize the goods we need to buy to survive. With this context in mind, loan prediction projects are important because they can help, at one side, the people who is really in need; but also, on the other side, financial institutions, such as banks or credit unions, to make better lending decisions. By using advanced data analytics techniques, such as machine learning or predictive modeling, loan prediction models can help us to predict the likelihood of a borrower defaulting on their loan or being able to repay it on time. Thus, this information can be used to optimize the lending process by identifying high-risk borrowers, improving loan approval processes, and reducing the overall risk of default for the financial institution. Additionally, and not less important, loan prediction models can help to increase access to credit for underserved communities or individuals with limited credit history by using alternative data sources to assess creditworthiness.

In addition, loan prediction projects can be used to optimize the financing of the supply chain. When it comes to the optimization of the supply chain, by using loan prediction models, organizations or institutions can identify potential risks or opportunities in the supply chain financing process. For example, a loan prediction model can be used to identify potential delays in payments or supply chain disruptions that could impact cash flow.

## Project Goals
This project has the goal to explore and analyze a dataset about loans in order to understand which group of applicants and co-applicants are more likely to be approved when requesting a loan from a financial institution. After interpreting de dataset, performing EDA, cleaning and preprocessing the data, the goal was to create a machine learning model to make loan predictions based on the dataset available and, finally, deploy it to the cloud.

## Hypothesis
Before having any contact with the dataset, some hypothesis were generated from the problem statement and research-question (*Which group of applicants are more likely to be approved to get a loan?*) to analyze them while we were doing EDA. Even though we created beforehand 9 hypothesis to be tested, only 3 were analyzed at this moment, such as: if applicants or co-applicants were moslty male, married, with a high-level of education and living in property areas with growth perspectives. As part of our results, we noticed that, although the dataset is significant biased in some of the variables that it contains, the group most likely to get a loan is composed of males, who are married, living in semiurban areas and not necessarily graduated. More research is needed in the area though as this dataset is not balanced and, therefore, the results are not accurate.

## Project Steps
1. Data gathering/loading
2. Data exploration (EDA)
3. Text preprocessing
4. Feature engineering
5. Model building, evaluation and hyperparameter tunning
6. Model deployment

## EDA Process (Data Exploration, Cleaning and Processing)
During the EDA, we explored the distribution of some variables, such as the applicant and co-applicant income and we noticed that they didn't follow a normal distribution. Processing steps, such as the log, was applied to both variables which were feature enginneered in a new one called 'Total_Income'. 
Besides this, most of this dataset is composed of categorical variables. Therefore, each one of them was explored with the use of visualizations and pivot tables, and, after that, converted to numerical types with different techniques. 
From these results, we could extract the basic demographics from our customers of this dataset. Also, we could see that the dataset is biased towards genre (male), civil status (married) and education (graduate) as there is a larger count of these values in comparison with the others. 
After the EDA, we moved forward to clean the data and these were the steps performed: 
- Missing values were analyzed and filled out with different statistical metrics;
- Extreme values were interpreted and excluded from the dataset with the log transformation applied to some variables (such as loan amount, applicant income and co-applicat income variables).

## Machine Learning Model and Results
Then, with the dataset cleaned, prepared and preprocessed, we created 2 base line models (Logistic Regressor and Random Forest) to classify the applicants more likely to receive the loan. As Logistic Regressor gave better evaluation metrics, this model was chosen to build the final pipeline.
Finally, our model was deployed in the cloud with Flask (web application) and it has constantly being updated to get better results. 

## Expectations from this Project
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

## Challenges 
One of the main challenges of this project was the time to complete all the steps of data analysis before building the machine learning model, testing it and deploying it in a short time. In addition to that, as we are still making some changes in the application as this is an iterative process, another challenges faced were: 
- How to choose which features can offer better preformance to our model;
- How to balance a dataset biased toward some variables to make ethical and more trustworthy decisions;
- How to make flask work with an API;
- How to deploy the model in AWS (step still in process to be concluded).

## Future Goals
If we had more time, more time would have been spent in the EDA and feature engineering before moving forward in building a base line model. For example, during the EDA, it was noted that the amount of loan status approval was significative bigger than the number of decline, but we didn't have the time to explore this information and its consequences to our machine learning model further. 