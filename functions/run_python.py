import os, subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_directory = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(["python", file_path, *args], cwd=working_directory, capture_output=True, timeout=30, text=True)
        lines = []

        if not result.stdout and not result.stderr:
            return "No output produced."
        if result.stdout:
            lines.append(f'STDOUT: {result.stdout}')
        if result.stderr:
            lines.append(f'STDERR: {result.stderr}')
        if result.returncode != 0:
            lines.append(f'Process exited with code {result.returncode}')
        return "\n".join(lines)
    
    except Exception as e:
        return f'Error: executing Python file: {e}'
