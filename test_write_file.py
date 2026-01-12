from functions.write_file import write_file

results = write_file("calculator", "lorem.txt","wait, this isn't lorem ipsum")
print("Results for calculator, lorem.txt")
print(results)

results = write_file("calculator", "pkg/morelorem.txt", "Lorem ipsum dolor sit amet")
print("Results for pkg/morelorem.txt, main.py")
print(results)

results = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print("Results for /tmp/temp.txt, main.py")
print(results)
