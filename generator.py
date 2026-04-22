import replicate
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


def generate_abstract_ref(params):
    api_token = os.getenv("REPLICATE_API_TOKEN") or st.secrets.get("REPLICATE_API_TOKEN")

    if not api_token:
        return "Error: API Token не найден."

    roi = params['ROI']
    # Проверка на аномалию (темный фон + нет лица + высокий ROI)
    is_anomaly = roi > 3.0 and params['background'] == 'dark' and params['face'] == 'no'

    if is_anomaly:
        prompt = (f"Cinematic close-up of a mystical animal with glowing neon eyes, "
                  f"emerging from deep pitch-black shadows, vibrant electric purple accents, "
                  f"high contrast, futuristic dark aesthetic, 8k, sharp details --ar 9:16")
    else:
        bg_style = "bright high-key lighting" if params['background'] == 'light' else "dark shadows"
        prompt = f"Abstract digital art, {bg_style}, vibrant colors, graphic design style --ar 9:16"

    try:
        client = replicate.Client(api_token=api_token)
        output = client.run(
            "black-forest-labs/flux-schnell",
            input={"prompt": prompt, "aspect_ratio": "9:16"}
        )
        return str(output[0])
    except Exception as e:
        return f"Error: {e}"