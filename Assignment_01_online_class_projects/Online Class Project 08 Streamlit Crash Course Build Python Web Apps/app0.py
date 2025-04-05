# Different Text Formats

# Import the streamlit library for creating web applications
import streamlit as st

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ Different Text Formats @@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Create the main title for the web application
st.title("Streamlit Fundamentals")

# Display a header - larger than subheader but smaller than title
st.header("This is a header")

# Display a subheader - smaller than header
st.subheader("This is a subheader")

# Display plain text without any formatting
st.text("This is a simple text output")

# Use markdown formatting for styled text
st.markdown("**This is bold text using markdown**")  # Bold text
st.markdown("_This is italic text using markdown_")  # Italic text

# Add a visual separator
st.divider() # Horizontal line for separation

# Define variables for demonstration
name = "Osama"
number = 10

# Display formatted text using f-strings
st.write(f"Hello, {name}!")
st.write(f"Random Number: {number}")

st.divider() # Horizontal line for separation

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ Different Widgets @@@@@@@@@@@@@@@@@@@@@@@@@@

# Create an interactive button
if st.button("Click Me!"):  # Returns True when clicked
    st.write("Button Clicked!")

# Create a checkbox widget
checked = st.checkbox("Check Me!")  # Returns True when checked
if checked:
    st.write("Checkbox is Checked!")

# Create a slider widget for age selection
# Parameters: label, min value, max value, default value, step
age = st.slider("Select your age" , 0, 100, 18, 1)
st.write(f"Your age is {age}")

# Create a text input field
name = st.text_input("Enter your name", value= "")  # Empty default value
if name:
    st.write(f"Hello, {name}!")

st.divider()

# Example of multiple widgets working together
your_name =st.text_input("Enter your name:")
your_age = st.slider("Select your age", 0, 100, 18, 1, key="age_slider")  # Unique key for multiple sliders

# Submit button to process the form data
if st.button("Submit"):
    st.write(f"Hello, {your_name}! You are {your_age} years old.")

st.divider()

# Create a number input widget
# Parameters: label, minimum value, maximum value, default value, step size
my_age = st.number_input("Enter your age", min_value=0, max_value=100, value=18, step=1)
st.write(f"Your age is {my_age}")