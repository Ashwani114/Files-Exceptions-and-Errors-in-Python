try:
    fh = open('sample.txt', 'r')
    content = fh.read()
    print("Reading file content: ")
    print(content)
    fh.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
    