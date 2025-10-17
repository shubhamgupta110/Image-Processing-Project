# app.py
import streamlit as st
from PIL import Image, ImageEnhance, ImageOps
import numpy as np

st.set_page_config(page_title="Image Processing App", page_icon="🖼️", layout="centered")
st.title("🖼️ Image Processing Web App")

# Image Upload
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Original Image', use_column_width=True)

    st.markdown("---")
    st.subheader("Choose Filter")
    filter_option = st.selectbox("Select a filter to apply:", 
                                 ["Brightness", "Contrast", "Inversion", "Grayscale"])

    # Brightness and Contrast sliders
    if filter_option in ["Brightness", "Contrast"]:
        level = st.slider(f"Select {filter_option} level", 0.0, 3.0, 1.0)

    # Apply filter
    if st.button("Apply Filter"):
        if filter_option == "Brightness":
            enhancer = ImageEnhance.Brightness(image)
            processed_image = enhancer.enhance(level)

        elif filter_option == "Contrast":
            enhancer = ImageEnhance.Contrast(image)
            processed_image = enhancer.enhance(level)

        elif filter_option == "Inversion":
            processed_image = ImageOps.invert(image.convert("RGB"))

        elif filter_option == "Grayscale":
            processed_image = ImageOps.grayscale(image)

        st.image(processed_image, caption=f'{filter_option} Applied', use_column_width=True)
