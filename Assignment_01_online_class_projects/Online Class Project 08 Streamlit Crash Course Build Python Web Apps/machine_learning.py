import streamlit as st
import joblib

model = joblib.load('linear_regression_model.pkl')

st.title('Linear Regression Prediction App')
st.write('Enter the feature values for prediction:')

feature_value = st.number_input('Enter a value for Feature:', min_value=0.0, max_value=100.0, value=50.0)

if st.button('Predict'):
    prediction = model.predict([[feature_value]])[0][0]
    st.write(f'Predicted Target value for Feature {feature_value} = {prediction:.2f}')
