import openai

openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = "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"

response = openai.ChatCompletion.create(
  model="openai/gpt-3.5-turbo",
  messages=["hi"],
 
)

reply = response.choices[0].message