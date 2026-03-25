import streamlit as st
import pickle
import pandas as pd

with open("Loan_Model.pkl","rb") as pickle_in:
    model=pickle.load(pickle_in)

st.title("Credit Wise Loan Recommendation System")
st.header("Enter your details to get a loan recommendation")
st.text("This app uses a machine learning model to predict whether you are eligible for a loan based on your financial and personal information.")


st.subheader("DTI Ratio")
dti_ratio=st.number_input("Enter the DTI ratio of your income")

st.subheader("Credit Score")
credit_score=st.number_input("Enter your credit score")

st.subheader("Applicant Income")
applicant_income=st.number_input("Enter your income")

st.subheader("Loan Amount")
loan_amount=st.number_input("Enter the loan amount you want")

st.subheader("Co-Applicant Income")
coapplicant_income=st.number_input("Enter the co-applicant's income")

st.subheader("Collateral Value")
collateral_value=st.number_input("Enter the collateral value")

st.subheader("Savings")
savings=st.number_input("Enter your savings amount")

st.subheader("Age")
age=st.number_input("Enter your age")   

st.subheader("Loan Term")
loan_term=st.number_input("Enter the loan term in months")

st.subheader("Existing Loans")
existing_loans=st.number_input("Enter the number of existing loans you have")

st.subheader("Dependents")
dependents=st.number_input("Enter the number of dependents you have")

st.subheader("Employment status")
employment_status=st.selectbox("Select your employment status", ["salaried", "Self-employed"])
if employment_status == "salaried":
    employment_status = 1
else:   
    employment_status = 0
    
st.subheader("Gender")
gender=st.selectbox("Select your gender", ["Male", "Female"])
if gender == "Male":
    gender = 1
else:
    gender = 0
    
st.subheader("Employer Category MNC")
employer_category_mnc=st.selectbox("Select your employer category", ["Yes", "No"])
if employer_category_mnc == "Yes":
    employer_category_mnc = 1
else:
    employer_category_mnc = 0
    
st.subheader("Marital Status")
marital_status=st.selectbox("Select your marital status", ["Married", "Single"])
if marital_status == "Single":
    marital_status = 1  
else:
    marital_status = 0

if st.button("Predict Loan Eligibility"):
    input_data = pd.DataFrame({
        "dti_ratio": [dti_ratio],
        "credit_score": [credit_score],
        "applicant_income": [applicant_income],
        "loan_amount": [loan_amount],
        "coapplicant_income": [coapplicant_income],
        "collateral_value": [collateral_value],
        "savings": [savings],
        "age": [age],
        "loan_term": [loan_term],
        "existing_loans": [existing_loans],
        "dependents": [dependents],
        "employment_status": [employment_status],
        "gender": [gender],
        "employer_category_mnc": [employer_category_mnc],
        "marital_status": [marital_status]
    })

    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.success("Congratulations! You are eligible for the loan.")   
    else:
        st.error("Sorry, you are not eligible for the loan at this time.")  
                  
