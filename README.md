# Model_Deployment_Monitoring

# Student Performance Prediction API – Model Deployment & Monitoring

                                                                    [![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
                                                                    [![FastAPI](https://img.shields.io/badge/FastAPI-0.95-brightgreen)](https://fastapi.tiangolo.com/)
                                                                    [![Render](https://img.shields.io/badge/Render-Deployment-orange)](https://render.com/)


## Project Overview

                                                                    This project demonstrates the end-to-end workflow of deploying a Student Performance Prediction Machine Learning model as a fully functional cloud API.

The workflow includes:

                                                                  1. Dataset creation  
                                                                  2. Model training and preprocessing pipeline  
                                                                  3. Model serialization  
                                                                  4. API development with FastAPI  
                                                                  5. Deployment-ready configuration files (`requirements.txt`, `Procfile`, `runtime.txt`)  
                                                                  6. Deployment on Render (free tier)  
                                                                  7. Testing and monitoring  

                                                                  The final outcome is a publicly accessible API endpoint for predicting student performance.

## Table of Contents

                                                                  - [Dataset](#dataset)  
                                                                  - [Model Training](#model-training)  
                                                                  - [Serialization](#serialization)  
                                                                  - [API Development](#api-development)  
                                                                  - [Deployment Configuration](#deployment-configuration)  
                                                                  - [Local Testing](#local-testing)  
                                                                  - [GitHub Repository](#github-repository)  
                                                                  - [Render Deployment](#render-deployment)  
                                                                  - [Live API URL](#live-api-url)  
                                                                  - [Sample Prediction](#sample-prediction)  
                                                                  - [Folder Structure](#folder-structure)  
                                                                  - [Implementation Decisions](#implementation-decisions)  
 
## Dataset
  
                                                                 A simulated dataset was created to mimic student performance factors:

                                                                  | study_hours | attendance | previous_grade | assignments_completed | participation | final_score |
                                                                  | 2           | 75         | 60             | 3                   | 2            | 65          |
                                                                  | 5           | 90         | 85             | 5                   | 5            | 90          |
                                                                  | …           | …          | …              | …                   | …            | …           |

                                                           - Features: study hours, attendance, previous grade, assignments completed, participation  
                                                           - Target: `final_score`

                                                            > Screenshot of dataset (optional):

                                                                        ![Dataset Screenshot](Screenshots/dataset.png)

## Model Training

                                                                      - Algorithm: RandomForestRegressor  
                                                                      - Pipeline: `StandardScaler` + `RandomForestRegressor`  
                                                                      - Train/Test Split: 80/20  

                                                                                 python
                                                                                 pipeline = Pipeline([
                                                                                                       ("scaler", StandardScaler()),
                                                                                                           ("model", RandomForestRegressor(n_estimators=200, random_state=42))
                                                                                  ])
                                                                                   pipeline.fit(X_train, y_train)




# Author

# SAMUEL 
