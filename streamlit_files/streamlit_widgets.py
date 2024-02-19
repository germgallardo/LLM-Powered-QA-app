import streamlit as st
import pandas as pd

# Text Input
name = st.text_input("Your name: ")
if name:
    st.write(f"Hello {name}!")

# Number Input
x = st.number_input("Enter a number", min_value=1, max_value=99, step=1)
st.write(f"The current number is {x}")

st.divider()    # adds a new line/separator

# Buttons
clicked = st.button("Click me!")
if clicked:
    st.write(":ghost:" * 3)

st.divider()

# Checkbox
agree = st.checkbox("I agree")
if agree:   # if the user has checked the box
    "Great, you agreed!"

checked = st.checkbox("Continue", value=True)
if checked:
    ":+1:" * 5

df = pd.DataFrame({"Name" : ["Anne", "Mario", "Douglas"],
                   "Age" : [30, 25, 40]
                   })
if st.checkbox("Show data"):
    st.write(df)

st.divider()

# Radio
pets = ["cat", "dog", "fish", "turtle"]
pet = st.radio("Favorite pet", pets, index=2, key="your_pet")
st.write(f"Your favorite pet: {pet}")
st.write(f"Your favorite pet: {st.session_state.your_pet}")

st.divider()

# Select box
cities = ["London", "Berlin", "Paris", "Madrid"]
city = st.selectbox("Your city", cities, index=1)
st.write(f"You live in {city}")

st.divider()

# Slider
x = st.slider("x", value=15, min_value=12, max_value=78, step=3)
st.write(f"x is {x}")

st.divider()

# File uploader
uploaded_file = st.file_uploader("Upload a file:", type=["txt", "csv", "xlsx"])
if uploaded_file:
    st.write(uploaded_file)
    if uploaded_file.type == "text/plain":
        from io import StringIO
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        st.write(string_data)
    if uploaded_file.type == "text/csv":
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.write(df)
    else:
        import pandas as pd
        df = pd.read_excel(uploaded_file)
        st.write(df)

st.divider()

# Camera input
camera_photo = st.camera_input("Take a photo")
if camera_photo:
    st.image(camera_photo)

st.image("https://static.streamlit.io/examples/owl.jpg")