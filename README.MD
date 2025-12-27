<p align="center"> <!-- Core Languages & ML --> <img src="https://img.shields.io/badge/Python-3.13-blue.svg" alt="Python"> <img src="https://img.shields.io/badge/Machine%20Learning-0078D4.svg" alt="Machine Learning"> <img src="https://img.shields.io/badge/Deep%20Learning-FF6F00.svg" alt="Deep Learning"> <img src="https://img.shields.io/badge/Data%20Science-FFDD00.svg" alt="Data Science"> <img src="https://img.shields.io/badge/Binary%20Classification-4CAF50.svg" alt="Binary Classification"> <img src="https://img.shields.io/badge/Supervised%20Learning-9C27B0.svg" alt="Supervised Learning"> <!-- Libraries --> <img src="https://img.shields.io/badge/Scikit--learn-F7931E.svg" alt="Scikit-learn"> <img src="https://img.shields.io/badge/Pandas-150458.svg" alt="Pandas"> <img src="https://img.shields.io/badge/NumPy-013243.svg" alt="NumPy"> <img src="https://img.shields.io/badge/Matplotlib-005C96.svg" alt="Matplotlib"> <img src="https://img.shields.io/badge/Seaborn-76B900.svg" alt="Seaborn"> <img src="https://img.shields.io/badge/XGBoost-FF6600.svg" alt="XGBoost"> <!-- Backend / APIs --> <img src="https://img.shields.io/badge/FastAPI-009688.svg" alt="FastAPI"> <img src="https://img.shields.io/badge/Pydantic-v2-3776AB.svg" alt="Pydantic v2"> <!-- Cloud & DevOps --> <img src="https://img.shields.io/badge/AWS%20EC2-FF9900.svg" alt="AWS EC2"> <img src="https://img.shields.io/badge/AWS%20S3-569A31.svg" alt="AWS S3"> <img src="https://img.shields.io/badge/Docker-2496ED.svg" alt="Docker"> <!-- Apps & Tools --> <img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg" alt="Streamlit"> <img src="https://img.shields.io/badge/Jupyter-F37626.svg" alt="Jupyter Notebook"> <img src="https://img.shields.io/badge/VS%20Code-007ACC.svg" alt="VS Code"> <img src="https://img.shields.io/badge/macOS%20M1-000000.svg" alt="macOS M1"> <!-- Deployment --> <img src="https://img.shields.io/badge/Deployment-Cloud%20Native-blueviolet.svg" alt="Deployment">
</p>

# WanderWells Travels – Customer Propensity Modeling

*Predicting which customers are most likely to purchase the “Bliss Retreat Wellness Package” using data-driven insights.*


---


## 🌍 Project Overview

WanderWells Travels, a rapidly growing luxury travel company, aims to revolutionize customer targeting for its newest offering — the Zen Escape Wellness Package 🧘‍♀️✨

Previously, marketing campaigns reached customers randomly, leading to high costs and low conversion rates (~19 %).

This project uses machine learning and data analytics to identify which customers are most likely to purchase the new package — helping the marketing team work smarter, not harder.

### 🚀 Live Demo
[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit%20App-FF4B4B?logo=streamlit)](https://wanderwells-customer-propensity.streamlit.app/)


---


## 📊 About the Data

*Dataset Link*

[Tour Package Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/sanamps/tourpackageprediction)


The dataset contains information about customer demographics, behavior, and interactions with the sales team.

The dataset was stored on AWS S3



---


## 🎯 Objective

To build a predictive model that classifies potential customers into two groups:

* Likely to Purchase 🟢

* Not Likely to Purchase 🔴

This helps the marketing team focus resources on the most promising leads, thereby reducing costs and boosting sales.


---


## 📊 Model Performance Results

Performance on Test Set

- Accuracy: 0.95

- F1 Score: 0.87

- Precision: 0.91

- Recall: 0.84


| Class            | Precision | Recall | F1-Score | Support |
| ---------------- | --------- | ------ | -------- | ------- |
| **0**            | 0.96      | 0.98   | 0.97     | 787     |
| **1**            | 0.91      | 0.84   | 0.87     | 191     |
| **Accuracy**     |           |        | 0.95     | 978     |
| **Macro Avg**    | 0.94      | 0.91   | 0.92     | 978     |
| **Weighted Avg** | 0.95      | 0.95   | 0.95     | 978     |


### Business Impact:

Model-selected leads convert at ~91% vs. the original 19% baseline,
delivering a : 

- ⭐ → 4.7× uplift in conversion efficiency


- Confusion Matrix
![Confusion Matrix](assets/cm.png)

- ROC-AUC Curve
![ROC Curve](assets/roc-auc.png)

- P-R Curve
![Precision-Recall Curve](assets/precision-recall.png)




---



🔧 Project Workflow

1. 🔍 Exploratory Data Analysis (EDA)

2. 🧹 Data Preprocessing & Feature Engineering

3. ⚙️ Model Training & Evaluation

4. 🚀 FastAPI Backend for Model Prediction

5. 🐳 Dockerized Model Deployment

6. ☁️ Deployment on AWS EC2

XGBOOST CLASSIFIER was selected as the best-performing classifier model after hyperparameter tuning. 


---


## 🐳 Docker Hub Registry

[![Docker Image](https://img.shields.io/badge/Docker%20Hub-customer--prospenity--api-2496ED?logo=docker)](https://hub.docker.com/repository/docker/isarthak24/customer-prospenity-api/tags)


---


## 🖥️ Tech Stack

| Category                 | Tools                                            |
| ------------------------ | ------------------------------------------------ |
| **Programming Language** | Python 3.13                                      |
| **Frameworks**           | FastAPI, Streamlit                               |
| **Libraries**            | Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, XGBoost |
| **Deployment**           | Docker, AWS EC2                                  |
| **Version Control**      | Git & GitHub                                     |
| **Data Validation**      | Pydantic                                         |
| **IDE**                  | Visual Studio Code, Jupyter Notebook             |


---


## 🏆 Conclusion

This project demonstrates how data-driven marketing can significantly reduce cost and increase conversions in the travel industry.
With predictive modeling, WanderWells Travels can now target the right customers at the right time, enhancing both customer satisfaction and business revenue.


---


## 👨‍💻 Author

Sarthak Sharma

Data Science Student  |  Machine Learning  |  Deep Learning  |   NLP  |  GenAI

[![Email](https://img.shields.io/badge/Email-Write-blue?logo=gmail)](mailto:sarthaksharma@gmail.com)


[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sarthak-sharma-2004/)


