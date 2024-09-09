import requests
import streamlit as st
from PIL import Image, UnidentifiedImageError
import io

# Hugging Face API URL and headers
API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
headers = {"Authorization": "Bearer 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"}

# Function to query the Hugging Face API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Streamlit app
st.title("Stable Diffusion Image Generator")
st.write("Enter a prompt to generate an image:")

# Text input for the prompt
prompt = st.text_input("Prompt", "Astronaut riding a horse")

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        image_bytes = query({"inputs": prompt})
        
        # Attempt to open the image
        try:
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image, caption=prompt)
        except UnidentifiedImageError:
            st.error("The response from the API was not a valid image. Please try again.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
