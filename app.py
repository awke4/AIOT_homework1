import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Business Understanding
st.title("Simple Linear Regression with CRISP-DM")
st.markdown("""
This application demonstrates a simple linear regression model following the CRISP-DM methodology.
- **Business Objective:** To understand the relationship between an independent variable (X) and a dependent variable (y).
- **Success Criteria:** Successfully build a linear regression model that can predict y given X.
""")

# 2. Data Understanding
st.sidebar.header("CRISP-DM Steps")
st.sidebar.markdown("""
- **1. Business Understanding**
- **2. Data Understanding**
- **3. Data Preparation**
- **4. Modeling**
- **5. Evaluation**
- **6. Deployment**
""")

st.sidebar.header("Parameters")
a = st.sidebar.slider("Slope (a)", 0.0, 10.0, 2.0, 0.1)
noise = st.sidebar.slider("Noise", 0.0, 10.0, 1.0, 0.1)
num_points = st.sidebar.slider("Number of Points", 10, 1000, 100, 10)

# 3. Data Preparation
st.header("3. Data Preparation")
X = np.linspace(0, 10, num_points)
y = a * X + np.random.normal(0, noise, num_points)
X = X.reshape(-1, 1)

st.markdown(f"""
- Generated {num_points} data points.
- Independent variable (X) is a sequence from 0 to 10.
- Dependent variable (y) is calculated as `y = {a} * X + noise`.
""")

# 4. Modeling
st.header("4. Modeling")
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

st.markdown("""
- A `LinearRegression` model from `scikit-learn` is used.
- The model is trained on the generated data.
""")

# 5. Evaluation
st.header("5. Evaluation")
st.markdown(f"""
- **Original Slope (a):** {a}
- **Model Slope (Coefficient):** {model.coef_[0]:.2f}
- **Model Intercept:** {model.intercept_:.2f}
""")

fig, ax = plt.subplots()
ax.scatter(X, y, label="Original Data")
ax.plot(X, y_pred, color='red', label="Regression Line")
ax.set_xlabel("X")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)


# 6. Deployment
st.header("6. Deployment")
st.markdown("""
This Streamlit application is the deployment of the model. You can interact with the model by changing the parameters in the sidebar.
""")
