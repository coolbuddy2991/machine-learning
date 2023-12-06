import streamlit as st
import numpy as np

st.header("This app calculates the highest of numbers")

a = st.number_input("Please enter a number",min_value=0)
b = st.number_input("Please enter another number",min_value=0)
c = st.number_input("Please enter yet another number", min_value=0)

l = np.array([a,b,c])

result = l.max()

st.subheader("The Maximum of the Numbers is ")
st.subheader(result)
