import os
import environ
import openai

env= environ.Env()
environ.Env.read_env()

openai.api_key=env('OPENAI_API_KEY')

def OpenaiResponse(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": ""},
        {"role": "user", "content": prompt}
    ]
    #   temperature=0,
    #   max_tokens=256,
    )
    return response['choices'][0]['text']