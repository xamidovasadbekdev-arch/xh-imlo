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
O'zbek tilida "{word}" so'zining to'g'ri va noto'g'ri yozilishini ber.
Faqat X va H harflari bilan bog'liq imlo xatolari haqida.
Masalan: "halovat" to'g'ri, "xalovat" noto'g'ri.

FAQAT JSON formatda qaytar, boshqa hech narsa yozma:
{{
    "correct": "to'g'ri yozilishi",
    "incorrects": ["noto'g'ri variant 1", "noto'g'ri variant 2"]
}}

Agar X yoki H bilan bog'liq imlo muammosi bo'lmasa:
{{
    "correct": null,
    "incorrects": []
}}
            """
        }]
    )

    try:
        result = json.loads(response.choices[0].message.content)
        return result
    except json.JSONDecodeError:
        return None

