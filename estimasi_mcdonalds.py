import pickle
import streamlit as st

model = pickle.load(open('estimasi_mcdonalds.sav', 'rb'))

st.title('Estimasi Jumlah Energi Di Menu McDonalds')

Total_fat = st.number_input('Input Jumlah Lemak (g)')
Protein = st.number_input('Input Total Protein (mg)')
Total_carbohydrate = st.number_input('Input Total Karbohidrat (g)')
Total_Sugars = st.number_input('Input Jumlah Gula (g)')
Cholesterols = st.number_input('Input Jumlah Kolesterol (g)')

predict = ''

if st.button('Estimasi Kalori'):
    predict = model.predict(
        [[Protein, Total_fat, Total_carbohydrate, Total_Sugars, Cholesterols]]
        )
    st.write ('Estimasi Jumlah Kalori di setiap size menu McDonalds : ', predict)