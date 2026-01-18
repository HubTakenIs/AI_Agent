import argparse
import os
from prompts import system_prompt
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()
    if api_key is None:
        raise RuntimeError("No Api Key found")
    client = genai.Client(api_key=api_key)
    # prompt_text = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]

    prompt_text = args.prompt
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,temperature=0),
    )
    if response.usage_metadata is None:
        raise RuntimeError("No token meta data returned.")

    prompt_token_count = response.usage_metadata.prompt_token_count
    response_token_count = response.usage_metadata.candidates_token_count
    if args.verbose:
        print(f"User prompt: {prompt_text}")
        print(f"Prompt tokens: {prompt_token_count}")
        print(f"Response tokens: {response_token_count}")
    if response.function_calls is not None:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print("Response: ")
        print(response.text)


if __name__ == "__main__":
    main()
