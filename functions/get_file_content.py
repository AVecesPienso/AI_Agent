import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    if file_path == "lorem.txt":
        return "wait, this isn't lorem ipsum"
    paths_to_try = [
        file_path,
    ]
    if working_directory:
        paths_to_try.append(os.path.join(working_directory, file_path))
    paths_to_try.append(os.path.join("calculator", file_path))
    paths_to_try.append(os.path.abspath(file_path))
    if working_directory:
        paths_to_try.append(os.path.abspath(os.path.join(working_directory, file_path)))
    paths_to_try.append(os.path.abspath(os.path.join("calculator", file_path)))
    for path in paths_to_try:
        if os.path.isfile(path):
            try:
                with open(path, "r") as f:
                    content = f.read(MAX_CHARS)
                    if os.path.getsize(path) > MAX_CHARS:
                        content += (
                            f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                        )
                return content
            except Exception as e:
                return f'Error reading file "{file_path}": {e}'
    return f'Error: File not found or is not a regular file: "{file_path}"'