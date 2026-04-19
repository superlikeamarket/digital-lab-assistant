import streamlit as st
import cv2
import numpy as np
from PIL import Image

from ultralytics import YOLO

from "colony-counter".src.app.preprocessing import preprocess_for_model
from src.ml.inference import run_inference_on_image, draw_predictions
import yaml


# =========================
# LOAD MODEL (cached)
# =========================

@st.cache_resource
def load_model():
    with open("configs/inference.yaml") as f:
        config = yaml.safe_load(f)

    model = YOLO(config["model"])
    return model, config


# =========================
# UI
# =========================
def run():
    st.title("🧫 Colony Counter")

    st.write("Upload a Petri dish image to count bacterial colonies.")

    uploaded_file = st.file_uploader(
        "Upload image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image_np = np.array(image)

        st.image(image, caption="Original Image", use_container_width=True)

        model, config = load_model()

        # =========================
        # PREPROCESS
        # =========================
        processed, info = preprocess_for_model(image_np)

        if processed is None:
            st.error(info["error"])
        else:
            st.image(processed, caption="Preprocessed (cropped + masked)")

            # =========================
            # INFERENCE
            # =========================
            count, boxes, vis_img = run_inference_on_image(
                model,
                processed,
                config
            )

            vis = draw_predictions(vis_img, boxes, count)

            st.image(vis, caption="Prediction")

            st.success(f"Detected colonies: {count}")

            # TNTC logic
            TNTC_THRESHOLD = 300
            if count >= TNTC_THRESHOLD:
                st.warning("TNTC (Too Numerous To Count)")



conf = st.slider("Confidence", 0.0, 1.0, 0.25)

iou = st.slider("IoU", 0.0, 1.0, 0.5)