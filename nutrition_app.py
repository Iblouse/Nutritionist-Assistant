from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load all environment variables
load_dotenv()

# Configure generative AI with the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_prompt, image):
    """
    Generates a response from the Gemini AI model based on the input prompt and image data.

    Args:
        input_prompt (str): The text prompt to provide context or instructions to the model.
        image (list): A list containing a dictionary with image data and its MIME type.

    Returns:
        str: The text response generated by the model.
    """
    response = model.generate_content([input_prompt, image[0]])
    return response.text

def input_image_details(uploaded_file):
    """
    Processes the uploaded image file and extracts its details.

    Args:
        uploaded_file (UploadedFile): The uploaded image file from the user.

    Returns:
        list: A list containing a dictionary with the image's MIME type and binary data.
    
    Raises:
        FileNotFoundError: If no file is uploaded.
    """
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the MIME type of the uploaded file
                "data": bytes_data  # Image data in binary format
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize the Streamlit app
st.set_page_config(page_title="Diet Advisor App")

# Set the header for the app
st.header("Diet Advisor App")

# File uploader for the user to upload their food image
uploaded_file = st.file_uploader("Upload your food image", type=["jpg", "jpeg", "png", "WebP"])
image = ""

# Display the uploaded image if available
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Button for the user to submit and get food analysis
submit = st.button("Give me advice about this food")

# Input prompt for the generative model
input_prompt = """
You are an expert nutritionist. Analyze the food items in the image and calculate the total calories, 
providing details for each item in the following format:

1. Item 1 - no of calories
2. Item 2 - no of calories 
- - - -
- - - -

Mention the percentage split of carbohydrates, fats, fibers, sugar, and nutrients required for a healthy diet.
Indicate whether the food is healthy or not, and if not, suggest how to make it healthier. Mention ingredients to 
remove or reduce and what ingredients could replace them.
"""

# If the submit button is clicked, process the image and generate the response
if submit:
    # Extract image details from the uploaded file
    image_data = input_image_details(uploaded_file)
    # Get the AI model's response using the input prompt and image data
    response = get_gemini_response(input_prompt, image_data)
    # Display the response in the Streamlit app
    st.subheader("The Response is")
    st.write(response)