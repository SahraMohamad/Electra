import openai
from openai import OpenAI

client = openai.OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key=""
)

class NPC():
    def __init__(self, identity: str):
        self.backstory = self.generate_backstory(identity)

    def generate_backstory(self, identity: str):
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": '''Create a human-like backstory emphasizing realism with fully fleshed out details, 
                    character and personality traits, based on the provided characteristics:''',
                },
                {
                    "role": "user",
                    "content": identity,
                }
            ],
            model="llama3.1-70b",
            stream=False,
        )
        return (response.choices[0].message.content)

def generate_identities(number: int):
    identities = []
    return identities

def spawn(number: int):
    identities = generate_identities(number)
    npcs = [NPC(identity) for identity in identities]
    return npcs


