import streamlit as st
from PIL import Image, ImageDraw
from utils import inference
from utils.inference import predict_image

st.set_page_config(page_title="DeepFake Detector", layout="centered")

st.title("🕵️ DeepFake Detection App")
st.write("Upload an image to check if it's Real or Fake.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Analyzing..."):
        label, confidence = predict_image(image)

    st.success(f"Prediction: **{label}**")
    st.info(f"Confidence Score: **{confidence:.2f}**")

    # Simple visualization: draw a red border
    draw = ImageDraw.Draw(image)
    draw.rectangle([0, 0, image.width, image.height], outline="red", width=5)
    st.image(image, caption="Detection Visualization", use_column_width=True)
