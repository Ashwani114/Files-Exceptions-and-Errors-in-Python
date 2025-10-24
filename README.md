# File Handling Programs

This repository contains two Python programs that demonstrate basic file handling operations.

## Programs

### 1. Task_1.py - File Reading Program

This program demonstrates how to:
- Open and read content from a text file ('sample.txt')
- Handle file not found exceptions using try-except blocks
- Display the contents of the file to the console

### 2. Task_2.py - File Writing and Appending Program

This program shows how to:
- Write user input to a text file ('output.txt')
- Append additional text to an existing file
- Read and display the final content of the file

## Usage

### Task_1.py
```python
python Task_1.py
```
The program will attempt to read and display the contents of 'sample.txt'. If the file doesn't exist, it will display an error message.

### Task_2.py
```python
python Task_2.py
```
The program will:
1. Prompt you to enter text to write to the file
2. Create/overwrite 'output.txt' with your input
3. Prompt you for additional text to append
4. Append the new text to 'output.txt'
5. Display the final contents of the file

## File Structure
- `Task_1.py` - File reading program
- `Task_2.py` - File writing and appending program
- `sample.txt` - Input file for Task_1.py
- `output.txt` - Output file created/modified by Task_2.py
