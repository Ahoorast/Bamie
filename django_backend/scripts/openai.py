import os
import environ
import openai

env= environ.Env()
environ.Env.read_env()

openai.api_key=env('OPENAI_API_KEY')

options=[]

system_instruction="As a customer service representive, choose the closest option and only return index of option. you have these options: "

for i, option in enumerate(options):
    system_instruction += str(i) + ". " + option + "\n"

def OpenaiResponse(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": prompt}
    ]
    #   temperature=0,
    #   max_tokens=256,
    )
    return response.choices[0].message["content"]
