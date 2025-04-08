import streamlit as st
import pandas as pd

st.set_page_config(
    page_title= 'Data Dashboard & Visualization',
    page_icon= '📊',
    layout= 'centered'
)

st.title("Data Dashboard & Visualization 🛢️")

uploaded_file = st.file_uploader('Upload a CSV file:', type= 'csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader('Data Preview')
    st.write(df.head())

    st.subheader('Data Summary')
    st.write(df.describe())

    st.subheader('Filter Data')
    columns = df.columns.tolist()
    selected_columns = st.selectbox('Select columns to filter by:', columns)
    unique_values = df[selected_columns].unique()
    selected_value = st.selectbox('Select a value to filter by:', unique_values)

    filtered_df = df[df[selected_columns] == selected_value]
    st.write(filtered_df)

    st.subheader('Plot Data')
    x_column =  st.selectbox('Select a column for the x-axis:', columns)
    y_column =  st.selectbox('Select a column for the y-axis:', columns)

    if st.button('Generate Plot'):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.info('Please upload a CSV file to get started.')