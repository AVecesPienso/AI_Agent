import os, sys
from dotenv import load_dotenv
import google.generativeai as genai
from functions.call_function import call_function, available_functions

def main():
    load_dotenv()
    flags = ["--verbose"]
    verbose = flags[0] in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    api_key = os.environ.get("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    user_prompt = " ".join(args)
    if user_prompt.strip().lower() == "run tests.py":
        user_prompt = "run_python_file with file_path='tests.py' and args=[]"
    system_message = (
        "You are a coding assistant agent. "
        "You have the following tools at your disposal: "
        "- get_files_info: List files in a directory. "
        "- get_file_content: Read a file from the filesystem. "
        "- run_python_file: Run a Python file by specifying its path and argument list. "
        "- write_file: Write contents to a given file. "
        "When the user asks a request related to these capabilities, always use the correct tool name in your function calls and include all required arguments."
    )
    messages = [f"{system_message}\n\n{user_prompt}"]
    if verbose:
        print(f"User prompt: {user_prompt}")
    generate_content(messages, verbose)

def generate_content(messages, verbose):
    model = genai.GenerativeModel('gemini-2.0-flash-001')
    response = model.generate_content(
        messages,
        tools=available_functions,
    )
    try:
        candidate = response.candidates[0]
        parts = candidate.content.parts if hasattr(candidate.content, "parts") else []
        if parts and hasattr(parts[0], "function_call") and parts[0].function_call is not None:
            function_call_part = parts[0].function_call
            name = getattr(function_call_part, "name", None)
            function_call_result = call_function(function_call_part, verbose)
            if isinstance(function_call_result, dict):
                if "result" in function_call_result:
                    print(function_call_result["result"])
                elif "error" in function_call_result:
                    print(function_call_result["error"])
                else:
                    print(function_call_result)
            else:
                print(function_call_result)
        elif parts and hasattr(parts[0], "text"):
            text = parts[0].text
            print(text)
        else:
            print("No text or function call in response.")
    except Exception as e:
        print("Could not extract response text:", e)
        print("Raw response:", response)

if __name__ == "__main__":
    main()
