# Heart-Failure-Prediction

<p align="center">
  <img src="https://images.squarespace-cdn.com/content/v1/5daddb33ee92bf44231c2fef/e163d977-3fe5-42da-b959-5b5319027458/machine-learning-in-healthcare.jpg" alt="Title" width="650px" height="249px">
</p>

Data analysis and Machine Learning approach to Heart Failure Prediction.

[LINK](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data/data) to the dataset on Kaggle.

## Overview

Cardiovascular diseases (CVDs) stand as the leading cause of death globally, claiming approximately 17.9 million lives each year. Heart failure, a common consequence of CVDs, significantly contributes to this mortality rate. This project is dedicated to leveraging Machine Learning techniques to predict mortality caused by heart failure, enabling early intervention and tailored patient management strategies. The dataset comprises 12 features predictive of heart failure mortality, aiming to support healtchare professionals in making informed decisions.

## Dataset Description

The dataset includes the next features (12 for prediction and DEATH_EVENT):

- Age: Patient's age, a critical risk factor.
- Anaemia: Presence of anaemia, a condition marked by low hemoglobin levels.
- Creatinine Phosphokinase (CPK): Enzyme levels indicating heart muscle stress.
- Diabetes: Patient's diabetes status, a known risk factor for heart disease.
- Ejection Fraction: Measurement of the heart's efficiency in pumping blood.
- High Blood Pressure: Presence of hypertension, a significant heart disease risk factor.
- Platelets: Blood platelet count, essential for clotting.
- Serum Creatinine: Kidney function indicator, relevant for cardiovascular health.
- Serum Sodium: Levels of sodium in the blood, with imbalances indicating heart failure.
- Sex: Biological sex, influencing heart disease risk and outcomes.
- Smoking: Smoking status, a major cardiovascular risk factor.
- Time: Duration of follow-up, essential for outcome analysis.
- Death Event: Indicates if a heart failure mortality event occurred.
  
## Project Structure

### Part 1: Data Preparation and Analysis

<p align="center">
  <img src="https://i.ytimg.com/vi/yOmxJbZjTnU/maxresdefault.jpg" alt="Title" width="300px" height="150px">
</p>

During this first phase of the project I will be performing several data cleaning queries through MySQL, addressing missing values, outliers and inconsistencies. Now that the data is ready I will enhance the dataset with the creation of new features that will further improve the model and finally create a pipeline that connects this new dataset to Python so I can perform an EDA (Exploratory Data Analysis) to uncover patterns and relationships.

Analyzing the dataset through visualization will help uncover patterns, trends, and correlations among the features. This step is critical for understanding the factors that contribute most significantly to heart failure mortality.

Once important questions have been solved thanks to the visuals, we can start building our Heart Failure Prediction Model, thanks to the use of a cloud platform like Snowflake. First of all we have to pipeline our current data from MySQL to the cloud, I we will use code within the same file as before.

### Part 2: Machine Learning Model Development

<p align="center">
  <img src="https://datasense.be/wp-content/uploads/snowflake-cloud-data-warehouse-data-vault-e1639652727931.png" alt="Title" width="300px" height="90px">
</p>

In this phase, I focus on applying various Machine Learning algorithms to predict mortality due to heart failure. My approach involves utilizing a combination of Logistic Regression, Random Forest Classifier, Support Vector Machine (SVM), and XGBoost models.

Each model is trained on a dataset processed to highlight features relevant to predicting heart failure outcomes. I perform feature scaling to ensure my models can interpret the data effectively, given the wide range of values across different features.

The process involves:

Data Preprocessing: Including feature scaling and splitting the dataset into training and testing sets.
Model Training: Where each model is trained on the training set.
Model Prediction: Utilizing the trained models to make predictions on the test set.
Performance Evaluation: Assessing each model's accuracy to determine its effectiveness in predicting heart failure mortality.
This rigorous approach allows me to compare the predictive power of each algorithm and select the most suitable model for deployment.

### Part 3: Results and Discussion
The evaluation of my models yielded the following accuracies:

- Logistic Regression Model Accuracy: 80%
- Random Forest Classifier Accuracy: 75%
- Gradient Boosting Classifier Accuracy: 73.33%
- Support Vector Machine Accuracy: 75%

With some hyperparameter tuning we can get the Logistic Regression Model up to 85.37%, but that is not enough! I will be looking into ways of improving this number to be over 90%, as this is the milestone I want this model to achieve.

<p align="center">
  <img src="https://i.imgur.com/2RehOsS.png" alt="Title" width="750px" height="431px">
</p>

These results demonstrate the potential of Machine Learning in enhancing the prediction of heart failure mortality. The Random Forest Classifier emerged as the top-performing model, with an accuracy of over 80%. This model's success can be attributed to its ability to handle the complexity and non-linearity within our dataset, providing a more nuanced understanding of the factors influencing heart failure mortality.

## Discussion
The findings from this project underscore the importance of leveraging advanced analytics and machine learning in healthcare. By accurately predicting heart failure mortality, I can help healthcare professionals tailor interventions and management strategies to individual patient needs, ultimately improving patient outcomes.

It is crucial to note that while the models show promising results, the deployment of such models in a clinical setting requires further validation and testing. Additionally, incorporating more patient data and potentially relevant features could further enhance model performance.

## Future Work
Moving forward, I aim to:

- Explore the incorporation of additional features that could improve model accuracy.
- Implement more advanced machine learning techniques, such as deep learning, to assess their performance in predicting heart failure mortality.
- Conduct a more extensive validation of my models using a larger and more diverse dataset to ensure their robustness and reliability in various clinical settings.
