import streamlit as st
import requests
import json

# URL of the AWS Lambda function's API Gateway endpoint (replace with your actual URL)
LAMBDA_URL = "https://g8qjzmodh4.execute-api.eu-north-1.amazonaws.com/default/textAnalysisLambda"

def load_widget():
    st.header("Widget 6: Text Analysis")
    st.write("This widget sends text to a serverless AWS Lambda function and displays detailed text analysis.")

    # Create a text area for user input
    user_input = st.text_area("Enter some text to analyze:")

    # Add a button to trigger the text analysis
    if st.button("Analyze"):
        if user_input:
            # Send the input to the AWS Lambda function
            result = analyze_text(user_input)

            # Organizing the output into different sections
            
            # Character and Word Count
            st.subheader("Character & Word Count")
            st.write(f"**Character Count**: {result.get('char_count', 'N/A')}")
            st.write(f"**Word Count**: {result.get('word_count', 'N/A')}")
            st.write(f"**Unique Word Count**: {result.get('unique_word_count', 'N/A')}")

            # Word Data Section
            st.subheader("Word Analysis")
            
            # Display sorted word frequency
            st.write("**Word Frequency (Sorted by Most Common)**:")
            word_frequency = result.get('word_frequency', {})
            for word, frequency in word_frequency.items():
                st.write(f"{word.capitalize()}: {frequency}")
            
            # Display longest and shortest words
            st.write(f"**Longest Word(s)**: {', '.join(result.get('longest_words', []))}")
            st.write(f"**Shortest Word(s)**: {', '.join(result.get('shortest_words', []))}")
            st.write(f"**Average Word Length**: {result.get('avg_word_length', 'N/A'):.2f}")

            # Sentence Data Section
            st.subheader("Sentence Analysis")
            
            st.write(f"**Sentence Count**: {result.get('sentence_count', 'N/A')}")
            st.write(f"**Longest Sentence(s) (in words)**: {', '.join(result.get('longest_sentences', []))}")
            st.write(f"**Shortest Sentence(s) (in words)**: {', '.join(result.get('shortest_sentences', []))}")
            st.write(f"**Average Sentence Length (in words)**: {result.get('avg_sentence_length', 'N/A'):.2f}")
        else:
            st.write("Please enter some text to analyze.")

# Function to call AWS Lambda function for text analysis
def analyze_text(text):
    try:
        # Send a POST request to the AWS Lambda function with the text
        response = requests.post(LAMBDA_URL, json={"text": text})

        # Parse the response JSON
        return response.json()
    except Exception as e:
        return {"error": str(e)}
