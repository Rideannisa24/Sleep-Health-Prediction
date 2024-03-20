import streamlit as st
import eda
import model
from PIL import Image




page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.title("Milestone 2")
    st.write('Name      : Rizqia Dewi Annisa')
    st.write('Batch     : HCK-010')
    st.write('Objective   : Develop a predictive analytics tool to analyze sleep disorder. The goal is to identify people who has sleep disorder(sleep apnea or insomnia) or Normal.')
    st.caption('Select another menu from the left-side Select Box on your screen to get started!')
    st.write('')
    st.write('')
    st.title("Sleep Disorder Prediction")

    st.subheader('What is Sleep Disorder ?')
    img1 = Image.open('sleep.jpg')
    img2 = Image.open('Symptoms-Of-Sleep-Disorders.jpg')
    img3 = Image.open('Causes-Of-Sleep-Disorders.jpg')
    img4 = Image.open('Treatment-Of-Sleep-Disorders.jpg')
    st.image(img1, width=400, use_column_width=True)
    st.image(img2, width=400, use_column_width=True)
    st.image(img3, width=400, use_column_width=True)
    st.image(img4, width=400, use_column_width=True)

    with st.expander("Background"):
        st.caption('''
                    Sleep plays a vital role in maintaining overall health and well-being. 
                    Nevertheless, various lifestyle factors can significantly impact the quality and duration of sleep. 
                    Understanding the relationship between lifestyle choices and sleep health is essential for individuals seeking to improve their sleep patterns.
                     ''')

    with st.expander("Problem Statement"):
            st.caption('''
                        Solving the problem : With the development we are witnessing from artificial intelligence, machine learning models can be used and then trained on a set of training data, 
                       then tested on a set of test data, and the classifier predicts whether a person has sleep disorder or not based on the data to be entered.
                       ''')

    with st.expander("Conclusion"):
        st.caption('''
                    0 = Normal,
                    1 = Sleep Apnes
                    2 = Insomnia
                    ''')
        
elif page == 'Exploration Data Analysis':
    eda.run()
else:
    model.run()