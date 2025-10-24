user_input = input("Enter text to write to file: ")

with open('output.txt', 'w') as file:
    file.write(user_input)

print("Data successfully written to output.txt.")

user_input_append = input("Enter additional text to append: ")
with open('output.txt', 'at') as file:
    file.write(f"\n{user_input_append}")

print("Data successfully appended.")

with open('output.txt', 'r') as file:
    content = file.read()
    print("Final content of output.txt:")
    print(content)