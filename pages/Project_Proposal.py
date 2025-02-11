import streamlit as st
import pandas as pd

st.text('Introduction')

	
st.write('1. Introduction/Background') 
st.write('Provide an introduction of your topic and literature review of related work. Briefly explain your dataset and its features, and provide a link to the dataset if possible.')
st.write('✅Literature Review')
# st.write('')
st.write('Temporal convolutional autoencoder for unsupervised anomaly detection in time series')
st.write('Development and Online Validation of an Intrinsic Fault Detector for a Powered Robotic Knee Prosthesis')
st.write('A Deep Learning Framework for End-to-End  Control of Powered Prostheses')

st.write('✅Dataset Description')
st.write('Data from 28 sensor channels')
st.write('Torque data (Knee and Ankle)')

st.write('✅Dataset Link (if applicable)')
st.write('Internal to EPIC Lab')

st.write('2. Problem Definition: Identify a problem and motivate the need for a solution.')
st.write('✅Problem')
st.write('Anomalies in prosthesis torque data can lessen accuracy of deep-learning models training on this information.')
st.write('Goal: Identify anomalies in powered prosthesis data using an autoencoder.')

st.write('✅Motivation')
st.write('Anomalies in prosthesis torque data can lessen accuracy of deep-learning models training on this information. The goal is to create a model using an autoencoder to identify these anomalies, which can then be filtered out of the original data set. Eliminating this bad data will improve the accuracy of the original deep-learning model.') 


st.write('3. Methods: Present proposed solutions including specific data processing methods and machine learning algorithms, and elaborate on why you think each will be effective. It is recommended to identify specific functions/classes in existing packages and libraries (i.e. scikit-learn) rather than coding the algorithms from scratch.')
st.write('✅3+ Data Preprocessing Methods Identified')
st.write('Cropping stance and swing phases')
st.write('Sensors from the 28 channels may not be in the exact same time frame/collection frequency so may need to interpolate the sensor data')
st.write('Adjusting sensor orientation for left/right foot individuals & post-hardware upgrades')


st.write('✅3+ ML Algorithms/Models Identified') 
st.write('Autoencoder (find anomalies) -> TCN')
st.write('TCN (not filtered by autoencoder)')
st.write('Autoencoder (find anomalies) -> CNN')
st.write('CNN (not filtered by autoencoder) ')
st.write('✅CS 7641: Unsupervised and Supervised Learning Methods Identified')
st.write('Unsupervised - Autoencoder  -  input torque get torque or 28 sensor input to get 28 sensor channels')
st.write('Supervised - TCN Deep-learning model - predict knee and ankle torque  - input sensor data get torque')


st.write('Autoencoder')
st.write('- has layers that get smaller and smaller')
st.write('- latent space can store all the data into a small abstract space, like a zip file compressing')
st.write('- then this compressed data is passed through bigger and bigger stuff which reconstructs the time sample based on the most compressed version of the data')
st.write('- model predicts more common pattern based on the compressed feature')
st.write('- then can use this re-expanded data to do anomaly detection')
st.write('- based on anomaly detection will retrain deep learning model to see if performance goes up')
st.write('- model filter out bad data so another model can train better')
st.write('- this structure of big to small to big layers')
st.write('- autoencoder unsupervised')

st.write('4. (Potential) Results and Discussion: Identify several quantitative metrics you plan to use for the project (i.e. ML Metrics). Present goals in terms of these metrics, and state any expected results.')
st.write('✅3+ Quantitative Metrics')
st.write('- RMSE')
st.write('- R2')
st.write('- Dynamic Time Warping')
st.write('- Inference Time')
st.write('✅Project Goals (recommended to include sustainability and ethical considerations)')
st.write('Identify anomalies in powered prosthesis data using an autoencoder.')
st.write('Improve accuracy of TCN Deep-Learning Model in predicting torque')
st.write('Improve overall gait in transfemoral amputees wearing powered prosthesis')
st.write('✅Expected Results')
st.write('TCN with Autoencoder will perform the best, due to feeding in better filtered data')
st.write('Baseline TCN model will successfully assess the effectiveness of the anomaly filter using Autoencoder')
st.write('CNN + Autoencoder will have a slower inference time and worse performance than baseline TCN model')
st.write('5. References: Cite relevant papers and articles utilizing the IEEE format. All references in this section must have a matching in-text citation in the body of your proposal text.')
st.write('✅3+ References (preferably peer reviewed)')
st.write('✅1+ In-Text Citation Per Reference')
st.write('Seamless and intuitive control of a powered prosthetic leg using deep neural network for transfemoral amputees')
st.write('Read auto encoder part')
st.write('Other Helpful Resources:')
st.write('https://www.jeremyjordan.me/autoencoders/')
st.write('Temporal convolutional autoencoder for unsupervised anomaly detection in time series')
st.write('Development and Online Validation of an Intrinsic Fault Detector for a Powered Robotic Knee Prosthesis')
st.write('A Deep Learning Framework for End-to-End  Control of Powered Prostheses')




