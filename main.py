import streamlit as st
# import pandas as pd
st.title("Welcome To My First Stream Lit Application")

st.header("This is Header")

st.subheader("This is SubHeader")

st.markdown("Here we use to right just Text")

st.code(""" for x in range(1,5):
            print("Hello World")
            """)
# dataset = pd.read_csv("test.csv")
# st.dataframe(dataset)

name = st.text_input("Enter Your Name")
state = st.text_input("Enter Your State")
adr = st.text_area("Enter Your Address")
classNo = st.selectbox("Select your class from below lists ",(1,2,3,4,5))

button1 = st.button("Submit")
if button1 :
    st.markdown(f'''
            Name : {name}
            State : {state}
            Address : {adr}
            Class : {classNo}
            ''')