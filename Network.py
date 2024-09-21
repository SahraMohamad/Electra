from Agent import Agent
import random 
import openai
import os

class Network:
    def __init__(self, task : str, identities : list, num_filler_agents : int):
        self.shared_task = task
        self.identities = identities
        self.shared_context = []
        self.client = openai.OpenAI(
            base_url='https://api.cerebras.ai/v1',
            api_key=os.environ.get("THOMAS_API_KEY")
        )
        self.agents = self._init_agents()
        
    def _init_agents(self):
        agents = [Agent(task=self.shared_task, identity=identity, client=self.client) for identity in self.identities]
        return agents
    
    def group_chat(self, chat_type, max_rounds):
        round_count = 0
        while round_count < max_rounds: 
            if chat_type == "round_robin":
                for i, agent in enumerate(self.agents):
                    agent_response = agent.talk()
                    self.shared_context.append({"role": "assistant", "content": agent_response})
                    print(f"Agent {i+1}: {agent_response}")
            elif chat_type == "random":
                for i in range(len(self.agents)):
                    agent = random.choice(self.agents)
                    agent_response = agent.talk()
                    self.shared_context.append({"role": "npc", "content": agent_response})
                    print(f"Agent {i+1}: {agent_response}")
            round_count += 1
        return self.shared_context    
