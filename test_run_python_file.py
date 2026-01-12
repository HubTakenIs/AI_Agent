from functions.run_python_file import run_python_file

output = run_python_file("calculator", "main.py")
print("Output for Calculator and Main.py")
print(output)

output = run_python_file("calculator", "main.py", ["3 + 5"])
print("Output for Calculator and Main.py with [3 + 5] as args")
print(output)

output = run_python_file("calculator", "tests.py",)
print("Output for Calculator and Main.py")
print(output)

output = run_python_file("calculator", "../main.py",)
print("Output for Calculator and ../main.py")
print(output)

output = run_python_file("calculator", "nonexistent.py",)
print("Output for Calculator and nonexistent.py")
print(output)

output = run_python_file("calculator", "lorem.txt",)
print("Output for Calculator and lorem.txt")
print(output)