import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="write provided content to a file",
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
            "content": types.Schema(
                type=types.Type.STRING,
                description="a string of content to be written",
            )
        },
    ),
)


def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot write to "{working_dir_abs}" as it is outside the permitted working directory'
        if os.path.isdir(target_file):
            return f'Error: cannot write to "{target_file}" as it is a directory'
        os.makedirs(working_dir_abs,exist_ok=True)
        with open(target_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{target_file}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error writing to file ... {e}'