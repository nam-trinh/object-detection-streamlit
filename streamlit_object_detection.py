import streamlit as st
from PIL import Image
import requests

# Upload an image and set some options for demo purposes
st.header("Object Detection Demo using DETR from Facebook AI Research")
image_file = st.sidebar.file_uploader(label='Upload a file', type=['png', 'jpg', 'jpeg'])

if image_file:
    headers = {"accept": "application/json"}
    bytes_image = image_file.getvalue()
    files = {'data': (image_file.name, bytes_image, 'image/jpeg')}
    link_to_api = 'http://127.0.0.1:5000/detect_object/'
    response = requests.post(url=link_to_api, headers=headers, files=files)
    
    st.image(Image.open(image_file))      
    st.write(response.content)
