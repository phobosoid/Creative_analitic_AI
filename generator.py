import replicate
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


def generate_abstract_ref(params):
    api_token = os.getenv("REPLICATE_API_TOKEN") or st.secrets.get("REPLICATE_API_TOKEN")

    if not api_token:
        return "Error: API Token не найден."

    # Если ROI аномальный и нет лица - генерим животное/маскота
    if params['ROI'] > 3.0 and params['face'] == 'no':
        subject = "cybernetic glowing animal, futuristic mascot"
    else:
        subject = "abstract geometric composition"

    bg = "dark cinematic atmosphere" if params['background'] == 'dark' else "bright minimalist gallery lighting"

    prompt = (f"{subject}, {bg}, {params['color']} palette, {params['dynamics']} movement, "
              f"high-end graphic design, trendy 3D render, sharp focus, 8k --ar 9:16")

    try:
        client = replicate.Client(api_token=api_token)
        output = client.run(
            "black-forest-labs/flux-schnell",
            input={"prompt": prompt, "aspect_ratio": "9:16"}
        )
        return str(output[0])
    except Exception as e:
        return f"Error: {e}"