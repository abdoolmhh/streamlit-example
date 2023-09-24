import streamlit as st
import pandas as pd
import pyshark

# Create a title and a sidebar
st.title ("Packet Capture")
st.sidebar.header ("Options")

# Get the interface and filter from the user
interface = st.sidebar.selectbox ("Select interface", ["1", "2", "3"])
filter = st.sidebar.text_input ("Enter filter", value="http")

# Create a button to start capturing
if st.sidebar.button ("Start"):
    # Capture packets from the selected interface and filter
    capture = pyshark.LiveCapture (interface=interface, display_filter=filter)
    # Create an empty dataframe to store the packet data
    df = pd.DataFrame (columns=["Source IP", "Destination IP", "HTTP Method", "HTTP Host", "HTTP URI"])
    # Loop through captured packets and append them to the dataframe
    for packet in capture.sniff_continuously ():
        df = df.append ({
            "Source IP": packet.ip.src,
            "Destination IP": packet.ip.dst,
            "HTTP Method": packet.http.request_method,
            "HTTP Host": packet.http.host,
            "HTTP URI": packet.http.request_uri
        }, ignore_index=True)
        # Display the dataframe as a table
        st.table (df)
        # Display a chart of packets by source IP address
        st.bar_chart (df["Source IP"].value_counts ())
        # Create a button to stop capturing
        if st.button ("Stop"):
            # Terminate the script execution
            st.stop ()
    # Create a button to download the captured packets as a CSV file
    st.download_button ("Download CSV", df.to_csv (), file_name="packets.csv")
