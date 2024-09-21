import openai
from pydantic import BaseModel
gpt_client = openai.OpenAI(api_key="")

def gpt(input:str):
    completion = gpt_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f'''You are a brilliant problem-solver and logical thinker. 
             Given this problem: {input}, please break down the solution process step-by-step, 
             thinking through each part clearly and explaining your reasoning at every stage.'''},
        ]
    )
    return (completion.choices[0].message.content)

cerebras_client = openai.OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key="csk-tr33y8n58m4xh4h55yfdpckryddevjktxw4e5jw4m4w66536"
)

class GraderEvaluation(BaseModel):
    CorrectnessOrAccuracy: float
    DepthOfReasoning: float
    ClarityAndCoherence: float
    CreativityOrInnovation: float
    EfficiencyAndFeasibility: float

def judge(input:str):
    completion = gpt_client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f'''
    Task: Evaluate the quality of the provided solutions, approaches, or reasoning on a scale from 1 to 10 (1 = Poor, 10 = Excellent). Base your evaluation on the following criteria:

    1. Correctness/Accuracy: Does the solution correctly address the problem or question? Are the key facts or principles accurately represented?
    2. Depth of Reasoning: Is the approach or reasoning thorough and well-developed? Does it demonstrate a strong understanding of the underlying concepts?
    3. Clarity and Coherence: Is the solution clearly articulated and easy to follow? Are the arguments logically organized and free of contradictions?
    4. Creativity/Innovation: Does the solution introduce novel or insightful ideas that go beyond standard approaches? Is the reasoning creative in tackling the problem?
    5. Efficiency and Feasibility: For practical problems, is the approach efficient and realistic? Does it provide a solution that can be implemented effectively?

    For each response:
    - Provide a numerical score (1-10) for each criterion.
    - Offer a brief explanation for each score, noting strengths and areas for improvement.
    - Conclude with an overall assessment, explaining why the given response excels or falls short in comparison to an ideal solution.
    Here is the response you need to evaluate: {input}'''},
        ],
        response_format=GraderEvaluation
    )
    return (completion.choices[0].message.content) 


solution = gpt("You are a member of Bloomgberg's board of directors. You must find a solution for improving financial literacy in the city of New York. You must come to a unified conclusion.")
print(solution)
scores = judge(solution)
print(scores)


