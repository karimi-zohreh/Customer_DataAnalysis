import streamlit as st
import pandas as pd


df = pd.read_csv("data/Home/data.csv")


def write():
    st.markdown(
        """
        ### Customer Data

        This dataset contains customer information that can be explored
        through the available analysis pages.
        """
    )

    st.dataframe(df, use_container_width=True)
