import replicate
import os
from dotenv import load_dotenv

load_dotenv()


def generate_abstract_ref(params):
    """
    Генерирует абстрактное изображение на основе успешных параметров через Flux.
    """
    # Маппинг данных в художественные промпты
    bg_style = "bright high-key lighting, airy atmosphere" if params[
                                                                  'background'] == 'light' else "moody cinematic shadows, dark aesthetic"
    motion_style = "kinetic energy, fluid motion blur, fast movement" if params[
                                                                             'dynamics'] == 'dynamic' else "minimalist geometric stability, static balance"
    color_style = "vibrant saturated neon colors" if params['color'] == 'bright' else "muted sophisticated pastel tones"

    prompt = (f"Abstract digital composition, {bg_style}, {motion_style}, {color_style}, "
              f"graphic design style, high contrast, sharp details, 8k resolution, "
              f"trending on behance, professional studio lighting --ar 9:16")

    try:
        # Используем быструю модель Flux Schnell
        output = replicate.run(
            "black-forest-labs/flux-schnell",
            input={
                "prompt": prompt,
                "aspect_ratio": "9:16",
                "output_format": "webp"
            }
        )

        # Безопасное извлечение URL
        if isinstance(output, list) and len(output) > 0:
            return str(output[0])
        return str(output)

    except Exception as e:
        return f"Error during generation: {e}"