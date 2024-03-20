import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Welcome to Explaration Data Analysis')

#menampilkan eda 
    st.title('Sleep Disorder Distribution')
    image = Image.open('1.png')
    st.image(image, caption='figure 1')
#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('''Berdasarkan bar plot di atas, dapat diketahui bahwa lebih banyak orang yang tidak mengalami gangguan tidur(normal),
                      perbandingan orang yang mengalami sleep apnea maupun insomnia tidak sangat tipis.
                   ''')

#menampilkan eda 
    st.title('BMI Category Distribution')
    image = Image.open('2.png')
    st.image(image, caption='figure 2')
    image = Image.open('3.png')
    st.image(image, caption='figure 3')
#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('''
                    Berdasarkan plot di atas:
                    - lebih banyak pasien yang memiliki berat badan normal
                    - namun tidak sedikit pula pasien yang memiliki masalah berat badan overweight
                    - kebanyakan pasien yang memiliki berat badan overweight yaitu wanita
                    - sedangkan pasien yang memiliki berat badan normal di dominasi oleh pria
                   ''')

#menampilkan eda 
    st.title('Daily Step by Occupation')
    image = Image.open('4.png')
    st.image(image, caption='figure 4')
#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('''Berdasarkan bar diatas dapat kita lihat bahwa pekerja yang miliki jumlah langkah harian paling banyak ialah seorang perawat,
                   namun yang memiliki jumlah langkah harian paling sedikit ialah sales representative''')
