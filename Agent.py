from openai import OpenAI

class Agent:
    def __init__(self, prompt : str, identity: str, client: OpenAI):
        self.prompt = prompt
        self.identity = identity
        self.client = client
        self.model_name = "llama3.1-8b"
        self.backstory = self._create_backstory()
        self.conversation_context = []
        
    def _create_backstory(self):
        response = self.client.chat.completions.create(
            messages = [{
            "role": "system",
            "content": '''Develop a deeply realistic, human-like backstory that equally explores both 
                    the strengths and flaws of this character. Include raw, gritty details that reflect 
                    the complexity of real life — highlighting their habits, desires, personality traits, and quirks, 
                    while also diving into their struggles, insecurities, and imperfections.'''},
            {
                "role": "user",
                "content": self.identity
            }],
            model=self.model_name,
            stream=False
        )
        backstory = response.choices[0].message.content
        return backstory
        
    def chat(self):
        response = self.client.chat.completions.create(
            messages=[{
                    "role": "system",
                    "content": f'''You are an imaginary voter: {self.identity}. This is your backstory: {self.backstory}.
                    Every response should reflect their identity, personal history, experiences, struggles, and values. 
                    Here's what to consider: Speech Patterns: Adapt your tone, vocabulary, and speech style to 
                    align with the character’s background. Thought Process: Respond as if you are truly living through this 
                    character's worldview. Personality and Flaws: Make sure to express their unique personality traits, quirks, 
                    and imperfections. This is the group conversation: {self.conversation_context}'''
                },
                {
                    "role": "user",
                    "content": self.prompt
                }],
            model=self.model_name,
            stream=False
        )
        agent_reply = response.choices[0].message.content
        self.conversation_context.append(self.identity + ": " + agent_reply)
        return agent_reply
