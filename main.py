import streamlit as st
import requests

def loan_prediction(data):
    url = 'http://localhost:5000/predict'
    r = requests.post(url, json=data)
    return r.json()['prediction']

def main():
    st.set_page_config(page_title="Loan Status Prediction", page_icon=":money_with_wings:")
    st.title("Loan Status Prediction")

    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Not Graduate", "Graduate"])
    self_employed = st.selectbox("Self Employed", ["No", "Yes"])
    applicant_income = st.number_input("Applicant Income", min_value=1)
    coapplicant_income = st.number_input("Co-applicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=1)
    loan_amount_term = st.number_input("Loan Amount Term", min_value=1)
    credit_history = st.number_input("Credit History", min_value=0, max_value=1)
    property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

    if st.button("Predict"):
        data = {
            "Gender": 1 if gender == "Male" else 0,
            "Married": 1 if married == "Yes" else 0,
            "Dependents": int(dependents[0]),
            "Education": 1 if education == "Not Graduate" else 0,
            "Self_Employed": 1 if self_employed == "Yes" else 0,
            "ApplicantIncome": applicant_income,
            "CoapplicantIncome": coapplicant_income,
            "LoanAmount": loan_amount,
            "Loan_Amount_Term": loan_amount_term,
            "Credit_History": credit_history,
            "Property_Area": ["Rural", "Semiurban", "Urban"].index(property_area)
        }
        prediction = loan_prediction(data)
        if prediction == 1:
            st.error("Loan application is likely to be approved.")
        else:
            st.success("Loan application is likely to be rejected.")

if __name__ == "__main__":
    main()
