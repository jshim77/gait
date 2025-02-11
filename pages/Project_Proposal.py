import streamlit as st
import pandas as pd

st.text('Introduction')

	
st.write('1. Introduction/Background: Provide an introduction of your topic and literature review of related work. Briefly explain your dataset and its features, and provide a link to the dataset if possible.')
# ✅Literature Review
# Temporal convolutional autoencoder for unsupervised anomaly detection in time series
# Development and Online Validation of an Intrinsic Fault Detector for a Powered Robotic Knee Prosthesis
# A Deep Learning Framework for End-to-End  Control of Powered Prostheses

# ✅Dataset Description
# Data from 28 sensor channels
# Torque data (Knee and Ankle)

# ✅Dataset Link (if applicable)
# Internal to EPIC Lab

# 2. Problem Definition: Identify a problem and motivate the need for a solution.
# ✅Problem
# Anomalies in prosthesis torque data can lessen accuracy of deep-learning models training on this information.
# Goal: Identify anomalies in powered prosthesis data using an autoencoder.

# ✅Motivation
# Anomalies in prosthesis torque data can lessen accuracy of deep-learning models training on this information. The goal is to create a model using an autoencoder to identify these anomalies, which can then be filtered out of the original data set. Eliminating this bad data will improve the accuracy of the original deep-learning model. 


# 3. Methods: Present proposed solutions including specific data processing methods and machine learning algorithms, and elaborate on why you think each will be effective. It is recommended to identify specific functions/classes in existing packages and libraries (i.e. scikit-learn) rather than coding the algorithms from scratch.
# ✅3+ Data Preprocessing Methods Identified
# Cropping stance and swing phases
# Sensors from the 28 channels may not be in the exact same time frame/collection frequency so may need to interpolate the sensor data
# Adjusting sensor orientation for left/right foot individuals & post-hardware upgrades


# ✅3+ ML Algorithms/Models Identified 
# Autoencoder (find anomalies) -> TCN
# TCN (not filtered by autoencoder)
# Autoencoder (find anomalies) -> CNN
# CNN (not filtered by autoencoder) 
# ✅CS 7641: Unsupervised and Supervised Learning Methods Identified
# Unsupervised - Autoencoder  -  input torque get torque or 28 sensor input to get 28 sensor channels
# Supervised - TCN Deep-learning model - predict knee and ankle torque  - input sensor data get torque


# Autoencoder
# - has layers that get smaller and smaller
# - latent space can store all the data into a small abstract space, like a zip file compressing
# - then this compressed data is passed through bigger and bigger stuff which reconstructs the time sample based on the most compressed version of the data
# - model predicts more common pattern based on the compressed feature
# - then can use this re-expanded data to do anomaly detection
# - based on anomaly detection will retrain deep learning model to see if performance goes up
# - model filter out bad data so another model can train better
# - this structure of big to small to big layers 
# - autoencoder unsupervised

# 4. (Potential) Results and Discussion: Identify several quantitative metrics you plan to use for the project (i.e. ML Metrics). Present goals in terms of these metrics, and state any expected results.
# ✅3+ Quantitative Metrics
# 	RMSE
# 	R2
# 	Dynamic Time Warping (maybe?)
# 	Inference Time`
# ✅Project Goals (recommended to include sustainability and ethical considerations)
# Identify anomalies in powered prosthesis data using an autoencoder.
# Improve accuracy of TCN Deep-Learning Model in predicting torque
# Improve overall gait in transfemoral amputees wearing powered prosthesis
# ✅Expected Results 
# TCN with Autoencoder will perform the best, due to feeding in better filtered data
# Baseline TCN model will successfully assess the effectiveness of the anomaly filter using Autoencoder
# CNN + Autoencoder will have a slower inference time and worse performance than baseline TCN model
# 5. References: Cite relevant papers and articles utilizing the IEEE format. All references in this section must have a matching in-text citation in the body of your proposal text.
# ✅3+ References (preferably peer reviewed)
# ✅1+ In-Text Citation Per Reference
# Seamless and intuitive control of a powered prosthetic leg using deep neural network for transfemoral amputees
# Read auto encoder part
# Other Helpful Resources:
# https://www.jeremyjordan.me/autoencoders/
# Temporal convolutional autoencoder for unsupervised anomaly detection in time series
# Development and Online Validation of an Intrinsic Fault Detector for a Powered Robotic Knee Prosthesis
# A Deep Learning Framework for End-to-End  Control of Powered Prostheses')




