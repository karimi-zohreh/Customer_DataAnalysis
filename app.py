import streamlit as st

from pages import home, Age, Education, Marital_Status


st.set_page_config(
    page_title="Customer Data Analysis",
    layout="wide"
)


st.sidebar.title("Customer Data Analysis")

page = st.sidebar.radio(
    "Select a page:",
    [
        "Home",
        "Age",
        "Education",
        "Marital Status"
    ]
)


if page == "Home":
    home.write()

elif page == "Age":
    Age.write()

elif page == "Education":
    Education.write()

elif page == "Marital Status":
    Marital_Status.write()
