import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import MinMaxScaler,StandardScaler, RobustScaler, LabelEncoder, OneHotEncoder
from PIL import Image

def run():
# Load All Files

    with open('final_model.pkl', 'rb') as file:
        final_model = final_model = pickle.load(file)


        Gender= st.selectbox("Gender", ["Male", "Female"])
        Occupation = st.selectbox("Occupation", ["Software Engineer", "Doctor", "Sales Representative", "Teacher", "Nurse", 
                                                 "Engineer", "Accountant", "Scientist", "Lawyer", "Salesperson", "Manager"])
        Sleep_Duration = st.selectbox("Sleep_Duration", [6.1, 6.2, 5.9, 6.3, 7.8, 6. , 6.5, 7.6, 7.7, 7.9, 6.4, 7.5, 7.2, 5.8,
                                                         6.7, 7.3, 7.4, 7.1, 6.6, 6.9, 8. , 6.8, 8.1, 8.3, 8.5, 8.4, 8.2])
        Physical_Activity_Level = st.selectbox("Physical_Activity_Level", [42, 60, 30, 40, 75, 35, 45, 50, 32, 70, 
                                                                           80, 55, 90, 47, 65, 85])
        Stress_Level = st.selectbox("Stress_Level", [6, 8, 7, 4, 3, 5])
        BMI_Category = st.selectbox("BMI_Category", ["Overweight", "Normal", "Obese", "Normal Weight"])
        Heart_Rate = st.selectbox("Heart_Rate", [77, 75, 85, 82, 70, 80, 78, 69, 72, 68, 76, 81, 65, 84, 74, 67, 73, 83, 86])
        
    
    st.write('In the following is the result of the data you have input : ')
    
    data_inf = pd.DataFrame({
            "Gender" : Gender,
            "Occupation" : Occupation,
            "Sleep Duration" : Sleep_Duration,
            "Physical Activity Level" : Physical_Activity_Level,
            "Stress Level" : Stress_Level,
            "BMI Category" : BMI_Category,
            "Heart Rate" : Heart_Rate,
        }, index=[0])

    st.table(data_inf)


    if st.button(label='predict'):
    
        # for input in data_inf.columns:
        #     if data_inf[input].dtype == 'object':
        #         data_inf[input].apply(LabelEncoder().fit_transform())
        #         data_inf[input] = final_model.predict(data_inf)
        #     if data_inf[input].dtype == 'int':
        #         data_inf[input].apply(StandardScaler().transform())
        #         data_inf[input] = final_model.predict(data_inf)

        y_pred_inf = final_model.predict(data_inf)

        st.write("Here is a prediction of the People Who Have Sleep Disorder: ")
        if y_pred_inf[0] == 1:
            st.subheader("The Diagnosis is:")
            prediction = 'Sleep Apnea'
            
        if y_pred_inf[0] == 2:
            st.subheader("This People Diagnosed Insomnia")
            prediction = 'Insomnia'
            
        else:
            st.subheader("This People Normal")
            prediction = 'Normal'
            
        st.subheader('Based on user input, the model predicted: ')
        st.header(y_pred_inf)