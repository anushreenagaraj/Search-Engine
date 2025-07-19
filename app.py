import streamlit as st
from PIL import Image
from upload_search import analyze_uploaded_image
from search import search_images

st.set_page_config(page_title="Mood & Emotion Image Search", layout="wide")
st.title("🎨 Mood, Emotion & Sentiment-based Image Search Engine")

mode = st.radio("Choose search mode:", ["Upload Image", "Text Search"])

# 📤 Upload mode
if mode == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        
        mood, description = analyze_uploaded_image(uploaded_file)
        
        st.markdown(f"**Inferred Mood:** `{mood}`")
        st.markdown(f"**Scene Tags:** `{description}`")

        st.markdown("### 🔍 Searching for similar images...")
        results = search_images(mood + " " + description, top_k=5)

        for r in results:
            st.image(f"data/images/{r}", caption=r)

# 🔤 Text mode
else:
    query = st.text_input("Enter mood/scene/emotion description:")
    
    if query:
        st.markdown("### 🔍 Top Matching Images:")
        results = search_images(query, top_k=5)

        for r in results:
            st.image(f"data/images/{r}", caption=r)
