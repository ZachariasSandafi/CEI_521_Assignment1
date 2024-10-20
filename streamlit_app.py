import streamlit as st
from streamlit_option_menu import option_menu
import widget1
import widget2
import widget3
import widget4
import widget5
import widget6

# Set the title for the home page
st.title("CEI_521 Assignment 1")

# Sidebar menu with icons
with st.sidebar:
    option = option_menu(
        menu_title="Menu",
        options=["Project Overview", "Widget 1", "Widget 2", "Widget 3", "Dog Breeds", "Astronomy Picture of the Day", "Text Analysis"],
        icons=["file-text-fill", "1-circle-fill", "2-circle-fill", "3-circle-fill", "gitlab", "rocket-takeoff", "alphabet-uppercase"],  # Bootstrap icons
        menu_icon="list",  
        default_index=0,  
    )



if option == "Project Overview":
    st.header("Project Overview")
    st.write("Welcome to the project overview! Choose a widget from the sidebar to explore.")

elif option == "Widget 1":
    widget1.load_widget()

elif option == "Widget 2":
    widget2.load_widget()

elif option == "Widget 3":
    widget3.load_widget()

elif option == "Dog Breeds":
    widget4.load_widget()

elif option == "Astronomy Picture of the Day":
    widget5.load_widget()

elif option == "Text Analysis":
    widget6.load_widget()
