# Data Visualization topics

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['A', 'B', 'C']
)

# Creating line chart
st.subheader('Line Chart')
st.line_chart(data)

st.divider()

# Bar chart
st.subheader('Bar Chart')
st.bar_chart(data)

st.divider()

# Area chart
st.subheader('Area Chart')
st.area_chart(data)

plotly_data = pd.DataFrame({
    'fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes'],
    'amount': [40, 10, 20, 50]
})

st.divider()
# @@@@@@@@@@@@@@@@@@@@@@@@@ Plotly Chart @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# plotly bar chart
st.subheader('Plotly Bar Chart')
fig = px.bar(plotly_data, x='fruit', y='amount', title='Fruit Sales')

st.plotly_chart(fig)

st.divider()
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Matplotlib Chart and seaborn @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

data = pd.DataFrame(
    np.random.randn(100, 3),
    columns= ['A', 'B', 'C']
)

plt.figure(figsize=(10, 6))
sns.scatterplot(x= data['A'], y= data['B'])
plt.title('Scatter Plot of A and B')

st.pyplot(plt)
