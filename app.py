import streamlit as st
import openai
import os

# Set up OpenAI API credentials
openai.api_key = os.environ["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"]

# Set up Streamlit app
st.title("AI Assistant")

# Define function for querying OpenAI API
def query_ai(query):
    response = openai.Completion.create(
        engine="davinci",
        prompt=query,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text

# Add text input box for user to ask a question
question = st.text_input("Ask me anything")

# If the user has entered a question, query the AI and display the answer
if question:
    answer = query_ai(question)
    st.write(answer)
