# Sensex Prediction README

This project focuses on analyzing data collected from various sources, and then building a deep learning prediction model for the Sensex points which would give better performance than simple machine learning models. The analysis includes data profiling, single variate and bivariate analysis, correlation analysis and modeling using Python.

## Data Collection

The historical data of BSE Sensex points was collected from trusted online sources and includes data from the year 1990 to year 2023. The dataset encompasses metrics like GDP, Inflation, Leap year, Election year, Dowjones value, Sensex points, Rate of interest, Rate of inflation, Price of gold, Price of Oil and USD to INR conversion rate with respect to time.

## Data Profiling

Before conducting the analysis, the data was profiled to gain insights into its structure, quality, and characteristics. Summarization techniques were applied to understand the distribution of variables, identify missing values, outliers, and potential data issues.

## Data Analysis

The analysis involved both single variate and bivariate analysis to explore relationships between different variables in the dataset. This helped uncover patterns, trends, and correlations that provide valuable insights into BSE Sensex Points behavior with respect to different variables.

## Data Visualization

The data after analysis is visually represented in forms of graph using bar-charts, histogram and line-charts to represents and visualize various changes in data for a better understanding of the dataset.

## Deep Learning Model Building

Using Python library TensorFlow, specifically Keras for easier use, setup a time-series-generator. The layers of this deep learning model are based on dense LSTM.

### Deep Learning Model Tuning

The deep learning model is tunned for finer and better results through tuning its hyper-parameters and number of epochs. The ideal values for both are decided through trial and error and a deep understanding of the working of these models in context of the project.

## Prediction

After fine tuning and training the model it is used on test dataset to predict next months Sensex Points. The predictions and other results of testing are visually represented using line-charts to better encompass the time series nature of the project.

## Usage

To replicate the analysis and prediction:

1. Download the Uber dataset from the government's open data portal.
2. Run the provided scripts for data profiling, analysis, and multidimensional data modeling.
3. Run the provided scripts for model building, tunning and training.
4. Run the provided scripts for prediction.
