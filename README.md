# 🎨 Emotion-Based Image Search Engine

This is an AI-powered image search engine that retrieves visually and emotionally similar images based on the **emotion**, **mood**, or **sentiment** detected in an uploaded image or user query.

---

## 🔍 Key Features

- **Upload an Image:** Detects **facial emotions**, **scene context**, and **text sentiment** using:
  - DeepFace (emotion from face)
  - CLIP (scene/object understanding)
  - OCR + Transformers (text sentiment)
- **Text Search:** Search by natural language like _"happy beach sunset"_ or _"angry office meeting"_.
- **Search from Internet (Optional):** Perform Bing image search for emotion-matched images (if enabled).
- **CLIP Embedding Matching:** Uses cosine similarity on CLIP embeddings to retrieve the most relevant images.

---

## 🧠 Tech Stack

| Component        | Purpose                                           |
|------------------|---------------------------------------------------|
| **Streamlit**     | Frontend for UI interaction                      |
| **CLIP**          | For embedding text/image & finding similarity    |
| **DeepFace**      | Detect facial emotion in uploaded images         |
| **OCR (Tesseract)** | Extract text from image and analyze sentiment |
| **Transformers**  | Sentiment analysis of extracted text             |
| **ArtEmis (Optional)** | Emotion understanding for artworks         |

---

## 📁 Project Structure

```bash
📂 data/
    ├── images/             # Image dataset (local)
    ├── embeddings.npy      # Precomputed CLIP embeddings
    └── metadata.json       # Metadata (filename, labels, etc.)
📂 search/
📂 utils/
📄 app.py                   # Streamlit main app
📄 upload_search.py         # Handles image analysis
📄 search.py                # Handles search logic
📄 .gitignore
📄 requirements.txt
