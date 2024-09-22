from openai import OpenAI

class Agent:
    def __init__(self, prompt : str, identity: str, client: OpenAI):
        self.prompt = prompt
        self.identity = identity
        self.client = client
        self.model_name = "llama3.1-8b"
        self.backstory = self._create_backstory()
        
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
        
    def chat(self, conversation_context: list):
        response = self.client.chat.completions.create(
            messages=[{
                    "role": "system",
                    "content": f'''You are an imaginary voter: {self.identity}. This is your backstory: {self.backstory}.
                    Every response should reflect the voter's identity, personal history, experiences, struggles, and values. 
                    Here's what to consider: Speech Patterns: Adapt your tone, vocabulary, and speech style to 
                    align with the voter's background. Thought Process: Respond as if you are truly living through the 
                    voter's worldview in first-person. Personality and Flaws: Make sure to express their unique personality traits, quirks, 
                    and imperfections. React to {self.prompt} and {conversation_context}. Remember you are in a group setting.'''
                }],
            model=self.model_name,
            stream=False
        )
        agent_reply = response.choices[0].message.content
        #self.conversation_context.append(self.identity + ": " + agent_reply)
        return agent_reply
