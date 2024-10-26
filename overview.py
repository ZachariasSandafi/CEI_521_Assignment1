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
      - **Widget 1**: 
      - **Widget 2**: 
      - **Widget 3**:             
    
    <br>
                
    - **Zacharias Sandafi** was responsible for the **interactive widgets** . These widgets, which require user input, include:
      - **Widget 4**: Dog Breeds Information (online service)
      - **Widget 5**: NASA Astronomy Picture of the Day (online service)
      - **Widget 6**: Text Analysis (AWS Lambda function)
                
    ### Widget Explanations
                
    #### Non-Interactive Widgets by Charalampos:
    #### Widget 1: 
    small explanation....
    - **Purpose**: 
    - **Implementation**: 
    - **Data Source**: 

    #### Widget 2: 
    small explanation....    
    - **Purpose**:
    - **Implementation**:
    - **Data Source**: 

    #### Widget 3: 
    small explanation....
    - **Purpose**: 
    - **Implementation**: 
    - **Data Source**:
                
    #### Interactive Widgets by Zacharias:
    #### Widget 4: Dog Breeds Information
    This widget utilizes **TheDogAPI** to fetch and display information and images about various dog breeds.
    - **Purpose**: Users can search or select a breed, displaying details like breed group, temperament, life span, height, and weight.
    - **Implementation**: After selecting a breed, an API request fetches breed-specific data, including images, and displays the data on the screen.
    - **Data Source**: TheDogAPI.

    #### Widget 5: Astronomy Picture of the Day
    Using NASA's **Astronomy Picture of the Day (APOD)** API, this widget retrieves an astronomical image or video and its description for a selected date.
    - **Purpose**: Users can select any date (starting from 1995-06-16, the beginning of the APOD service) to view NASA's featured astronomical media for that day.
    - **Implementation**: After selecting a date, an API request fetches data for the Astronomy Picture of the Day on that specific date and display the image/video along with an explanation if it’s in the public domain. If it’s copyrighted, users are prompted to choose a different date.
    - **Data Source**: NASA's APOD API.

    #### Widget 6: Text Analysis
    This widget uses an **AWS Lambda function** to perform in-depth text analysis, including word count, frequency, sentence analysis, and more.
    - **Purpose**: Users can input text, and the widget returns detailed text analysis, which includes metrics like character count, word frequency, and sentence analysis.
    - **Implementation**: The text is sent to an AWS Lambda function, which analyzes and returns data on the provided text. The data is displayed in categorized sections.
    - **Data Source**: Custom AWS Lambda endpoint.
    """, unsafe_allow_html=True)

