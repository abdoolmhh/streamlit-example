import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit page configuration
st.set_page_config(
    page_title="Network Traffic Analyzer",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Title and Header
st.title("Network Traffic Analyzer")
st.header("Analyze network traffic data effortlessly")

# Sidebar - User Input
st.sidebar.header("User Input")

# Upload Data
st.sidebar.subheader("Upload Network Traffic Data")
uploaded_file = st.sidebar.file_uploader("Choose a PCAP file for analysis", type=["pcap", "pcapng"])

# Options for Analysis
st.sidebar.subheader("Select Analysis Options")
show_summary = st.sidebar.checkbox("Show Traffic Summary")
show_visualizations = st.sidebar.checkbox("Show Visualizations")

# Main Content
st.subheader("Network Traffic Analysis")

# Data Upload and Analysis
if uploaded_file:
    st.success("File successfully uploaded. Analyzing...")

    # Perform analysis on uploaded_file (Use your analysis code here)
    # Assuming you have a DataFrame named 'analysis_results' with columns like 'Packet_Category', 'Send_Receive', etc.

    if show_summary:
        st.subheader("Traffic Summary")
        # Display summary data here (e.g., value counts of different packet categories)

        if 'analysis_results' in locals():
            packet_categories = analysis_results['Packet_Category'].value_counts()
            st.write(packet_categories)

    if show_visualizations:
        st.subheader("Traffic Visualizations")
        # Display visualizations here (e.g., pie chart of packet categories)

        if 'analysis_results' in locals():
            plt.figure(figsize=(8, 8))
            sns.set_palette("Set3")
            analysis_results['Packet_Category'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette())
            plt.title("Packet Category Distribution")
            st.pyplot()

# About Section
st.sidebar.header("About")
st.sidebar.write("This web app is designed to analyze network traffic data and provide insights.")
st.sidebar.write("Developed by Abdoolgram")
