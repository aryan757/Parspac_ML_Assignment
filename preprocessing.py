import re

# # Function to preprocess the text
# def preprocess_text(text):
#     text = text.lower()  # Convert to lowercase
#     text = re.sub(r'\d+', '', text)  # Remove numbers
#     text = re.sub(r'\W+', ' ', text)  # Remove special characters
#     return text

class Preprocessor:
    def preprocess_text(self, text):
        text = text.lower()  # Convert to lowercase
        text = re.sub(r'\d+', '', text)  # Remove numbers
        text = re.sub(r'\W+', ' ', text)  # Remove special characters
        return text