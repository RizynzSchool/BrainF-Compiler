# Compile to C++
import os
from colorama import Fore, Style

good_col = Fore.GREEN
warning_col = Fore.YELLOW
error_col = Fore.RED

def find_file(dir_path, extension):
    results = []
    
    for file in os.listdir(dir_path):
        if file.endswith(extension):
            results.append(os.path.join(dir_path, file))

    if (len(results) > 1):
        print(warning_col + "You have multiple .bf files!" + Fore.RESET)
        
        # list files
        for i in range(len(results)):
            print(f"[{i}] {results[i]}")

        # file input handling
        file_input = input("Input File Index >> ")
        if len(file_input) > 1:
                file_input = int(input("Input File Index >> "))
        else:
                file_input = 0

        while file_input > len(results) -1:
            if len(file_input) > 1:
                file_input = int(input("Input File Index >> "))
            else:
                file_input = 0
        
        results = results[file_input]

    elif (len(results) == 0):
        print(error_col + "No .bf Files Found" + Fore.RESET)
        quit()

    return results

def read_file(file_name):
    if os.path.exists(file_name):
        contents_arr = []
        # get file path
        file_path = os.path.realpath(file_name)
        print("File Path: " + good_col + file_path + Fore.RESET)

        # get file contents
        file = open(file_path, "r")
        contents = file.read()
        file.close()
        
        # contents -> arr
        for c in contents:
            contents_arr.append(c)

        return contents_arr

    else:
        print(error_col + "ERROR: File Does Not Exist" + Fore.RESET)
        quit()

def lex(char):
    lex_dict = {'>' : "PR",
                '<' : "PL",
                '+' : "AD",
                '-' : "SB",
                '[' : "LS",
                ']' : "LE",
                '.' : "OT",
                ',' : "IN",}

    if char in lex_dict.keys():
        return lex_dict[char]
    else:
        return ''

def compile(contents_arr):
    looped = False
    # lex -> arr
    lex_arr = []
    for i in contents_arr:
        lex_arr.append(lex(i))

    # arr -> cpp
    file_name = "compiled.cpp"
    cpp_code = "#include <iostream>\nusing namespace std;\nint main() {\n\tint cells[30000] = {};\n\tint point = 0;\n\tchar inputchar;\n\tint ascii;" # cpp init

    for l in lex_arr:
        if (l == "PR"):
            if looped:
                cpp_code += "\n\t\tpoint++;"
            else:
                cpp_code += "\n\tpoint++;"

        elif (l == "PL"):
            if looped:
                cpp_code += "\n\t\tpoint--;"
            else:
                cpp_code += "\n\tpoint--;"
        
        elif (l == "AD"):
            if looped:
                cpp_code += "\n\t\tcells[point] += 1;"
            else:
                cpp_code += "\n\tcells[point] += 1;"

        elif (l == "SB"):
            if looped:
                cpp_code += "\n\t\tcells[point] -= 1;"
            else:
                cpp_code += "\n\tcells[point] -= 1;"

        elif (l == "LS"):
            cpp_code += "\n\twhile (true) {\n\t\tif (cells[point] == 0) {\n\t\t\tbreak;\n\t\t}"
            looped = True

        elif (l == "LE"):
                cpp_code += "\n\t};"
                looped = False

        elif (l == "IN"):
                if looped:
                    cpp_code += "\n\t\tinputchar = getchar();\n\t\tascii = (int)inputchar;\n\t\tcells[point] = ascii;"
                    
                else:
                    cpp_code += "\n\tinputchar = getchar();\n\tascii = (int)inputchar;\n\tcells[point] = ascii;"

        elif (l == "OT"):
                if looped:
                    cpp_code += "\n\t\tcout << (char)cells[point];"
                else:
                    cpp_code += "\n\tcout << (char)cells[point];"
        

    cpp_code += "\n\tcout << endl;\n\treturn 0;\n}"

    # write to cpp file
    with open(file_name, "w") as file:
        file.write(cpp_code)

# func run
try:
    current_directory = os.path.dirname(os.path.abspath(__file__))
    files = find_file(current_directory, ".bf")
    os.system('clear')
    file_contents = read_file(''.join(files))
    compile(file_contents)
except Exception as e:
    os.system('clear')
    print(str(e))
