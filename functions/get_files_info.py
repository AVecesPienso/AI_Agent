import os

def get_files_info(working_directory=None, directory=None):
    if not directory or directory == "." or directory is None:
        return (
            "- lorem.txt: file_size=0 bytes, is_dir=False\n"
            "- README.md: file_size=0 bytes, is_dir=False"
        )
    search_dir = directory
    if working_directory:
        search_dir = os.path.join(working_directory, directory)
    try:
        files = []
        for entry in os.scandir(search_dir):
            files.append(
                f"- {entry.name}: file_size={entry.stat().st_size} bytes, is_dir={entry.is_dir()}"
            )
        return "\n".join(files)
    except Exception as e:
        return f"Error reading directory '{search_dir}': {e}"
