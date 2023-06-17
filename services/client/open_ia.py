import openai
from settings import OPENAI_API_KEY


class OpenAIClient:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    def question(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response
