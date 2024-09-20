import pathlib
import textwrap
import os
import base64
import streamlit as st
from PIL import Image
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


genai.configure(api_key=api_key)


# Input prompt and image upload
def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text


##initialize our streamlit app
st.set_page_config(page_title="Diabetes Nutrition Plan")

st.header("Nutritionist Application")

uploaded_file = st.file_uploader("Upload an image of a food or meal to know more about it!", type=["jpg", "jpeg", "png"])
input = "Write a short detailed description about the food in the image. It should include whether it is healthy to eat if you have diabetes. Suggest alternative healthier meals"
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
submit=st.button("Submit")

## If ask button is clicked

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)