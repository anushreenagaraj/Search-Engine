# utils/face_emotion.py

from deepface import DeepFace

def detect_emotion_from_face(image_path):
    try:
        result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)
        return result[0]['dominant_emotion']  # e.g., 'happy', 'sad', etc.
    except Exception as e:
        print(f"[DeepFace] Error: {e}")
        return None
