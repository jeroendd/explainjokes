import streamlit as st
import openai
import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Title of the application
st.title("Joke Explainer")

# Input text box for joke submission
joke = st.text_area("Enter your joke here:")

# Submit button
if st.button("Submit"):
    if joke:
        # Call OpenAI's GPT-4 model for explanation
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user", 
                    "content":  f"Explain the joke: {joke}",
                }
            ],
            model="gpt-4o-mini",
        )
       
        explanation = response.choices[0].message.content
        # Display the explanation
        st.subheader("Explanation")
        st.write(explanation)
    else:
        st.error("Please enter a joke before submitting.")