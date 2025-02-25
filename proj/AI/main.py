import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'col1' : [1,2,3,4],
    'col2' : [10,20,30,40],
})

st.title('Artificial Intelligent Project')
st.write(df)