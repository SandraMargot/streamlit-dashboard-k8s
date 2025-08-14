"""
Streamlit dashboard example for portfolio demonstration.
Developed by Sandra Margot to showcase Kubernetes (Minikube) deployment skills
using a containerized Python application in a WSL2 environment.

This code is intentionally simple for demonstration purposes.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Kubernetes Streamlit Dashboard", layout="wide")

st.title("Kubernetes Streamlit Dashboard")
st.write(
    "This demo application is deployed in a containerized Streamlit environment on a Kubernetes cluster "
    "(Minikube) running inside WSL2. It demonstrates basic dashboard components and interactivity."
)

# KPI metrics
col1, col2, col3 = st.columns(3)
col1.metric("Users", "1,024", "+12%")
col2.metric("Revenue", "$12.3k", "-3%")
col3.metric("Conversion Rate", "4.7%", "+0.5%")

# Interactive section
st.subheader("Random Data Visualization")
n_points = st.slider("Number of points", min_value=10, max_value=200, value=50)

# Generate data
data = pd.DataFrame({
    "x": np.random.randn(n_points),
    "y": np.random.randn(n_points)
})

# Scatter plot
fig, ax = plt.subplots()
ax.scatter(data["x"], data["y"], alpha=0.6)
ax.set_title("Random Scatter Plot")
st.pyplot(fig)

st.info("This dashboard is deployed using Minikube in a WSL2 environment.")
