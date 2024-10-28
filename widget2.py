import streamlit as st
import pandas as pd
import requests

cloud_function_url = "https://europe-west4-ergasia-serverless.cloudfunctions.net/graphs"
data = ""
def load_widget():
    st.header("Widget 2: Graphs")
    response = graphs(data);
    """st.write("This is the content of Widget 2.")"""

def graphs(data):
    try:
        # Send request to Google Cloud Function
        response = requests.post(cloud_function_url, json={"data": data})
        data = response.json()
        # Check if the request was successful
        if response.status_code == 200:
            first = data.get("first")
            st.subheader("Assets")
            st.bar_chart(first)
            st.write("Total: ")
            st.write("Winner: " )
                     
            st.subheader("Sallaries")
            st.line_chart(data.get("second"))
            st.write("Total: ")
            st.write("Winner: " )

            return response  # Assuming the response is in JSON format
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Request failed: {e}"