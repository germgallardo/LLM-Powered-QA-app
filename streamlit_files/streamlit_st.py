import streamlit as st
import pandas as pd

st.title("Hello Streamlit World! :100:")

# Displaying Data on the Screen:
# Using st.write()
st.write("We learn streamlit!")

l1 = [1,2,3]
st.write(l1)

l2 = list("abc")
d1 = dict(zip(l1, l2))
st.write(d1)

# Using Magic
"Displaying using Magic :smile:"

df = pd.DataFrame({
    "first column" : [1,2,3,4],
    "second column" : [10,20,30,40]
})

df  # it's the same as st.write(df)