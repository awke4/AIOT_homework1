import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import altair as alt

# Set page title
st.set_page_config(page_title="Simple Linear Regression with CRISP-DM")

# App title
st.title("Simple Linear Regression with CRISP-DM")

# --- 1. Business Understanding ---
st.header("1. Business Understanding")
st.write(
    "The goal of this application is to understand the relationship between an independent variable 'x' and a dependent variable 'y' "
    "through simple linear regression. Users can adjust the parameters of the data generation process to see how they affect the "
    "resulting regression model. This helps in understanding the core concepts of linear regression and the impact of data characteristics."
)

# --- 2. Data Understanding ---
st.header("2. Data Understanding")
st.write(
    "We will generate synthetic data for this task. The data is created based on the linear equation `y = a*x + b`, "
    "with some random noise added. You can control the parameters of this data generation process using the sliders in the sidebar."
)

# Sidebar for user input
st.sidebar.header("Data Generation Parameters")
a = st.sidebar.slider("Slope (a)", -10.0, 10.0, 2.0, 0.1)
b = st.sidebar.slider("Intercept (b)", -10.0, 10.0, 1.0, 0.1)
noise = st.sidebar.slider("Noise", 0.0, 10.0, 1.0, 0.1)
num_points = st.sidebar.slider("Number of points", 10, 1000, 100, 10)

# --- 3. Data Preparation ---
st.header("3. Data Preparation")
st.write(
    "The data is generated and prepared for modeling. We create a pandas DataFrame with two columns, 'x' and 'y'. "
    "This DataFrame is then used to train our linear regression model."
)

# Generate data
np.random.seed(42)
x = np.linspace(-10, 10, num_points)
y = a * x + b + np.random.normal(0, noise, num_points)

df = pd.DataFrame({'x': x, 'y': y})

st.write("Sample of the generated data:")
st.write(df.head())


# --- 4. Modeling ---
st.header("4. Modeling")
st.write(
    "We use a simple linear regression model from the scikit-learn library to fit the generated data. "
    "The model learns the best-fit line that describes the relationship between 'x' and 'y'."
)
# Perform linear regression
model = LinearRegression()
model.fit(df[['x']], df['y'])

y_pred = model.predict(df[['x']])


# --- 5. Evaluation ---
st.header("5. Evaluation")
st.write(
    "The model's performance is evaluated using the R-squared value, which measures how well the regression line "
    "approximates the real data points. An R-squared value of 1 indicates a perfect fit. We also visualize the "
    "data points and the regression line."
)
r2 = r2_score(df['y'], y_pred)

# Plot data and regression line
chart = alt.Chart(df).mark_circle().encode(
    x='x',
    y='y'
).properties(
    title="Data and Regression Line"
)

line = alt.Chart(pd.DataFrame({'x': x, 'y': y_pred})).mark_line(color='red').encode(
    x='x',
    y='y'
)

st.altair_chart(chart + line, use_container_width=True)

# Display results
st.subheader("Results")
st.write(f"Original Equation: y = {a:.2f}x + {b:.2f}")
st.write(f"Regression Equation: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}")
st.write(f"R-squared: {r2:.2f}")


# --- 6. Deployment ---
st.header("6. Deployment")
st.write(
    "This Streamlit application itself is the deployment of the model. It provides an interactive interface for users "
    "to explore the linear regression model and its sensitivity to different parameters."
)
