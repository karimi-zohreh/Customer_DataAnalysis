import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.graph_objects as go


data = pd.read_csv("data/Education/data.csv")


def write():
    options = st.multiselect(
        "What features do you want to compare?",
        ["Purchase", "Education", "Costs", "Income", "users_day"]
    )

    if "Income" in options:
        fig = px.bar(
            data,
            x="Marital_Status",
            y="Income",
            color="Education"
        )

        fig.update_layout(
            title_text="Relation between Marital Status and Education with Income",
            title_x=0.5
        )

        st.plotly_chart(fig, use_container_width=True)

    if "Costs" in options:
        fig = px.bar(
            data,
            x="Marital_Status",
            y="Costs",
            color="Education"
        )

        fig.update_layout(
            title_text="Relation between Marital Status and Education with Costs",
            title_x=0.5
        )

        st.plotly_chart(fig, use_container_width=True)

    if "Purchase" in options:
        fig = px.bar(
            data,
            x="Marital_Status",
            y="Purchase",
            color="Education"
        )

        fig.update_layout(
            title_text="Relation between Marital Status and Education with Purchase",
            title_x=0.5
        )

        st.plotly_chart(fig, use_container_width=True)

    if "users_day" in options:
        fig = px.bar(
            data,
            x="Marital_Status",
            y="users_day",
            color="Education"
        )

        fig.update_layout(
            title_text="Relation between Marital Status and Education with Users Day",
            title_x=0.5
        )

        st.plotly_chart(fig, use_container_width=True)

    if "Education" in options:
        chart = (
            alt.Chart(data)
            .mark_bar()
            .encode(
                x="Marital_Status",
                y="count()",
                color="Education",
                tooltip="count()"
            )
            .properties(
                title="Relation between Marital Status and Education"
            )
        )

        st.altair_chart(chart, use_container_width=True)

    marital_counts = data["Marital_Status"].value_counts()

    fig = go.Figure(
        data=[
            go.Pie(
                labels=marital_counts.index,
                values=marital_counts.values
            )
        ]
    )

    st.plotly_chart(fig, use_container_width=True)
