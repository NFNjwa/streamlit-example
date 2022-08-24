import streamlit as st
import numpy as np
import pandas as pd

st.header("Final Assignment Streamlit App")
st.write(pd.DataFrame({
    'No.': ['0', '1', '2'],
    'Name': ['Iris-setosa','Iris-versicolor','Iris-virginica']
}))
