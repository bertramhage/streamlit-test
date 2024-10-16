import streamlit as st
import pandas as pd

st.title('Hello World!')

st.write('This is a simple example of a Streamlit app.')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write('Here is a DataFrame:')

st.write(df)