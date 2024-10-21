import streamlit as st
import requests
from datetime import datetime

def load_widget():
    st.header("Widget 5: NASA Astronomy Picture of the Day")
    st.write("This widget lets the user choose a date and displays NASA's Astronomy Picture of the Day for that specific date.")

    st.write("""**Note**: This widget only displays images that are believed to be in the public domain based on the information provided by the NASA APOD API.
    If a photo or video is copyrighted, it will not be shown. Please choose another date if that happens.""")

    # Get API key from Streamlit Secrets
    api_key = st.secrets["api"]["nasa_apod_key"]

    # Date input for user to select a date
    selected_date = st.date_input("Select a date:", datetime.now().date(), datetime(1995, 6, 16).date(), datetime.now().date())

    # Format the date for the API request
    formatted_date = selected_date.strftime("%Y-%m-%d")

    # Define API URL
    api_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={formatted_date}"

    # Make the request
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        # Get copyright field
        copyright_info = data.get("copyright")

        if copyright_info:
            # If there is a copyright field, show a message and ask the user to choose another date
            st.warning("Photo or video not in the public domain. Please choose another date.")
        else:
            # Display the title of the APOD
            st.subheader(data.get("title", "Astronomy Picture of the Day"))

            # Display the image or video
            media_type = data.get("media_type")
            if media_type == "image":
                st.image(data.get("url"))
            elif media_type == "video":
                st.video(data.get("url"))

            # Display the explanation of the image
            explanation = data.get("explanation", "No explanation available.")
            st.markdown(f"**Explanation:** \n\n{explanation}")

    else:
        st.error("Error fetching data from NASA APOD API.")



