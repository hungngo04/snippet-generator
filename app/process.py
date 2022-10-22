from http.client import ResponseNotReady
import os
import openai
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User input: {user_input}")
    result = generate_snippet(user_input)
    print(result)



def generate_snippet(prompt: str):
    #Load API key from OpenAI
    openai.api_key = os.getenv("OPENAI_API_KEY")
    enriched_prompt = f"Generate upbeat branding snippet for {prompt}: "
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

    return branding_text


if __name__ == "__main__":
    main()