# ads-508-team-project

**ADS508: Cloud Computing**

This GitHub repository is for group 7 completed April 14, 2025.

### Members:
Austin Mallie, Cynthia Portales-Loebell, and Sasha Libolt

---

## Company Details:

**Company Name**: LoanGuard Insights  
**Industry**: Real Estate and Finance  
**Company Size**: Mid-size

## Abstract:
LoanGuard Insights is a for-profit consulting company in the real estate sector seeking to advise mortgage lenders on potential loan defaults by analyzing arrest data, crimes reported and foreclosure data in Los Angeles to highlight the correlations between foreclosures and crime in order to predict foreclosure hotspots and patterns. By leveraging advanced data science techniques such as machine learning algorithms and statistical analysis, this study aims to uncover the negative effects that crime has on property foreclosure rates. 

## Problem Statement:
LoanGuard Insights aims to help mortgage lenders predict potential loan defaults by identifying areas at high risk for foreclosure. The company seeks to address the challenge of understanding the correlation between crime rates, arrests, and foreclosure patterns in Los Angeles. By leveraging publicly available data, the goal is to develop a predictive model that can identify crime-prone areas with higher foreclosure risk, providing lenders with actionable insights to mitigate financial risks.

## Goals:
- Identify high-risk areas in Los Angeles for foreclosures, and offer actionable insight on lending strategies in areas found to be high-risk
- Develop a predictive model to predict future home foreclosures by analyzing crime and arrest data in the area
- Provide insight to adjust future lending strategies in order to mitigate losses

## Non-Goals:
- This project will not focus on specific individuals or properties that are at risk, instead focus on areas
- It will not focus on analyzing the crime data or advocating strategies on policing for the city of Los Angeles
- It will not forecast the economic state or fluctuations of the housing market

## Data Sources:
The data for this project will be stored in an AWS S3 Bucket, named `ads508-group7`, which will interact with AWS SageMaker for model development. The following four datasets will be uploaded to the S3 bucket:

1. **Arrest Data from 2020 to Present:**
csv file with 25 columns and 338,332 rows
https://catalog.data.gov/dataset/arrest-data-from-2020-to-present/
3. **Crime Data 2020 to Present:**
csv file with 28 Columns and 1,005,104 rows
https://catalog.data.gov/dataset/crime-data-from-2020-to-present
5. **2024 Registered Foreclosures:**
csv file with 18 Columns and 2,009 rows
https://catalog.data.gov/dataset/2024-registered-foreclosure-properties
7. **2023 Registered Foreclosures:**
csv file with 18 Columns and 2,080 rows
https://catalog.data.gov/dataset/2023-registered-foreclosure-properties

