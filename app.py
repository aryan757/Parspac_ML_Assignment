import streamlit as st
from text_extraction import TextExtractor
from preprocessing import Preprocessor
from model_training import ModelTrainer
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='logfile.log')

# Path to the training data CSV
TRAINING_DATA_PATH = 'pre_processed_data.csv'

# Initialize components
text_extractor = TextExtractor()
preprocessor = Preprocessor()
model_trainer = ModelTrainer(TRAINING_DATA_PATH)

# Train the model and save it
@st.cache_resource
def load_model():
    model_trainer.train_model()
    return model_trainer.get_pipeline()

model_pipeline = load_model()

st.title("PARSPEC Product Classification System")

st.write("""
    ### Description
    This app will take any PDF link and provide a detailed classification by understanding the extracted text.
    It classifies the content into the following product categories: **Lighting**, **Fuses**, **Cables**, **Others**.
""")

pdf_url = st.text_input("Enter PDF URL:")

if pdf_url:
    text = text_extractor.extract_text_from_pdf_url(pdf_url)
    if text:
        preprocessed_text = preprocessor.preprocess_text(text)
        prediction = model_pipeline.predict([preprocessed_text])
        prediction_prob = model_pipeline.predict_proba([preprocessed_text])

        st.write(f"### Predicted Label: {prediction[0]}")
        st.write("### Class Probabilities:")
        for idx, prob in enumerate(prediction_prob[0]):
            st.write(f"Class {idx}: {prob:.4f}")
    else:
        st.write("Failed to process PDF URL.")

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: right;
        padding: 10px;
        font-size: 12px;
        color: #888;
    }
    </style>
    <div class="footer">
        Developed by: Aryan Agrahari
    </div>
    """,
    unsafe_allow_html=True
)
