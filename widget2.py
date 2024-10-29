import streamlit as st
import pandas as pd
import requests

cloud_function_url = "https://europe-west4-ergasia-serverless.cloudfunctions.net/graphs"
data = ""
def load_widget():
    st.header("Widget 2: Charts")
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
            st.write("Total: " + str(data.get("totalFirst")))
            st.write("Average: " + str(data.get("avgFirst")))
            st.write("Highest: " + str(data.get("maxFirst")))
                     
            st.subheader("Salaries")
            st.line_chart(data.get("second"))
            st.write("Total: " + str(data.get("totalSecond")))
            st.write("Average: " + str(data.get("avgSecond")))
            st.write("Highest: " + str(data.get("maxSecond")))

            st.subheader("Sales")
            st.area_chart(data.get("Third"))
            st.write("Total: " + str(data.get("totalThird")))
            st.write("Average: " + str(data.get("avgThird")))
            st.write("Highest: " + str(data.get("maxThird")))
                     

            return response  # Assuming the response is in JSON format
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Request failed: {e}"