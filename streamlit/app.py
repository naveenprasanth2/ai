import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit!!!")

st.write("This is a simple Streamlit app.")

df = pd.DataFrame({
    "Marks": [1, 2, 3, 4],
    "Student": [10, 20, 30, 40],
})

st.line_chart(df)
