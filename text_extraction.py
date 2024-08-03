import requests
import fitz  # PyMuPDF
import logging

# # Set up logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def extract_text_from_pdf_url(url):
#     try:
#         response = requests.get(url, timeout=10)  # Set a timeout for the request
#         response.raise_for_status()
#         doc = fitz.open(stream=response.content, filetype="pdf")
#         text = ""
#         for page in doc:
#             text += page.get_text()
#         return text
#     except Exception as e:
#         logging.error(f"Error processing {url}: {e}")
#         return None

class TextExtractor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def extract_text_from_pdf_url(self, url):
        try:
            response = requests.get(url, timeout=10)  # Set a timeout for the request
            response.raise_for_status()
            doc = fitz.open(stream=response.content, filetype="pdf")
            text = ""
            for page in doc:
                text += page.get_text()
            return text
        except Exception as e:
            self.logger.error(f"Error processing {url}: {e}")
            return None