import streamlit as st
from streamlit_option_menu import option_menu
import widget1
import widget2
import widget3
import widget4
import widget5
import widget6
import overview

# Set the title for the home page
st.title("CEI_521 Assignment 1")

# Sidebar menu with icons
with st.sidebar:
    option = option_menu(
        menu_title="Menu",
        options=["Project Overview", "Welcome Message", "Charts", "News Feed", "Dog Breeds", "Astronomy Picture of the Day", "Text Analysis"],
        icons=["file-text-fill", "brightness-alt-high-fill", "bar-chart-line-fill", "newspaper", "gitlab", "rocket-takeoff", "alphabet-uppercase"],  # Bootstrap icons
        menu_icon="list",  
        default_index=0,  
    )



if option == "Project Overview":
    overview.load_overview()

elif option == "Welcome Message":
    widget1.load_widget()

elif option == "Charts":
    widget2.load_widget()

elif option == "News Feed":
    widget3.load_widget()

elif option == "Dog Breeds":
    widget4.load_widget()

elif option == "Astronomy Picture of the Day":
    widget5.load_widget()

elif option == "Text Analysis":
    widget6.load_widget()
