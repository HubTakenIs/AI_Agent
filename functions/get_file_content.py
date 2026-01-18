import os
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="print file content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory":types.Schema(
                type=types.Type.STRING,
                description="Current working directory",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to read",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    MAX_CHARS = 10000
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    if not valid_target:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{target_file}"'
    try:
        with open(target_file,"r") as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += f'[...File "{target_file}" truncated at {MAX_CHARS} characters]'
            return file_content
    except OSError as e:
        return f'Error: error occurred opening file "{e}"'