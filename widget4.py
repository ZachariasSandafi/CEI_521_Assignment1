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
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching breeds: {response.status_code} - {response.text}")
        return []

# Function to fetch breed-specific images
def get_breed_images(breed_id):
    response = requests.get(f"{BASE_URL}/images/search?breed_id={breed_id}&limit=3", headers=headers)  # Limit to 3 images
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching images: {response.status_code} - {response.text}")
        return []

# Function to display breed information
def display_breed_info(breed):
    st.header(breed['name'])
    st.write(f"**Breed Group**: {breed.get('breed_group', 'N/A')}")  
    st.write(f"**Temperament**: {breed.get('temperament', 'N/A')}")
    st.write(f"**Life Span**: {breed.get('life_span', 'N/A')}")
    st.write(f"**Height**: {breed.get('height', {}).get('metric', 'N/A')} cm") 
    st.write(f"**Weight**: {breed.get('weight', {}).get('metric', 'N/A')} kg")

# Function to display breed images
def display_breed_images(images):
    for image in images:
        st.image(image['url'], width=300)

# Function to load the widget
def load_widget():
    st.header("Widget 4: TheDogAPI")
    st.write("This widget lets the user select or search for a dog breed and displays certain information and photos of the selected dog breed.")
    
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