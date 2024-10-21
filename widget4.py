import streamlit as st
import requests

# API key 
API_KEY = st.secrets["api"]["dog_api_key"]

# The Dog API base URL
BASE_URL = "https://api.thedogapi.com/v1"

# Headers with API key
headers = {
    "x-api-key": API_KEY
}

# Function to fetch all breeds
def get_breeds():
    response = requests.get(f"{BASE_URL}/breeds", headers=headers)
    return response.json()

# Function to fetch breed-specific images
def get_breed_images(breed_id):
    response = requests.get(f"{BASE_URL}/images/search?breed_id={breed_id}&limit=3", headers=headers)  # Limit to 3 images
    return response.json()

# Function to display breed information
def display_breed_info(breed):
    st.header(breed['name'])
    st.write(f"**Breed Group**: {breed['breed_group']}")
    st.write(f"**Temperament**: {breed['temperament']}")
    st.write(f"**Life Span**: {breed['life_span']}")
    st.write(f"**Height**: {breed['height']['metric']} cm")
    st.write(f"**Weight**: {breed['weight']['metric']} kg")

# Function to display breed images
def display_breed_images(images):
    for image in images:
        st.image(image['url'], width=300)

# Function to load the widget
def load_widget():
    st.header("Widget 4")
    st.write("This is the content of Widget 4.")
    
    # Fetching breeds data
    breeds = get_breeds()

    # Dropdown with search functionality for breed selection
    breed_names = [breed['name'] for breed in breeds]
    selected_breed_name = st.selectbox("Select a breed", breed_names, help="Start typing to filter breeds")

    # Display information of the selected breed
    if selected_breed_name:
        selected_breed = next(breed for breed in breeds if breed['name'] == selected_breed_name)
        
        # Display breed facts
        display_breed_info(selected_breed)
        
        # Fetch and display breed-specific images
        breed_images = get_breed_images(selected_breed['id'])
        display_breed_images(breed_images)