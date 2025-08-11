from google.generativeai.types import FunctionDeclaration
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from function_schemas import *

func_dict = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file
}

available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file,
]

def call_function(function_call_part, verbose=False):
    name = getattr(function_call_part, "name", None)
    args = getattr(function_call_part, "args", None)
    if args is not None and not isinstance(args, dict):
        try:
            args = dict(args)
        except Exception:
            pass
    if name in func_dict:
        func_to_call = func_dict[name]
        if args is not None and isinstance(args, dict):
            args["working_directory"] = "./calculator"
            result = func_to_call(**args)
        else:
            result = func_to_call(working_directory="./calculator")
        return {
            "role": "tool",
            "name": name,
            "result": result,
        }
    else:
        return {
            "role": "tool",
            "name": name,
            "error": f"Unknown function: {name}",
        }