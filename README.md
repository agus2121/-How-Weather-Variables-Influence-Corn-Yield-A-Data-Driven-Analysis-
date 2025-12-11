# How Weather Variables Influence Corn Yield: A Data-Driven Analysis

## 📘 Overview

This project analyzes how corn yield changes from year to year and how
it is influenced by key weather variables such as temperature, humidity,
and rainfall. The analysis includes exploratory data analysis (EDA),
correlation studies, and an OLS regression model to identify which
factors most strongly affect productivity.

## 📊 Dataset Description

The dataset contains multi-year corn production and weather data.

### Main columns:

-   kota --- City
-   tahun --- Year
-   tanam --- Planting month (APR, MAY, JUN, JUL)
-   panen --- Harvest month
-   temperature
-   kelembaban (humidity)
-   curah_hujan (rainfall)
-   Yield(Kg/Ha) --- Corn yield in Kg/Ha

Additional encoded variables: - tanam_angka - panen_angka

## 🛠️ Tools & Libraries

-   Python
-   pandas
-   matplotlib
-   seaborn
-   statsmodels
-   scikit-learn
-   Jupyter Notebook

## 🔍 Analysis Workflow

### 1. Yearly Yield Trend

-   Calculated average corn yield per year
-   Visualized using bar chart
-   Identified highest and lowest yield years

### 2. Yield by Planting Month

-   Stacked bar chart comparing yield per planting month per year

### 3. Yield by Planting & Harvest Month

-   Mean yield for each planting and harvest month

### 4. Yield by City

-   Average yield per kota
-   Identified most productive regions

### 5. Correlation Analysis

-   Heatmap showing relationships among:
    -   temperature
    -   kelembaban
    -   curah_hujan
    -   yield

### 6. Regression Analysis (OLS Model)

-   Encoded months numerically
-   Built OLS model with:
    -   tanam_angka
    -   tahun
    -   temperature
    -   kelembaban
    -   curah_hujan
-   Evaluated statistical significance

## 📈 Visualizations Included

-   Bar chart of yearly yield
-   Stacked bar chart by planting month
-   Yield per planting and harvest month
-   Yield per city
-   Correlation heatmap

## 🧠 Key Findings (Fill based on your results)

-   Rainfall strongly influences yield
-   High humidity reduces productivity
-   Temperature shows moderate seasonal impact
-   Planting month significantly impacts yield distribution


## 🚀 Future Improvements

-   Incorporate wind-speed variable
-   Build predictive machine learning model
-   Analyze vegetative vs generative phase weather impact
-   Develop dashboard (Streamlit/Power BI)

