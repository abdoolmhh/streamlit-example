# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and description
st.title("Network Traffic Analysis Tool")
st.write("Upload your network traffic data file to analyze and visualize it.")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read data into a DataFrame
    data = pd.read_csv(uploaded_file)

    # Data summary
    st.subheader("Data Summary")
    st.write(data.head())

    # Data analysis options
    analysis_option = st.selectbox("Select Analysis Type", ["Summary Statistics", "Visualization"])

    if analysis_option == "Summary Statistics":
        # Display summary statistics
        st.subheader("Summary Statistics")
        st.write(data.describe())

    elif analysis_option == "Visualization":
        # Data visualization options
        visualization_option = st.selectbox("Select Visualization Type", ["Histogram", "Line Plot"])

        if visualization_option == "Histogram":
            # Plot a histogram
            selected_column = st.selectbox("Select a Column", data.columns)
            st.subheader(f"Histogram of {selected_column}")
            plt.hist(data[selected_column], bins=20)
            st.pyplot()

        elif visualization_option == "Line Plot":
            # Plot a line chart
            x_column = st.selectbox("Select X-Axis Column", data.columns)
            y_column = st.selectbox("Select Y-Axis Column", data.columns)
            st.subheader(f"Line Plot: {x_column} vs. {y_column}")
            plt.plot(data[x_column], data[y_column])
            st.pyplot()

# About section
st.sidebar.title("About")
st.sidebar.info(
    "This is a simple Network Traffic Analysis Tool created using Streamlit. "
    "Upload your CSV file and choose the type of analysis or visualization you want to perform."
)

# Footer
st.sidebar.footer("Built with ❤️ by Your Name")

