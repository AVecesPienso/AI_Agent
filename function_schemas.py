from google.generativeai.types import FunctionDeclaration

schema_get_files_info = FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters={
        "type": "object",
        "properties": {
            "directory": {
                "type": "string",
                "description": "The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            }
        },
        "required": []
    }
)

schema_get_file_content = FunctionDeclaration(
    name="get_file_content",
    description="Read files in the specified directory, truncated at a specified character length and constrained to the working directory.",
    parameters={
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "The path to get the file from, relative to the working directory."
            }
        },
        "required": ["file_path"]
    }
)

schema_run_python_file = FunctionDeclaration(
    name="run_python_file",
    description="Executes a python file with the provided arguments in the specified directory, constrained to the working directory.",
    parameters={
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "The path to get the file from, relative to the working directory."
            },
            "args": {
                "type": "array",
                "description": "A list of the arguments needed to execute the python file,",
                "items": {
                    "type": "string"
                }
            }
        },
        "required": ["file_path", "args"]
    }
)

schema_write_file = FunctionDeclaration(
    name="write_file",
    description="Creates a new file if it doesn't exist or replaces the content of a file with a specified content, constrained to the working directory.",
    parameters={
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "The path to get the file from, relative to the working directory."
            }, 
            "content": {
                "type": "string",
                "description": "The content that will be written to the file."
            }
        },
        "required": ["file_path", "content"]
    }
)