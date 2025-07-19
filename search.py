import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json
from utils.clip_utils import encode_text

# Load all data
image_embeddings = np.load("data/embeddings.npy", allow_pickle=True)
with open("data/metadata.json") as f:
    metadata = json.load(f)

def search_images(query, top_k=5):
    # Convert query to CLIP text embedding
    query_emb = encode_text(query).reshape(1, -1)

    # Compute cosine similarity
    similarities = cosine_similarity(query_emb, image_embeddings)[0]
    top_indices = similarities.argsort()[::-1][:top_k]

    # Return top matching image filenames
    return [metadata[i]["filename"] for i in top_indices]
