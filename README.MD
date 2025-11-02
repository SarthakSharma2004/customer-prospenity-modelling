<p align="center">
  <!-- Core -->
  <img src="https://img.shields.io/badge/Python-3.13-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Machine%20Learning-0078D4.svg" alt="Machine Learning">
  <img src="https://img.shields.io/badge/Data%20Science-FFDD00.svg" alt="Data Science">

  <!-- Frameworks -->
  <img src="https://img.shields.io/badge/FastAPI-009688.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg" alt="Streamlit">
  <img src="https://img.shields.io/badge/Pydantic-3776AB.svg" alt="Pydantic">

  <!-- Tools & Libraries -->
  <img src="https://img.shields.io/badge/Scikit--learn-F7931E.svg" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/XGBoost-FF6600.svg" alt="XGBoost">
  <img src="https://img.shields.io/badge/Pandas-150458.svg" alt="Pandas">
  <img src="https://img.shields.io/badge/Numpy-013243.svg" alt="NumPy">
  <img src="https://img.shields.io/badge/Matplotlib-005C96.svg" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Seaborn-76B900.svg" alt="Seaborn">

  <!-- Infrastructure -->
  <img src="https://img.shields.io/badge/AWS%20EC2-FF9900.svg" alt="AWS EC2">
  <img src="https://img.shields.io/badge/Render-46E3B7.svg" alt="Render">
  <img src="https://img.shields.io/badge/Docker-2496ED.svg" alt="Docker">
  <img src="https://img.shields.io/badge/GitHub-181717.svg" alt="GitHub">

  <!-- Environment -->
  <img src="https://img.shields.io/badge/Jupyter-F37626.svg" alt="Jupyter Notebook">
  <img src="https://img.shields.io/badge/VS%20Code-007ACC.svg" alt="VS Code">
  <img src="https://img.shields.io/badge/macOS-000000.svg" alt="macOS M1">

  <!-- Extras -->
  <img src="https://img.shields.io/badge/Model%20API-FastAPI%20Backend-green.svg" alt="Model API">
  <img src="https://img.shields.io/badge/Deployment%20Platform-Cloud%20Native-blueviolet.svg" alt="Deployment">
</p>


# WanderWells Travels – Customer Propensity Modeling

*Predicting which customers are most likely to purchase the “Bliss Retreat Wellness Package” using data-driven insights.*


## 🌍 Project Overview

WanderWells Travels, a rapidly growing luxury travel company, aims to revolutionize customer targeting for its newest offering — the Zen Escape Wellness Package 🧘‍♀️✨

Previously, marketing campaigns reached customers randomly, leading to high costs and low conversion rates.

This project uses machine learning and data analytics to identify which customers are most likely to purchase the new package — helping the marketing team work smarter, not harder.


## 🎯 Objective

To build a predictive model that classifies potential customers into two groups:

* Likely to Purchase 🟢

* Not Likely to Purchase 🔴

This helps the marketing team focus resources on the most promising leads, thereby reducing costs and boosting sales.


## 📊 About the Data

*Dataset Link*

[Tour Package Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/sanamps/tourpackageprediction)


The dataset contains information about customer demographics, behavior, and interactions with the sales team.


## 🧠 Approach

1. 🔍 Exploratory Data Analysis (EDA)

* Identified correlations between income, occupation, and package purchase rate

* Visualized demographic patterns using Seaborn and Matplotlib


2. 🧹 Data Preprocessing

Handled missing values

Encoded categorical features 

Scaled numerical features

Created new impactful features from existing ones


3. 🤖 Model Development 

Trained multiple classification models:

* XGBoost
* Random Forest
* GradientBoostingClassifier
* AdaBoostClassifier
* Decision Tree
* Logistic Regression
* Support Vector Classifier (SVC)

XGBOOST CLASSIFIER was selected as the best-performing classifier model after hyperparameter tuning. 

## 🌐 Model Deployment

Exposed model predictions via FastAPI , Dockerised the API and deployed it on AWS (EC2)
Integrated frontend using Streamlit , deployed using render

🐳 [Docker Image] (https://hub.docker.com/repository/docker/isarthak24/customer-prospenity-api/general)


## 🖥️ Tech Stack

| Category                 | Tools                                            |
| ------------------------ | ------------------------------------------------ |
| **Programming Language** | Python 3.13                                      |
| **Frameworks**           | FastAPI, Streamlit                               |
| **Libraries**            | Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn |
| **Deployment**           | Docker, AWS EC2                                  |
| **Version Control**      | Git & GitHub                                     |
| **Data Validation**      | Pydantic                                         |
| **IDE**                  | Visual Studio Code, Jupyter Notebook             |



## Project Structure :

WanderWells_Travels_Propensity_Model/
│
├── Data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
|
├── artifacts/
|   ├── best_model_pipeline.pkl  
|   ├── model.pkl
|   ├── preprocessor.pkl
|
├── notebooks/
│   ├── Prospenity_Modelling.ipynb
│ 
├── logs/
|   ├── logs                      # contains all the logs of the model pipeline
|    
├── schema/
│   ├── prediction_response.py    # Pydantic Model to validate response
│   ├── user_input.py             # Pydantic Model to validate user input               
│
├── src/
│   └── data_ingestion.py                              # Frontend Interface
│   └── preprocessing.py
|   └── model_training.py 
|
├── utils/
|   └── logger.py 
|
├── pipeline.py                   # Orchestrates all scripts in src folder
├── main.py                       # FastApi code
├── predict.py                    # A utility function used in main.py
├── app.py                        # Streamlit frontend
├── .dockerignore               
├── Dockerfile
├── .gitignore
├── requirements.txt              # For containerisation
├── requirements-dev.txt          # For creating the enviornment
└── README.md



## KPI And Insights

* Male Customers from Tier 1 cities, aged 30-40 having Large Businesses had highest conversion rates
* Male Customers from Tier 3 cities, having Small Businesses had goood conversion rates
* Salaried Female Customers from Tier 3 cities had also bought the package
* Self Enquiry type contacts had better conversion rates than Company Invited.
* Customers who enquired for Basic package converted the most
* Unmarried customers had better conversion rate than Married


## 🏆 Conclusion

This project demonstrates how data-driven marketing can significantly reduce cost and increase conversions in the travel industry.
With predictive modeling, WanderWells Travels can now target the right customers at the right time, enhancing both customer satisfaction and business revenue.


## 👨‍💻 Author

Sarthak Sharma
Data Science Student | Machine Learning , Deep Learning , NLP , GenAI Enthusiast

📧 [Email Me](2sarthaksharma@gmail.com)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sarthak-sharma-2004/)


