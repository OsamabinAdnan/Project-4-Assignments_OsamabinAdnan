# Data Dashboard & Visualization with Streamlit

A simple and effective data dashboard built with Streamlit that allows users to upload CSV files, explore data, and create visualizations.

## Features

- **CSV File Upload**: Easily upload and process CSV data files
- **Data Preview**: View the first few rows of your dataset
- **Data Summary**: Get statistical summaries of your data
- **Data Filtering**: Filter data based on selected columns and values
- **Data Visualization**: Create line charts from your filtered data

## How to Run

```bash
streamlit run main.py
```

## Usage

1. **Upload a CSV file** using the file uploader
2. **Explore your data** using the data preview and summary sections
3. **Filter your data** by selecting a column and value
4. **Visualize your data** by selecting columns for the x and y axes and clicking "Generate Plot"

## Requirements

- Python 3.6+
- Streamlit
- Pandas

## Installation

```bash
pip install streamlit pandas matplotlib
```

## Customization

You can customize the appearance of the dashboard by modifying the Streamlit theme settings in the `main.py` file:

```python
st.set_page_config(
    page_title='Data Dashboard & Visualization',
    page_icon='📊',
    layout='centered'
)
```

### Live Demo
[Data Visualization Dashboard](https://datavisualizationdashboard-osamabinadnan.streamlit.app/)

## License

This project is open source and available under the MIT License.
