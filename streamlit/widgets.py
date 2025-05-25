import streamlit as st

st.write("Hello Streamlit!!!")
name = st.text_input("Please enter your name")
if name:
    st.write(f"Hello {name}!")
age = st.slider("Please select your age", 0, 100, 25)
if age:
    st.write(f"You are {age} years old.")
choice = st.selectbox("Please select your programming language", ["Python", "Java", "C++"])
st.write(f"You selected {choice} as your programming language.")
uploaded = st.file_uploader("Upload a file", type=["csv", "txt", "png", "jpg"])
if uploaded:
    st.write("File uploaded successfully!")
    st.image(uploaded)