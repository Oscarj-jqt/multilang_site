import openai
from django.conf import settings

def get_chat_response(prompt):

    openai.api_key = settings.OPENAI_API_KEY

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user",
            "content": prompt}
        ],
        prompt = prompt,
        max_token = 150,
        temperature = 0.7,
        n = 1
    )

    print(response)

    return response.choices[0].message['content'].strip()