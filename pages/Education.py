import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.graph_objects as go


data = pd.read_csv("data/Education/data.csv")


def write():
    options = st.multiselect(
        "What features do you want to compare?",
        ["Purchase", "Marital Status", "Costs", "Income", "users_day"]
    )

    if "Income" in options:
        fig = px.bar(
            data,
            x="Education",
            y="Income",
            color="Marital_Status"
        )

        fig.update_layout(
            title_text="Relation between Education and Marital Status with Income",
            title_x=0.5
        )

        st.plotly_chart(fig, use_container_width=True)

    if "Costs" in options:
        fig = px.bar(
            data,
            x="Education",
            y="Costs",
            color="Marital_Status"
        )

        fig.update_layout(
            title_text="Relation between Education and Marital Status with Costs",
            title_x=0.5
        )

        st.plotly_chart(fig, use_container_width=True)

    if "Purchase" in options:
        fig = px.bar(
            data,
            x="Education",
            y="Purchase",
            color="Marital_Status"
        )

        fig.update_layout(
            title_text="Relation between Education and Marital Status with Purchase",
            title_x=0.5
        )

        st.plotly_chart(fig, use_container_width=True)

    if "users_day" in options:
        fig = px.bar(
            data,
            x="Education",
            y="users_day",
            color="Marital_Status"
        )

        fig.update_layout(
            title_text="Relation between Education and Marital Status with Users Day",
            title_x=0.5
        )

        st.plotly_chart(fig, use_container_width=True)

    if "Marital Status" in options:
        chart = (
            alt.Chart(data)
            .mark_bar()
            .encode(
                x="Education",
                y="count()",
                color="Marital_Status",
                tooltip="count()"
            )
            .properties(
                title="Relation between Education and Marital Status"
            )
        )

        st.altair_chart(chart, use_container_width=True)

    education_counts = data["Education"].value_counts()

    fig = go.Figure(
        data=[
            go.Pie(
                labels=education_counts.index,
                values=education_counts.values
            )
        ]
    )

    st.plotly_chart(fig, use_container_width=True)
