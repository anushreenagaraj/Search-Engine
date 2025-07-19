# utils/mood_logic.py

def infer_overall_mood(face_emotion, text_sentiment, clip_tags, art_emotion=None):
    moods = [face_emotion, text_sentiment, art_emotion] + clip_tags
    moods = [m for m in moods if m]  # Remove None values
    if not moods:
        return "neutral"
    return max(set(moods), key=moods.count)
