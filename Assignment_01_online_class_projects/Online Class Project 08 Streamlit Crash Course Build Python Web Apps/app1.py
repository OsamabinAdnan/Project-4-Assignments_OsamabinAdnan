# Displaying Data & Styling DataFrame using Streamlit and Pandas

import streamlit as st
import pandas as pd

st.title("Data Frame Creation using Pandas")
st.write("This is a simple Streamlit app to create and display a DataFrame using Pandas.")

data = {
    'Name': ['John', 'Jane', 'Bob', 'Alice'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo'],
    'Score': [95, 85, 91, 88],
    'Passed': [True, False, True, True],
}

# Data Frame creation
df = pd.DataFrame(data)

# Display the DataFrame
st.subheader("DataFrame:")
st.dataframe(df) # Scrollable DataFrame

# Display the DataFrame as a table
st.subheader("DataFrame as Table:")
st.table(df) # Non-scrollable table

st.divider()
# Selectbox widget with data frame @@@@@@@@@@@@@@ filtering @@@@@@@@@@@@@@@
st.subheader("Filtered DataFrame:")
city = st.selectbox("Select a city:", df['City'].unique())
filtered_df = df[df['City'] == city]

st.write(f"Data for {city}:")
st.dataframe(filtered_df)

st.divider()
# Style DataFrame @@@@@@@@@@@@@@@ style @@@@@@@@@@@@@@@
st.subheader("Styled DataFrame:")
styled_df = df.style.applymap(lambda x: 'background-color:yellow' if isinstance (x, int) and x > 90 else '')
st.dataframe(styled_df)

st.divider()

# Get an user input as number input and filter based on that number defaultly its going to be 80 
st.subheader("Filtered DataFrame based on user_input:")

value_of_style = st.number_input("Enter a minimum number to display in yellow:", value=80)
styled_df = df.style.applymap(lambda x: 'background-color:yellow' if isinstance (x, int) and x > value_of_style else '')
st.dataframe(styled_df)

st.divider()

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ JSON Data @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

st.subheader("JSON Data:")
json_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science", "History"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip": "10001"
    }
}

# Display JSON data
st.json(json_data)