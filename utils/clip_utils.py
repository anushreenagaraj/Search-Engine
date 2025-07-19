# utils/clip_utils.py

from sentence_transformers import SentenceTransformer, util
from PIL import Image
import torch

# Load CLIP model
clip_model = SentenceTransformer("clip-ViT-B-32")

# Predefined tags (optional)
clip_tags = [
    "sunset", "mountain", "ocean", "forest", "city", "lonely", "peaceful", "angry", 
    "joyful", "storm", "desert", "garden", "night", "fire", "happy", "sad", "rain"
]

def encode_image(image_path):
    image = Image.open(image_path).convert("RGB")
    return clip_model.encode(image, convert_to_tensor=True)

def encode_text(text):
    return clip_model.encode(text, convert_to_tensor=True)

def get_clip_tags(image_path, top_k=2):
    image_emb = encode_image(image_path)
    tag_embs = clip_model.encode(clip_tags, convert_to_tensor=True)
    similarities = util.cos_sim(image_emb, tag_embs)[0]
    top_indices = torch.topk(similarities, k=top_k).indices.tolist()
    return [clip_tags[i] for i in top_indices]
