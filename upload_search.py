import os
import tempfile
from PIL import Image

from utils.face_emotion import detect_emotion_from_face
from utils.ocr_sentiment import detect_sentiment_from_text
from utils.clip_utils import encode_image, get_clip_tags
from utils.mood_logic import infer_overall_mood

def analyze_uploaded_image(uploaded_file):
    """
    Full pipeline to analyze an uploaded image.
    Returns: (final_mood, image_description)
    """

    # Save uploaded image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_path = tmp_file.name
        tmp_file.write(uploaded_file.read())

    # 1. DeepFace: facial emotion
    try:
        face_emotion = detect_emotion_from_face(tmp_path)
    except Exception as e:
        print(f"[DeepFace] Error: {e}")
        face_emotion = None

    # 2. OCR + Sentiment
    try:
        text_sentiment, _, extracted_text = detect_sentiment_from_text(tmp_path)
    except Exception as e:
        print(f"[OCR] Error: {e}")
        text_sentiment = None
        extracted_text = ""

    # 3. CLIP tags
    try:
        image = Image.open(tmp_path).convert("RGB")
        clip_tags = get_clip_tags(image, top_k=2)
        image_description = ", ".join(clip_tags)
    except Exception as e:
        print(f"[CLIP] Error: {e}")
        clip_tags = []
        image_description = "Unknown scene"

    # 4. Final hybrid mood
    final_mood = infer_overall_mood(
        face_emotion=face_emotion,
        text_sentiment=text_sentiment,
        clip_tags=clip_tags,
        art_emotion=None
    )

    # Cleanup
    os.remove(tmp_path)

    return final_mood, image_description
