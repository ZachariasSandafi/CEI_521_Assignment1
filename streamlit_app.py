import streamlit as st

# Title for the main page
st.title("Streamlit App with 6 Sidebar Options")

# Sidebar options as radio buttons
st.sidebar.title("Navigation Menu")
option = st.sidebar.radio(
    "Choose an option:",
    [
        "Home",
        "Show Welcome Message",
        "Display Number",
        "User Details Form",
        "Show a Chart",
        "Contact Us"
    ]
)

# Main page content based on sidebar option
if option == "Home":
    st.header("Home")
    st.write("Welcome to the homepage! Choose an option from the sidebar to explore more.")

elif option == "Show Welcome Message":
    st.header("Welcome to the Streamlit App!")
    st.write("This is a simple app demonstrating a sidebar with 6 options.")

elif option == "User Details Form":
    st.header("User Details Form")
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", 0, 120, 25)
    if st.button("Submit"):
        st.write(f"Hello, {name}! You are {age} years old.")

elif option == "Show a Chart":
    st.header("Sample Chart")
    chart_data = {
        'x': [1, 2, 3, 4, 5],
        'y': [10, 20, 30, 40, 50]
    }
    st.line_chart(chart_data)

elif option == "Contact Us":
    st.header("Contact Us")
    st.write("For inquiries, please reach out at: contact@example.com")
