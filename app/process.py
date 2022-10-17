import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

subject = "dogs"
prompt = f"Generate branding snippet for {subject}"

response = openai.Completion.create(
    engine="davinci-instruct-beta-v3", 
    prompt=prompt, 
    max_tokens=32)

print(response)