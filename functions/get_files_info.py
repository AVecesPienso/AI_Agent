import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    abs_working_directory = os.path.abspath(working_directory)
    target_directory = os.path.abspath(full_path)
    
    if not target_directory.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_directory):
        return f'Error: "{directory}" is not a directory'
    
    try:
        directory_list = os.listdir(target_directory)
        files_info = []
        for file_name in directory_list:
            file_path = os.path.join(target_directory, file_name)
            is_dir = os.path.isdir(file_path)
            file_size = os.path.getsize(file_path)

            files_info.append(f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir}")
        
        return "\n".join(files_info)
          
    except Exception as e:
        return f"Error: {e}"
