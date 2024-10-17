import streamlit as st
import requests
import json

# URL of the AWS Lambda function's API Gateway endpoint
LAMBDA_URL = "https://g8qjzmodh4.execute-api.eu-north-1.amazonaws.com/default/textAnalysisLambda"

def load_widget():
    st.header("Widget 6: Text Analysis")
    st.write("This widget sends text to a serverless AWS Lambda function and displays text analysis.")

    # Create a text area for user input
    user_input = st.text_area("Enter some text to analyze:")

    # Add a button to trigger the text analysis
    if st.button("Analyze"):
        if user_input:
            # Send the input to the AWS Lambda function and get the result
            result = analyze_text(user_input)

            # Display the results directly from the Lambda response
            st.write(f"Character Count: {result.get('char_count', 'N/A')}")
            st.write(f"Word Count: {result.get('word_count', 'N/A')}")

            # Display word frequency
            st.write("Word Frequency:")
            word_frequency = result.get('word_frequency', {})
            for word, frequency in word_frequency.items():
                st.write(f"{word}: {frequency}")
        else:
            st.write("Please enter some text to analyze.")

# Function to call AWS Lambda function for text analysis
def analyze_text(text):
    try:
        # Send a POST request to the AWS Lambda function with the text
        response = requests.post(LAMBDA_URL, json={"text": text})

        # Parse and return the response JSON
        return response.json()
    except Exception as e:
        return {"error": str(e)}
