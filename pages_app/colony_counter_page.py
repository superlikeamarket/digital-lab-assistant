import streamlit as st
import cv2
from pathlib import Path
import numpy as np
from PIL import Image
import yaml

from ultralytics import YOLO
from src.app.predictor import predict_colonies


@st.cache_resource
def load_model_and_config():
    config_path = Path("assets/configs/colony_counter_inference.yaml")

    if not config_path.exists():
        raise FileNotFoundError(f"Missing config file: {config_path}")

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    model_path = Path(config["model"])
    if not model_path.exists():
        raise FileNotFoundError(f"Missing model file: {model_path}")

    model = YOLO(str(model_path))
    return model, config


def run():
    st.title("🧫 Colony Counter")
    st.write("Upload a Petri dish image to count bacterial colonies.")

    model, base_config = load_model_and_config()

    conf = st.slider("Confidence", 0.0, 1.0, float(base_config.get("conf", 0.25)), 0.01)
    iou = st.slider("IoU", 0.0, 1.0, float(base_config.get("iou", 0.5)), 0.01)

    uploaded_file = st.file_uploader(
        "Upload image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        image_np = np.array(image)

        st.image(image_np, caption="Original image", use_container_width=True)

        config = dict(base_config)
        config["conf"] = conf
        config["iou"] = iou

        result = predict_colonies(
            image=image_np,
            model=model,
            config=config,
        )

        if not result["success"]:
            st.error(result["error"])
            return

        processed_rgb = cv2.cvtColor(result["processed_image"], cv2.COLOR_BGR2RGB)
        vis_rgb = cv2.cvtColor(result["visualization"], cv2.COLOR_BGR2RGB)

        st.image(processed_rgb, caption="Preprocessed (cropped + masked)", use_container_width=True)
        st.image(vis_rgb, caption="Prediction", use_container_width=True)

        st.success(f"Detected colonies: {result['pred_count']}")

        if result["is_tntc"]:
            st.warning(f"TNTC (>{config.get('tntc_threshold', 300)})")
        else:
            st.info("Countable plate")