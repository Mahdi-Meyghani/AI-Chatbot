import json
import requests


class ChatBot:
    def __init__(self):
        self.headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
                             ".eyJ1c2VyX2lkIjoiNWI5MWU3ZjgtNGY0MC00MGFhLWF"
                             "mNGQtNWIzODVmMzI2YjUzIiwidHlwZSI6ImFwaV90b2tl"
                             "biJ9.o4DVt_po0DxyRYcjvNtQNHp6PZn3tfvQPHSTlY1xLAU"
        }
        self.url = "https://api.edenai.run/v2/text/generation"

    def get_response(self, text):
        payload = {
            "providers": "openai,cohere",
            "text": f"{text}",
            "temperature": 0.5,
            "max_tokens": 1000,
        }
        result = requests.post(self.url, json=payload, headers=self.headers)
        json_result = json.loads(result.text)
        response = json_result['openai']['generated_text']

        return response


if __name__ == "__main__":
    bot = ChatBot()
    answer = bot.get_response("Tell a joke about birds.")
    print(answer)
