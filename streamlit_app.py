import streamlit as st
import pandas as pd
import pyshark

# Create a title and a sidebar with a link
st.title ("Packet Capture", anchor="title")
st.sidebar.header ("Options")

# Get the interface and filter from the user with keys
interface = st.sidebar.selectbox ("Select interface", ["1", "2", "3"], key="interface")
filter = st.sidebar.text_input ("Enter filter", value="http", key="filter")

# Create a button to start capturing and get its value
start = st.sidebar.button ("Start")

# Capture packets from the selected interface and filter only if the button is clicked
if start:
    # Capture packets from the selected interface and filter with summaries
    # Specify the tshark path as an argument
    capture = pyshark.LiveCapture (interface=interface, display_filter=filter, tshark_path='/path/to/tshark', only_summaries=True)
    
    # Define a function that takes a packet and returns a dictionary of data
    def get_packet_data (packet):
        return {
            "Source IP": packet.ip.src,
            "Destination IP": packet.ip.dst,
            "HTTP Method": packet.http.request_method,
            "HTTP Host": packet.http.host,
            "HTTP URI": packet.http.request_uri
        }

    # Apply the function on each packet and get a list of results
    packet_data = capture.apply_on_packets (get_packet_data)

    # Create a dataframe from the list of results
    df = pd.DataFrame (packet_data)

    # Display the dataframe as a table with a wider width
    st.table (df, width=800)
