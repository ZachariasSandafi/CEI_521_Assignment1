import streamlit as st
import requests

api_key = st.secrets["api"]["news_api_key"]
url = "https://api.thenewsapi.com/v1/news/top?api_token=" + api_key + "&language=en&limit=3"

def load_widget():
    st.header("Widget 3: News Feed")
    st.write("This widget displays the latest news for the current date")

    data = ""
    response = news(data)


def news(data):
    try:
        # Send request to Google Cloud Function
        response = requests.get(url)
        data = response.json()
        # Check if the request was successful
        if response.status_code == 200:
            for d in data.get("data"):
                st.subheader( d.get("title"))
                st.image( d.get("image_url"))
                st.write( d.get("description"))
                st.write("Read more: " +  d.get("url"))

            return response  # Assuming the response is in JSON format
        else:
            st.write(response.status_code)
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Request failed: {e}"