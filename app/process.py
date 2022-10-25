from http.client import ResponseNotReady
from typing import List
import os
import openai
import argparse
import re

MAX_INPUT_LENGTH = 12

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User input: {user_input}")
    if validate_length(user_input):
        generate_snippet(user_input)
        generate_keyword(user_input)
    else:
        raise ValueError("Input is too long. Must be under {MAX_INPUT_LENGTH}")

def validate_length(prompt: str) -> bool:
    return len(prompt) <= MAX_INPUT_LENGTH

def generate_keyword(prompt: str) -> List[str]:
    #Load API key from OpenAI
    openai.api_key = os.getenv("OPENAI_API_KEY")
    enriched_prompt = f"Generate branding keywords for {prompt}: "
    print(enriched_prompt)
    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3", 
        prompt=enriched_prompt, 
        max_tokens=32
    )

    #Extract output
    keyword_text : str = response["choices"][0]["text"]

    #Remove blank space
    keyword_text = keyword_text.strip()
    keyword_array = re.split(",|\n|;|-", keyword_text)
    keyword_array = [k.lower().strip() for k in keyword_array]
    keyword_array = [k for k in keyword_array if len(k) > 0]

    print(f"Keywords array: {keyword_array}")
    return keyword_array


def generate_snippet(prompt: str):
    #Load API key from OpenAI
    openai.api_key = os.getenv("OPENAI_API_KEY")
    enriched_prompt = f"Generate upbeat branding snippet for {prompt}: "
    print(enriched_prompt)
    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3", 
        prompt=enriched_prompt, 
        max_tokens=32
    )

    #Extract output
    branding_text : str = response["choices"][0]["text"]

    #Remove blank space
    branding_text = branding_text.strip()

    #Add "..." at the end of string
    last_char = branding_text[-1]
    if last_char not in {".", "!", "?"}:
        branding_text += "..."

    print(f"Result: {branding_text}")
    return branding_text


if __name__ == "__main__":
    main()