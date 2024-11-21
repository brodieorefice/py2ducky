import time
import os 

def escape_special_characters(line):
    replacements = {
        "\\": "\\\\", 
        "\"": "\\\"",  
        "'": "\\'",    
        "`": "\\`",    
    }
    for char, escaped in replacements.items():
        line = line.replace(char, escaped)
    return line

def py_to_duckyscript(input_file, output_file, add_indentation):
    try:
        with open(input_file, 'r') as py_file:
            lines = py_file.readlines()
        duckyscript = []
        indent_level = 0
        for line in lines:
            stripped_line = line.strip()
            escaped_line = escape_special_characters(stripped_line)

            if line.startswith(' ') or line.startswith('\t'):
                new_indent_level = len(line) - len(line.lstrip())
                if new_indent_level < indent_level:
                    backspaces = (indent_level - new_indent_level) // 4
                    duckyscript.append(f"REPEAT {backspaces} BACKSPACE\n")
                indent_level = new_indent_level

            if add_indentation:
                tabs = indent_level // 4
                if tabs > 0:
                    duckyscript.append(f"REPEAT {tabs} TAB\n")

            duckyscript.append(f"STRING {escaped_line}\nENTER\n")

            if stripped_line.endswith(':'):
                indent_level += 4

        with open(output_file, 'w') as ducky_file:
            ducky_file.writelines(duckyscript)
        print(f"Converted {input_file} => {output_file} successfully.")
    except Exception as e:
        print(f"Error: {e}")

def app():
    print("Note: Only tested with python3.")
    add_indentation = input("Does your target environment lack auto-indent? (y/n): ").lower() == 'y'
    file = input("Enter python file: ")
    output_file = input("\nCustom output file name (enter to skip): ")
    if output_file == "":
        output_file = file + ".txt"
    py_to_duckyscript(file, output_file, add_indentation)

def credits():
    print("Created by [Your Name]")
    print("Version 1.1")
    print("Last updated: November 21, 2024")

def menu():
    while True:
        print("\nPython => DuckyScript")
        print("1. Start")
        print("2. Credits")
        print("3. Exit")
        menu_choice = input("Enter an option: ")
        if menu_choice == "1":
            app()
        elif menu_choice == "2":
            credits()
        elif menu_choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

menu()
