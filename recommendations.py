def generate_design_brief(top_params):
    """
    Формирует подробное текстовое ТЗ на основе переданных параметров.
    """
    style = str(top_params['style']).upper()
    bg = "светлых (light)" if top_params['background'] == 'light' else "темных (dark)"
    dynamics = "активную динамику, движение и монтаж" if top_params[
                                                             'dynamics'] == 'dynamic' else "статичную и спокойную композицию"
    colors = "яркие и насыщенные" if top_params['color'] == 'bright' else "приглушенные и мягкие"

    brief = f"""### 📝 Детальное ТЗ для дизайна

**1. Общая концепция:**
Необходимо создать серию креативов в стилистике **{style}**. Текущий ROI связки: {top_params['ROI']:.2f}.

**2. Визуальные инструкции:**
* **Цветовая палитра:** Используйте {colors} тона. 
* **Фон:** Придерживайтесь {bg} фонов.
* **Работа с движением:** Внедрите {dynamics}.

**3. Технические требования:**
* Формат: 9:16.
* Лицо: {'Обязательно наличие лица' if top_params.get('face') == 'yes' else 'Можно без лиц'}.

**4. Зачем это нужно:**
Эта комбинация параметров является наиболее эффективной по результатам последних тестов.
"""
    return brief


def create_rtf_brief(text):
    """
    Создает простейший RTF файл для Word.
    """
    clean_text = text.replace("### ", "").replace("**", "").replace("* ", "- ")
    rtf_header = r"{\rtf1\ansi\deff0 {\fonttbl {\f0 Arial;}} \f0\fs24 "
    rtf_footer = r"}"
    rtf_body = clean_text.replace("\n", "\\par ")
    return rtf_header + rtf_body + rtf_footer