# **Electoral LLM - Live Voter Polls w/ Intelligent Agents**

We built a multi-agent conversational & simulation framework from scratch. Leaner than CrewAI and Autogen, with just 4 lines of code, you can beat Chain-of-Thought prompting by relying on intelligent agents to do all the work for you. 

In Electoral-LLM, we adapted this framework to simulate how current events can affect voter popularity in real-time by mass-generating hordes of human-like llms with hyperspecific backstories and indentities. 

```python
from Network import Network
breaking_news = '''Breaking News! Donald Trump will launch his own cryptocurrency.'''
agent_network = Network(breaking_news, state = "Pennsylvania", num_agents = 15)
agent_network.simulate("round_robin", num_rounds = 1)
```

Electoral LLM  is an interactive web application designed to visualize real-time public sentiment for political candidates as the 2024 elections approach. Leveraging advanced language models and dynamic data visualization, the tool enables users to select a state, input specific scenarios, and explore sentiment trends across counties.
With an intuitive interactive map, users can easily comprehend public opinion and monitor shifts in sentiment over time.

Our aim is to provide a powerful, user-friendly platform that captures the diverse perspectives of communities nationwide, facilitating informed discussions around the upcoming elections.


## **Features**
- Interactive U.S. Map: Provides real-time visualization of sentiment data for political candidates across all U.S. counties.
- Advanced Sentiment Analysis: Leverages language models to deliver nuanced insights into public sentiment dynamics.
- Custom Scenario Inputs: Enables users to input different scenarios and observe their effects on public opinion toward candidates.

## **Technologies used**

### LLM's
- Cerebras: For high inference speed, crucial for generating and visualizing insights in real-time and at scale. Paramount for agentic frameworks.
- Llama 3.1 - 7b & 80b: Amazing LLM models in general, great for fine-tuning and open-source tooling

### Front-End
- CSS: For styling
- HTML: For markup
- React: For building the user interface
- D3.js: For dynamic data visualizations

### Back-End
- Node.js: For server-side logic
- Python: For data processing and integration

### Data Formats and Libraries
- GeoJSON: For geographic data representation

## **Setup Instructions**

### **Prerequisites**
- Python (version X.X)
- Node.js (if applicable for the front-end)

### **Installation Steps**
1. Clone the repository:
   ```bash git clone
       https://github.com/SahraMohamad/LLM-Net.git
       cd LLM-Net 
2. Install dependencies
3. 
### **Prerequisites**



