# Customer Data Analysis

An interactive **customer data analysis and visualization application** built with Python and Streamlit.

The project explores customer-related data through interactive charts and visualizations, focusing on variables such as age, education, marital status, income, costs, purchase, and users per day.

## Project Overview

The application provides several analysis pages that allow different customer attributes to be explored and compared.

The visualizations are created using **Plotly** and **Altair**, while **Pandas** is used for loading and working with the datasets.

## Analysis Pages

### Home

The Home page provides an overview of the customer dataset and displays the available data in an interactive table.

### Age

The Age page explores relationships between age and other customer attributes, including:

* Education
* Marital Status
* Income
* Costs

### Education

The Education page allows users to compare education with:

* Income
* Costs
* Purchase
* Users per day
* Marital Status

It also provides a distribution of customers across education categories.

### Marital Status

The Marital Status page allows users to compare marital status with:

* Income
* Costs
* Purchase
* Users per day
* Education

It also provides a distribution of customers across marital-status categories.

## Technologies

* Python
* Pandas
* Streamlit
* Plotly
* Altair

## Data

The project contains two datasets:

```text
data/
├── Education/
│   ├── data.csv
│   └── data.xlsx
│
└── Home/
    ├── data.csv
    └── data.xlsx
```

The analysis pages currently use the CSV files.

## Application Structure

```text
customerDataAnalysis/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── Education/
│   │   ├── data.csv
│   │   └── data.xlsx
│   │
│   └── Home/
│       ├── data.csv
│       └── data.xlsx
│
└── pages/
    ├── Age.py
    ├── Education.py
    ├── Marital_Status.py
    └── home.py
```

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Purpose

This project was created as a practical exercise in **customer data analysis, exploratory visualization, and interactive dashboard development using Python**.
