import streamlit as st

def load_overview():
    st.header("Project Overview")
    st.write("This project was developed by **Charalampos Kampourides** and **Zacharias Sandafi**.")
    
    st.subheader("Project Structure and Collaboration")

    st.markdown("""
    - **Collaboration Method**: To enable real-time collaboration, we used Streamlit’s Community Cloud to host and develop our Streamlit app, allowing us to work on the project simultaneously.
    - **File Organization**: We organized the project into 8 files—one is the main project file, one file is for the Project Overview and six are dedicated to individual widgets. A sidebar, implemented with Streamlit’s option menu, allows users to select each widget and view its content.

    ### Responsibilities
                
    - **Charalampos Kampourides** was responsible for the **non-interactive widgets**. These widgets, which do not require user input, include:
      - **Widget 1**: Personalized Welcome Message (Google Cloud Run Function)
      - **Widget 2**: Chart Data (Google Cloud Run Function)
      - **Widget 3**: Daily News Feed (Online Service)            
    
    <br>
                
    - **Zacharias Sandafi** was responsible for the **interactive widgets** . These widgets, which require user input, include:
      - **Widget 4**: Dog Breeds Information (online service)
      - **Widget 5**: NASA Astronomy Picture of the Day (online service)
      - **Widget 6**: Text Analysis (AWS Lambda function)
                
    ### Widget Explanations
                
    #### Non-Interactive Widgets by Charalampos:
    #### Widget 1: Welcoming Message
    This widget is responsible for greeting the user with a unique message
    - **Purpose**: To welcome users, displaying a different message based on parameters like date and time.
    - **Implementation**: A POST request is made to the Google Cloud Platform serverless function, with the current date and time. The function returns the relevant message,
    - **Data Source**: Custom GCP Serverless Function.

    #### Widget 2: Charts
    This Widget receives data from the back end and visualize it for the user.
    - **Purpose**: To fetch data from a serverless back end and display them to the user in a visual way.
    - **Implementation**: The function generates (or fetches from a database) data to be displayed by the application. The application displays the data alongside some statistics.
    - **Data Source**: Custom GCP Serverless Function

    #### Widget 3: News Feed
    The widget is using TheNewsAPI to display the latest news to the user.
    - **Purpose**: Informing the user about the latest events internationally.
    - **Implementation**: An API request is made fetching the latest articles for a given language (english). It is then displayed on screen alongside the title, image, url etc.
    - **Data Source**: TheNewsAPI.
                
    #### Interactive Widgets by Zacharias:
    #### Widget 4: Dog Breeds Information
    This widget utilizes **TheDogAPI** to fetch and display information and images about various dog breeds.
    - **Purpose**: Users can search or select a breed, displaying details like breed group, temperament, life span, height, and weight.
    - **Implementation**: After selecting a breed, an API request fetches breed-specific data, including images. This data is displayed on the screen.
    - **Data Source**: TheDogAPI.

    #### Widget 5: Astronomy Picture of the Day
    Using NASA's **Astronomy Picture of the Day (APOD)** API, this widget retrieves an astronomical image or video and its description for a selected date.
    - **Purpose**: Users can select any date (starting from 1995-06-16, the beginning of the APOD service) to view NASA's featured astronomical media for that day.
    - **Implementation**: After selecting a date, an API request fetches data for the Astronomy Picture of the Day on that specific date. The image/video and explanation are displayed if the specific media is in the public domain. If it’s copyrighted, users are prompted to choose a different date.
    - **Data Source**: NASA's APOD API.

    #### Widget 6: Text Analysis
    This widget uses an **AWS Lambda function** to perform in-depth text analysis, including word count, frequency, sentence analysis, and more.
    - **Purpose**: Users can input text, and the widget returns detailed text analysis, which includes metrics like character count, word frequency, and sentence analysis.
    - **Implementation**: The text is sent to an AWS Lambda function, which analyzes and returns data on the provided text. The data is displayed in categorized sections.
    - **Data Source**: Custom AWS Lambda endpoint.
    """, unsafe_allow_html=True)

