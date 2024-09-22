from Agent import Agent
import random 
import openai
from generate_identity import generate_identities

class Network:
    def __init__(self, prompt : str, state: str, num_agents:int):
        self.prompt = prompt
        self.identities = self._create_identities(state, num_agents)
        self.client = openai.OpenAI(
            base_url='https://api.cerebras.ai/v1',
            api_key=""
        )
        self.shared_context = []
        self.agents = self._init_agents()
        
    def _create_identities(self, state:str, num_agents:int):
        identities = generate_identities(state, num_agents)
        return identities
        
    def _init_agents(self):
        agents = [Agent(prompt=self.prompt, identity=identity, client=self.client) for identity in self.identities]
        return agents
    
    def group_chat(self, chat_type, max_rounds):
        round_count = 0
        while round_count < max_rounds: 
            if chat_type == "round_robin":
                for i, agent in enumerate(self.agents):
                    agent_response = agent.chat()
                    self.shared_context.append({"role": "agent", "content": agent_response})
                    print(f"\n{agent.identity}: {agent_response}")
            elif chat_type == "random":
                for i in range(len(self.agents)):
                    agent = random.choice(self.agents)
                    agent_response = agent.chat()
                    self.shared_context.append({"role": "agent", "content": agent_response})
                    print(f"\n{agent.identity}: {agent_response}")
            round_count += 1
        return self.shared_context
    
    def simulate(self):
        self.group_chat()
