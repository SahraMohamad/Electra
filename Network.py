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
                    agent_response = agent.chat(self.shared_context)
                    self.shared_context.append(agent.identity + ": " + agent_response)
                    if len(self.shared_context) > 28000:
                        self.shared_context = self.shared_context[-14000:]
                    print(f"\n{agent.identity}: {agent_response}")
            elif chat_type == "random":
                for i in range(len(self.agents)):
                    agent = random.choice(self.agents)
                    agent_response = agent.chat(self.shared_context)
                    self.shared_context.append(agent.identity + ": " + agent_response)
                    if len(self.shared_context) > 28000:
                        self.shared_context = self.shared_context[-14000:]
                    print(f"\n{agent.identity}: {agent_response}")
            round_count += 1
        return self.shared_context
    
    def simulate(self, chat_type, max_rounds):
        pre_vote = [2]*len(self.agents)
        post_vote = [2]*len(self.agents)
        for i, agent in enumerate(self.agents):
            pre_decision = agent.pre_predict()
            pre_vote[i] = pre_decision
        self.group_chat(chat_type, max_rounds)
        for i, agent in enumerate(self.agents):
            post_decision = agent.post_predict()
            post_vote[i] = post_decision
        print(f"Pre-vote: {pre_vote}")
        print(f"Post-vote: {post_vote}")
        change = (sum(post_vote) - sum(pre_vote))/len(pre_vote) * 100
        change = round(change, 2)
        if change < 0:
            print(f"Harris' support increased by {-1*change}%")
        elif change > 0:
            print(f"Trump's support increased by {change}%")
        else:
            print("Voter support remained the same")
        return pre_vote, post_vote
