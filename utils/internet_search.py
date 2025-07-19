# utils/internet_search.py
import requests
import os

def bing_image_search(query, count=10, api_key="YOUR_KEY"):
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    params = {"q": query, "count": count, "imageType": "Photo"}
    url = "https://api.bing.microsoft.com/v7.0/images/search"
    response = requests.get(url, headers=headers, params=params)
    results = response.json()["value"]
    
    os.makedirs("internet_images", exist_ok=True)
    paths = []

    for i, item in enumerate(results):
        img_url = item["contentUrl"]
        try:
            img_data = requests.get(img_url, timeout=5).content
            file_path = f"internet_images/{query.replace(' ', '_')}_{i}.jpg"
            with open(file_path, "wb") as f:
                f.write(img_data)
            paths.append(file_path)
        except:
            continue
    return paths
