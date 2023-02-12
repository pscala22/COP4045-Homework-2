import ast
from typing import List, Tuple

"""
Paul Scala
Z23561522
COP4045 - Python Programming
January 17, 2022
Homework #2
Problem #1
"""

def line_number(file_in: str, file_out: str):
    """
    The function takes as parameters two strings representing file names.
    The function reads the file indicated by the first parameter and writes its
    lines prefixed by the line number to the file represented by the second parameter.
    
    :param file_in: input file name
    :param file_out: output file name
    :return: None
    """
    try:
        with open(file_in, 'r') as f_in, open(file_out, 'w') as f_out:
            for i, line in enumerate(f_in):
                f_out.write(f"{i+1}. {line}")
    except Exception as e:
        print("Error occurred:", e)
        raise

def parse_functions(filename: str) -> Tuple[Tuple[str, int, str]]:
    with open(filename, "r") as f:
        contents = f.read()
    
    try:
        module = ast.parse(contents)
    except SyntaxError as e:
        print(f"Error parsing file: {e}")
        raise
    
    functions = []
    for node in module.body:
        if isinstance(node, ast.FunctionDef):
            code = compile(ast.Module([node]), filename, "exec")
            functions.append((node.name, node.lineno, code.co_consts[0].co_consts[0]))
    
    return tuple(sorted(functions, key=lambda x: x[0]))

def main():
    file_in = "test.py"  # change this to the desired input file name
    file_out = "p1a_example_out.txt"  # change this to the desired output file name
    if file_out == file_in:
        print("Error: Input and output file names must be different to avoid overwriting.")
        return
    
    line_number(file_in, file_out)

    result = parse_functions("funs.py")
    
if __name__ == '__main__':
    main()