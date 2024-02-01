Introduction
============

Machine Learning Models for Salinity Prediction
----------------------------------------------

In this study, we have developed two machine learning models for predicting salinity levels in the Karnaphuli River. These models utilize advanced algorithms to analyze water quality parameters and other relevant features, providing valuable insights into the salinity trends.

Dependencies
------------

The implementation of our machine learning models relies on several key Python libraries, including:

- pandas
- numpy
- matplotlib
- seaborn


These libraries contribute to data manipulation, numerical operations, and visualization, enhancing the efficiency and effectiveness of our analysis.

Dataset
-------

The dataset used in this study is sourced from the Department of Environment, Bangladesh. It comprises monthly data for various water quality parameters in the Karnaphuli River, including pH, Total Dissolved Solids (TDS), Electrical Conductivity (EC), Chloride (Cl), Dissolved Oxygen (DO), Total Solids (TS), Suspended Solids (SS), Temperature, and salinity. This comprehensive dataset allows us to conduct a detailed analysis of the factors influencing salinity levels in the river.

Models
------

Two distinct machine learning models were constructed as part of this study:

1. **Parameter-based Model:**
   - Features: Water quality parameters (pH, TDS, EC, Cl, DO, TS, SS, Temp)
   - Objective: Predicting salinity based on water quality metrics.

2. **Context-based Model:**
   - Features: Source location, month, year
   - Objective: Predicting salinity with additional context, considering source location and temporal factors.

These models aim to provide accurate and reliable predictions, contributing to a deeper understanding of salinity variations in the Karnaphuli River.
