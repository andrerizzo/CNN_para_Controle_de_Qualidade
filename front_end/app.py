import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# --- Configurações da página ---
st.set_page_config(page_title="Classificador de Tomates", layout="centered")
st.title("🍅 Classificador de Qualidade de Tomates")
st.write("Modelo baseado em CNN + VGG16 (Transfer Learning)")

# --- Parâmetros ---
IMAGE_SIZE = (224, 224)
CLASS_NAMES = ['Danificado', 'Maduro', 'Velho', 'Verde']
MODEL_PATH = 'model/modelo_final.h5'

# --- Função de preprocessamento ---
def preprocess_image(image):
    img = image.resize(IMAGE_SIZE)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# --- Carregar modelo ---
@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

# --- Upload da imagem ---
uploaded_file = st.file_uploader("Envie uma imagem de tomate", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Imagem enviada", use_column_width=True)

    # Preprocessar e prever
    input_image = preprocess_image(image)
    prediction = model.predict(input_image)
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = 100 * np.max(prediction)

    # Resultado
    st.markdown("---")
    st.subheader(f"🧠 Predição: **{predicted_class}**")
    st.write(f"Confiabilidade: `{confidence:.2f}%`")
