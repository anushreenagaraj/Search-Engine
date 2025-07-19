# utils/ocr_sentiment.py

from PIL import Image, ImageEnhance, ImageFilter
from transformers import pipeline
import pytesseract

# Set path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"

# Load sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

def detect_sentiment_from_text(image_path):
    # Load and preprocess image
    image = Image.open(image_path).convert("L")
    image = image.filter(ImageFilter.SHARPEN)
    image = ImageEnhance.Contrast(image).enhance(3)
    image = image.resize((image.width * 2, image.height * 2))

    # Run OCR
    extracted_text = pytesseract.image_to_string(image, lang='eng').strip()

    # Skip if empty
    if not extracted_text:
        return "neutral", 0.0, ""

    # Run sentiment analysis
    result = sentiment_analyzer(extracted_text)[0]
    label = result["label"].lower()  # 'positive', 'negative'
    score = result["score"]

    return label, score, extracted_text
