import json
from groq import Groq
from django.conf import settings


def get_word_variants(word):
    client = Groq(api_key=settings.GROQ_API_KEY)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=200,
        messages=[{
            "role": "user",
            "content": f"""
Sen o'zbek tili imlo mutaxassisisan.
"{word}" so'zining X va H harflari bilan bog'liq 
to'g'ri imlosini O'zbek tilining rasmiy imlo qoidalari 
asosida aniqla.

Masalan:
- "halovat" TO'G'RI, "xalovat" NOTO'G'RI
- "xurmo" TO'G'RI, "hurmo" NOTO'G'RI  
- "xizmat" TO'G'RI, "hizmat" NOTO'G'RI

FAQAT JSON formatda qaytar:
{{
    "correct": "to'g'ri yozilishi",
    "incorrects": ["noto'g'ri variant 1"]
}}
"""
        }]
    )

    try:
        result = json.loads(response.choices[0].message.content)
        return result
    except json.JSONDecodeError:
        return None
