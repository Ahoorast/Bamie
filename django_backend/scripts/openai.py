import os
import environ
import openai

env= environ.Env()
environ.Env.read_env()

openai.api_key=env('OPENAI_API_KEY')

prompt=""
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": ""},
    {"role": "user", "content": prompt}
  ]
#   temperature=0,
#   max_tokens=256,
)
print(response.choices[0].message)