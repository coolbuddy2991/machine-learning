import streamlit as st
import numpy as np

st.header("This app calculates the sum of the two numbers")

a = st.number_input("Please enter a number",min_value=0)
b = st.number_input("Please enter another number",min_value=0)
c = st.number_input("Please enter yet another number", min_value=0)

l = np.array([a,b,c])

result = l.max()

st.subheader("The Addition of the Number is ")
st.subheader(result)
