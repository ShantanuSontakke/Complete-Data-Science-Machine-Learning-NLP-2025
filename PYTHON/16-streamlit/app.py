import streamlit as st
import pandas as pd
import numpy as np

## Title of the aplication
st.title("Simple Streamlit App")

## Display a Simple Text
st.write("Welcome to this simple Streamlit application!")

##create a simple Dataframe

df = pd.DataFrame({
    'Column 1': [1,2,3,4,5,6,7,8,9],
    'Column 2': [10,20,30,40,50,60,70,80,90]
})


# Display the DataFrame
st.write("Here is a simple DataFrame:")
st.dataframe(df)

#create a line line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

