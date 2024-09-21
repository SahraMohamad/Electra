import openai
from pydantic import BaseModel
gpt_client = openai.OpenAI(api_key="")

class IdentitySchema(BaseModel):
    ListOfIdentities: list[str]

def generate_identities(input:str, num_voters:int):
    completion = gpt_client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f'''
    You are a brilliant problem-solver and logical thinker. 

    Given this problem: "{input}", you are tasked with simulating a list of {num_voters} random basic voter identities for a population in a given city (e.g., Atlanta, Georgia). 

    The identities should be proportional to the actual population demographics of the city, which includes:
    - Race/Ethnicity proportions
    - Age group breakdowns (e.g., 18-24, 25-34, 35-44, 45-64, 65+)
    - Gender distribution (e.g., male, female, non-binary)
    - Political leanings (e.g., Democrat, Republican, Independent, Other), with leanings proportional to the city's historical voting patterns and demographic data.

    Each voter identity should be simple and include:
    - A unique name identifier (like "Joey Chestnut")
    - Race/Ethnicity (e.g., "Black", "White", "Hispanic", "Asian", etc.)
    - Age group (e.g., "18-24", "25-34", etc.)
    - Height (e.g., "5'8", "5'10", "5'3")
    - Weight (e.g., "120", "145", "180")
    - Gender (e.g., "Male", "Female", "Non-binary")
    - Political leaning (e.g., "Democrat", "Republican", "Independent", "Other")

    The political leanings must be based on real-world voting trends for the city. For example, in a city like Atlanta, Georgia, you might see more Democratic leanings, especially among certain racial groups, age ranges, and urban areas.

    Example output:
    - Joey Midler: Race: Black, Age: 25-34, Height: 5'1, Weight: 150, Gender: Female, Political leaning: Democrat
    - Michael Smith: Race: White, Age: 45-64, Height: 5'9, Weight: 190, Gender: Male, Political leaning: Republican
    - Adam Swavy: Race: Hispanic, Age: 18-24, Height: 6'1, Weight: 224, Gender: Non-binary, Political leaning: Independent

    Generate a list of random voters proportional to the actual population distribution and political leanings of the input city. 

    Please break down the solution process step-by-step, explaining your reasoning at every stage.'''},
        ],
        response_format=IdentitySchema
    )
    return (completion.choices[0].message.content) 
