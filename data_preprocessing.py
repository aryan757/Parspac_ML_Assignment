#This is the script for data pre-processing.abs
import requests
import fitz  # PyMuPDF
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to extract text from PDF URL
def extract_text_from_pdf_url(url):
    try:
        response = requests.get(url, timeout=10)  # Set a timeout for the request
        response.raise_for_status()
        doc = fitz.open(stream=response.content, filetype="pdf")
        text = ""
        for page in doc:
            print("extracting text")
            text += page.get_text()
        return text
    except Exception as e:
        logging.error(f"Error processing {url}: {e}")
        return None


# Function to preprocess the text
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'\W+', ' ', text)  # Remove special characters
    return text

# Load the CSV file
file_path = '/content/pre_processed_testing_data.csv'
df = pd.read_csv(file_path)

# Counter to track the number of successfully processed PDFs
processed_count = 0

# Extract and preprocess text for all PDF URLs in the dataset
def extract_and_preprocess(url):
    global processed_count
    text = extract_text_from_pdf_url(url)
    if text:
        processed_count += 1
        print(f"Successfully processed PDF count: {processed_count}")
        return preprocess_text(text)
    return None

# Apply the extraction and preprocessing function to the dataframe
df['preprocessed_text'] = df['datasheet_link'].apply(extract_and_preprocess)
df = df.dropna(subset=['preprocessed_text'])  # Drop rows where text extraction failed

