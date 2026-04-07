import streamlit as st
import joblib
st.title('HR ATTRITION')
Age=st.number_input("enter your age:")
DistanceFromHome=st.number_input("enter your distance from home:")
EnvironmentSatisfaction=st.number_input("enter your enviornment satisfaction:")
JobLevel=st.number_input("enter your job level:")
JobRole=st.selectbox("select job role",['Sales Executive','Research Scientist','Laboratory Technician',
       'Manufacturing Director','Healthcare Representative','Manager',
       'Sales Representative','Research Director','Human Resources'])
JobSatisfaction=st.number_input("enter your job satisfaction:")
MonthlyIncome=st.number_input("enter your monthly income:")
OverTime=st.selectbox("select overtime",['Yes', 'No'])
WorkLifeBalance=st.number_input("enter your worklife balance:")
YearsAtCompany=st.number_input("enter your years at company:")
YearsInCurrentRole=st.number_input("enter your years in current role:")
YearsSinceLastPromotion=st.number_input("enter your Years Since LastPromotion:")
YearsWithCurrManager=st.number_input("enter your Years With CurrManager:")

classi=joblib.load(r'C:\Users\Swathi\project.1\hr project.pkl')
label1=joblib.load(r'C:\Users\Swathi\project.1\lb1.pkl')
label2=joblib.load(r'C:\Users\Swathi\project.1\lb2.pkl')
label3=joblib.load(r'C:\Users\Swathi\project.1\lb3.pkl')
stand=joblib.load(r'C:\Users\Swathi\project.1\sd.pkl')


JobRole=label2.transform([JobRole])[0]
OverTime=label3.transform([OverTime])[0]

if st.button("Predict"):
    result=classi.predict(stand.transform([[Age,DistanceFromHome,EnvironmentSatisfaction,JobLevel,JobRole,JobSatisfaction,MonthlyIncome,OverTime,
                                        WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager]]))[0]
    if result==1:
        st.success('employee left the company'.format(result))
    else:
      st.success('employee stayed in the company'.format(result))
    
    