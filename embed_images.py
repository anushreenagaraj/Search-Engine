import os
import numpy as np
import json
from PIL import Image
from tqdm import tqdm

from utils.clip_utils import encode_image

image_folder = "data/images"
output_embedding_file = "data/embeddings.npy"
output_metadata_file = "data/metadata.json"

embeddings = []
metadata = []

# Process all images in the folder
for filename in tqdm(os.listdir(image_folder)):
    path = os.path.join(image_folder, filename)
    try:
        image = Image.open(path).convert("RGB")
        emb = encode_image(image)
        embeddings.append(emb.cpu().numpy())
        metadata.append({"filename": filename})
    except Exception as e:
        print(f"Failed to process {filename}: {e}")

# Save embeddings and metadata
np.save(output_embedding_file, embeddings)
with open(output_metadata_file, "w") as f:
    json.dump(metadata, f)

print("✅ Embeddings saved!")
