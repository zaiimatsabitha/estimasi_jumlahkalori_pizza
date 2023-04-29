import pickle
import streamlit as st

model = pickle.load(open('Pizza.sav', 'rb'))

st.title('Estimasi jumlah kalori pada menu pizza')

prot = st.number_input('input protein')
carb = st.number_input('Input karbohidrat')
sodium = st.number_input('Input sodium')
fat = st.number_input('Input lemak')


predict = ''

if st.button('Estimasi kalori'):
    predict = model.predict(
        [[prot,carb,sodium,fat]]
    )
    st.write ('Estimasi jumlah kalori pada menu pizza : ', predict)