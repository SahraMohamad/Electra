import openai
import json
from pydantic import BaseModel
gpt_client = openai.OpenAI(api_key="")

class IdentitySchema(BaseModel):
    ListOfIdentities: list[str]

def generate_identities(input:str, num_voters:int):
    state_data = ""
    completion = gpt_client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f'''
    You are a brilliant problem-solver and logical thinker. 

    You are tasked with simulating a list of {num_voters} hypothetical {input} voters with the help of the following data: {state_data}

    The identities should be proportional to the actual population demographics of the state, which includes:
    - Race/Ethnicity proportions (e.g., "Black", "White", "Hispanic", "Asian", etc.)
    - Age group breakdowns (e.g., 18-24, 25-34, 35-44, 45-64, 65+)
    - Gender distribution (e.g., male, female, non-binary)
    - Candidate choice (Kamala Harris or Donald Trump or Neutral), with support proportional to the state's historical voting patterns and demographic data. 
    - Intensity score (a number between 1 and 10, with 10 being the most in favor, and 1 being the least) that represents how strongly they are in favor of their canidate.
    

    Example output:
    - Joseph Smith: Race: Black, Age: 25-34, Gender: Female, Candidate choice: Kamala Harris, Intensity score: 7
    - Michael Kelly: Race: White, Age: 45-64, Gender: Male, Candidate choice: Donald Trump, Intensity score: 9
    - Adam Sullivan: Race: Hispanic, Age: 18-24, Gender: Non-binary, Candidate choice: Neutral, Intensity score: 4

    Generate a list of random voters proportional to the actual population distribution and political leanings of the input state. 

    Please break down the process to make the sample size as representative of the state as possible, step-by-step.'''},
        ],
        response_format=IdentitySchema
    )
    json_obj = json.loads(completion.choices[0].message.content)
    print(json_obj)
    return json_obj["ListOfIdentities"]
