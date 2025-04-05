# Layout and Theme options (topics)

import streamlit as st

###################### Theme options
st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":tada:",
    layout="centered",
    initial_sidebar_state='expanded'
)

st.title("My Streamlit Title")
st.write("This is a simple Streamlit app")

st.divider()

######################## Create columns in  streamlit app
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("This is column 1")
    st.button("Button 1")

with col2:
    st.header("Column 2")
    st.write("This is column 2")
    st.button("Button 2")

st.divider()
##################### Expander widget
with st.expander("See more details"):
    st.write('Here are some additional details')
    st.line_chart([1, 2, 3, 4, 5, 6])

st.divider()
###################### Sidebar widget
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose a page", ['Home', 'About', 'Contact'])

if option == 'Home':
    st.write("Welcome to the Home page")
elif option == 'About':
    st.write("This is the About page")
    # you can put your portfolio project with link under this elif statement
elif option == 'Contact':
    st.write("Contact us at contact@example.com")

st.divider()
