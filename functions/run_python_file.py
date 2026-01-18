import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="run a python file with given arguments",
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
            "args": types.Schema(
                type=types.Type.OBJECT,
                description="a list of strings of arguments to pass to the file",
            )
        },
    ),
)

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file.endswith(".py"):
           return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        if args:
            command.extend(args)

        process = subprocess.run(command,cwd=working_dir_abs, capture_output=True, text=True, timeout=30)
        output= ""
        if process.returncode != 0:
            output += f"Process exited with code {process.returncode} \n"
        
        
        
        
        if process.stdout:
            output += f"STDOUT: {process.stdout}\n"

        if process.stderr:
            output += f"STDERR: {process.stderr}\n"

        if not process.stdout and not process.stderr:
            output += f"No Output Produced\n"
        return output 
    except Exception as e:
        return f"Error: executing Python file: {e}"
