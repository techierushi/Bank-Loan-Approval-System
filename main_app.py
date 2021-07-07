import numpy as np
import pickle
import streamlit as st
from keras.models import load_model
from sklearn.preprocessing import StandardScaler

model = load_model('Bank_Loan_model.h5')

scaler = pickle.load(open('scaler.pkl','rb'))

def prediction(Age,Experience,Income,Family,CC_avg,Education,Mortage,Securities,CD_account,Online,CC):
    x = scaler.transform(np.array([[Age,Experience,Income,Family,CC_avg,Education,Mortage,Securities,CD_account,Online,CC]]))
    new_pred = model.predict(x)
    new_pred = (new_pred > 0.8)

    if new_pred == True:
        res = "Potential Customer for Personal Loan"
    else:
        res = "Customer might not be interested in Personal Loan"

    return res

def main():
    html_temp = """
    <div style ="background-color:#acf07f;padding:13px">
    <h1 style ="color:black;text-align:center;font-family: Garamond, serif;font-size:43px;"> Bank Personal Loan <br> Recommender System </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    st.markdown("""
    <h3><center> Check whether a potential customer (Depositor) <br> will buy the personal loan or not </center></h3>
    """
    ,unsafe_allow_html = True)


    st.sidebar.subheader("About App")

    st.sidebar.info("This web app is my hands-on project on Deep Learning ")
    st.sidebar.info("It will help to predict the likelihood of a customer buying personal loan ")
    st.sidebar.info("This will help Bank to issue personal loan to depositors therefore growing their annual revenue")
    st.sidebar.info("Hence, this model is developed to target customers/depositors who have high probability of obtaining personal loan ")
    st.sidebar.info("Enter the details mentioned ")
    st.sidebar.info("Click on the 'Predict' button to get the result whether the customer buy personal loan ")
    st.sidebar.info('Developed By ~ TechieRushi (Rushikesh Shinde)')

    st.sidebar.subheader("My GitHub Profile")
    link = '[Github: @techierushi](https://github.com/techierushi)'
    st.sidebar.markdown(link, unsafe_allow_html=True)

    Age = st.number_input("Enter the Age of Customer :")
    Income = st.number_input("Enter the annual income of the customer : (Enter value without 0s eg- for 134000 Enter 134) ")
    value = range(1,4)
    Education = st.select_slider("Education Level : (Select-> 1 - Undergrad, 2 - Graduate, 3 - Advanced/Professional)", options=value)
    Family = st.slider("No.of.Family Members of Customer:",1,10)
    CC_avg = st.number_input("Enter the customers average spending on credit cards/month : (Enter value without 0s eg- for 134000 Enter 134)")
    Experience = st.number_input("No.of.Years of Professional Experience")
    Mortage = st.number_input("Value of House Mortage : (Enter value without 0s eg- for 134000/134k Enter 134)")
    Securities = st.radio("Does the customer have Securities account with the bank : (Yes:1, No:0)", [1, 0])
    CD_account = st.radio("Does the customer have Certificate of deposit (CD) account with the bank : (Yes:1, No:0)", [1, 0])
    Online = st.radio("Does the customer uses bank's online facilities : (Yes:1, No:0)", [1,0])
    CC = st.radio("Does the customer use the Credit Card issued by the bank : (Yes:1, No:0)", [1,0])


    if st.button("Predict"):
        result = prediction(Age,Experience,Income,Family,CC_avg,Education,Mortage,Securities,CD_account,Online,CC)
        st.success(result)

if __name__=='__main__':
    main()
