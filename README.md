# Simple Linear Regression with CRISP-DM

This project is a web application that demonstrates simple linear regression. It is built with Python and Streamlit, and follows the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology.

## Features

*   **Interactive Interface:** Users can adjust the parameters of the linear data generation process, including the slope (a), intercept (b), noise level, and the number of data points.
*   **Real-time Updates:** The application updates in real-time to show how changes in the parameters affect the data and the regression model.
*   **CRISP-DM Framework:** The application is structured around the six phases of the CRISP-DM framework, providing explanations for each step.
*   **Visualization:** The generated data and the fitted regression line are visualized using Altair.
*   **Model Evaluation:** The performance of the linear regression model is evaluated using the R-squared metric.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the application, use the following command:

```bash
streamlit run app.py
```

This will start a local web server and open the application in your browser.

## CRISP-DM Framework

This project follows the CRISP-DM methodology:

1.  **Business Understanding:** The goal is to create an educational tool for understanding simple linear regression.
2.  **Data Understanding:** The data is synthetically generated based on user-defined parameters.
3.  **Data Preparation:** The generated data is formatted into a pandas DataFrame for modeling.
4.  **Modeling:** A simple linear regression model from scikit-learn is used to fit the data.
5.  **Evaluation:** The model is evaluated using the R-squared metric and visualized.
6.  **Deployment:** The model is deployed as an interactive web application using Streamlit.
