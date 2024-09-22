from openai import OpenAI

class Agent:
    def __init__(self, prompt : str, identity: str, client : OpenAI):
        self.identity = identity
        self.prompt = prompt
        self.system_prompt = self._create_system_prompt()
        self.model_name = "llama3.1-70b"
        self.client = client
        self.context = self._init_context()
        
    def _create_system_prompt(self):
        sys_prompt = {
            "role": "system",
            "content": f'''
            This is your identity: ###{self.identity}###, 
            And you have just been told this news: ###{self.prompt}###
            
            You should now begin to think about how this news will affect your voting disposition,
            and you should openly discuss if hearing the news has or has not changed your opinion on who you will vote for
            out of these two candidates: [Donald Trump, Kamala Harris]
            '''
        }
        
        return sys_prompt
        
    def _init_context(self):
        return [self.system_prompt]
        
    def talk(self):
        response = self.client.chat.completions.create(
            messages=self.context,
            model=self.model_name,
            stream=False
        )
        agent_reply = response.choices[0].message.content
        self.context.append({"role": "assistant", "content": agent_reply})
        return agent_reply
