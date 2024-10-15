import streamlit as st
from datetime import datetime
import requests

cloud_function_url = "https://europe-west4-ergasia-serverless.cloudfunctions.net/Greetings"

def load_widget():
    st.header("Widget 1")
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = greetings(data);
    """st.write("This is the content of Widget 1.")"""

def greetings(data):
    try:
        # Send request to Google Cloud Function
        response = requests.post(cloud_function_url, json={"data": data})
        
        # Check if the request was successful
        if response.status_code == 200:
            st.write(response.text)
            return response  # Assuming the response is in JSON format
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Request failed: {e}"