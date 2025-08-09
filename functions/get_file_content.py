import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_working_directory = os.path.abspath(working_directory)
    target_directory = os.path.abspath(full_path)

    if not target_directory.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_directory):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_directory, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            next_char = f.read(1)
            if next_char:
                return file_content_string + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string
        
    except Exception as e:
        return f"Error: {e}"
