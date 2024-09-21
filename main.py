from Network import Network
from Agent import Agent
from variables import identities
def main():
    task = '''
    You are a members of a comittee which is trying to decide on a superhero name for a new marvel movie. 
    You must find a solution by the end of your conversation.
    You should output your final conclusion delimited by triple backticks.
    '''
    agent_network = Network(task=task, identities=identities, num_filler_agents=0)
    agent_network.group_chat("round_robin", 5)
    
if __name__ == '__main__':
    main()
