import os
import openai

client = openai.OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key="csk-tr33y8n58m4xh4h55yfdpckryddevjktxw4e5jw4m4w66536"
)

output = client.completions(prompt = "What is the meaning of life?", max_tokens = 1)
print

class spawn():
    def __init__(self, name, age, backstory):
        self.name = name
        self.age = age
        self.backstory = backstory
        api 