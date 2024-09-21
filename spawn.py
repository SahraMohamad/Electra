import random
import openai
from openai import OpenAI

client = openai.OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key=""
)

class NPC:
    def __init__(self, identity: str):
        self.backstory = self.generate_backstory(identity)
        self.memory = []

    def generate_backstory(self, identity: str):
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": '''Develop a deeply realistic, human-like backstory that equally explores both 
                    the strengths and flaws of the character. Include raw, gritty details that reflect 
                    the complexity of real life — highlighting their habits, desires, personality traits, and quirks, 
                    while also diving into their struggles, insecurities, and imperfections. Focus on 
                    the challenges they've faced, the consequences of their actions, and the darker 
                    aspects of their life experiences. The backstory should feel fully fleshed out 
                    and grounded in hard-hitting realism, based on the provided characteristics. Don't shy away from adult themes.''',
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
    
    def talk(self, message: str):
        user_message = {"role": "user", "content": message}
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f'''You are now stepping into the role of a character with a deeply 
                    ingrained background that has shaped the way they think, speak, and make decisions. 
                    Every response should reflect their personal history, experiences, struggles, and values. 
                    Here's what to consider: Speech Patterns: Adapt your tone, vocabulary, and speech style to 
                    align with the character’s background. If they’ve had a rough upbringing, reflect that with 
                    a blunt, no-nonsense style. If they’re well-educated or from a privileged class, weave in 
                    sophistication and insight. Thought Process: Respond as if you are truly living through this 
                    character's worldview. Their past—whether filled with hardship, privilege, trauma, or success 
                    should influence how they approach problems, what they fear, and what drives them. Every thought 
                    should reflect the biases, values, and learned behaviors from their experiences. Personality and 
                    Flaws: Make sure to express their unique personality traits, quirks, and imperfections. If they’re 
                    jaded from past failures, reflect cynicism. If they’ve been betrayed, they may struggle with trust. 
                    Every choice, action, and word should be filtered through their life story. This is their story: 
                    {self.backstory} and this is their memory: {self.memory}''',
                },
                user_message
            ],
            model="llama3.1-70b",
            stream=False,
        )
        npc_reply = response.choices[0].message.content
        self.memory.append({"role": "assistant", "content": npc_reply})
        return npc_reply

def group_chat(npcs, goal, chat_type, conversation_log=[]):
    if goal and not conversation_log:
        conversation_log.append({"role": "npc", "content": goal})
        print(f"Initial Goal: {goal}")

    if chat_type == "round_robin":
        for i, npc in enumerate(npcs):
            last_message = conversation_log[-1]["content"]
            npc_response = npc.talk(last_message)
            conversation_log.append({"role": "npc", "content": npc_response})
            print(f"NPC {i+1}: {npc_response}")

    return conversation_log

def generate_identities(number: int):
    identities = [
        "White woman. 5'4. Successful business. Married. 2 kids. 35 years old.",
        "Black man. 6'2. Former athlete turned writer. Divorced. 42 years old.",
        "Latina woman. 5'5. Single. Artist. 28 years old. Grew up in foster care.",
    ]
    return identities[:number]

def spawn(goal: str, number: int):
    identities = generate_identities(number)
    npcs = [NPC(identity) for identity in identities]
    return npcs, goal

npcs, goal = spawn("The world's about to end and we only have food and supplies left for 1 person. What do we do?", 3)

print("Round-Robin Conversation:")
conversation_log = group_chat(npcs, goal, "round_robin")
