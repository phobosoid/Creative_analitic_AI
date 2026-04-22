import openai
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


def generate_design_brief(top_params):
    """
    Генерирует уникальное ТЗ, используя OpenAI GPT-4o.
    """
    api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")

    if not api_key:
        return "⚠️ Ошибка: Добавьте OPENAI_API_KEY в .env или Secrets."

    client = openai.OpenAI(api_key=api_key)

    # Контекст из данных
    context = (
        f"Стиль: {top_params['style']}, ROI: {top_params['ROI']:.2f}, "
        f"Фон: {top_params['background']}, Динамика: {top_params['dynamics']}, "
        f"Цвета: {top_params['color']}, Лицо: {top_params.get('face', 'no')}."
    )

    prompt = f"""
    Ты — ведущий креативный стратег в performance-маркетинге. 
    Твоя задача: на основе данных аналитики написать детальное и вдохновляющее ТЗ для дизайнера.

    Данные лучшей связки: {context}

    В ТЗ обязательно должно быть:
    1. ГИПОТЕЗА: Почему именно эти параметры (например, {top_params['background']} фон) дали такой ROI?
    2. ВИЗУАЛЬНЫЙ КОНЦЕПТ: Опиши композицию. Если ROI > 3.0 и лицо=no, предложи использовать необычного персонажа (животное, робот, маскот).
    3. ТЕХНИЧЕСКИЕ ДЕТАЛИ: Освещение, шрифты, акценты.
    4. ПРИЗЫВ К ДЕЙСТВИЮ: Как выделить оффер.

    Пиши профессионально, структурированно, в стиле Jira/Notion. Используй Markdown.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Ты эксперт по генерации рекламных стратегий."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ошибка AI-генерации: {e}"


def create_rtf_brief(text):
    # Упрощенная конвертация для RTF
    clean_text = text.replace("#", "").replace("*", "").replace("`", "")
    rtf_header = r"{\rtf1\ansi\deff0 {\fonttbl {\f0 Arial;}} \f0\fs24 "
    rtf_footer = r"}"
    rtf_body = clean_text.replace("\n", "\\par ")
    return rtf_header + rtf_body + rtf_footer