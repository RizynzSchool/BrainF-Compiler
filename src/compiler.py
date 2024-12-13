# Compile to C++
import os

def read_file(file_name):
    if os.path.exists(file_name):
        contents_arr = []
        # get file path
        file_path = os.path.realpath(file_name)
        print("File Path: " + file_path)

        # get file contents
        file = open(file_path, "r")
        contents = file.read()
        file.close()
        
        # contents -> arr
        for c in contents:
            contents_arr.append(c)

        return contents_arr

    else:
        print("ERROR: File Does Not Exist")

def lex(char):
    lex_dict = {'>' : "PR",
                '<' : "PL",
                '+' : "AD",
                '-' : "SB",
                '[' : "LS",
                ']' : "LE",
                '.' : "OT",
                ',' : "IN",}

    return lex_dict[char]

def compile(contents_arr):
    looped = False
    # lex -> arr
    lex_arr = []
    for i in contents_arr:
        lex_arr.append(lex(i))

    print(', '.join(lex_arr))
    print(', '.join(contents_arr))

    # arr -> cpp
    file_name = "compiled.cpp"
    cpp_code = "#include <iostream>\nusing namespace std;\nint main() {\n\tint cells[30000] = {};\n\tint point = 0;" # cpp init

    for l in lex_arr:
        if (l == "PR"):
            if looped == True:
                cpp_code += "\n\t\tpoint++;"
            else:
                cpp_code += "\n\tpoint++;"

        elif (l == "PL"):
            if looped == True:
                cpp_code += "\n\t\tpoint--;"
            else:
                cpp_code += "\n\tpoint--;"
        
        elif (l == "AD"):
            if looped == True:
                cpp_code += "\n\t\tcells[point] += 1;"
            else:
                cpp_code += "\n\tcells[point] += 1;"

        elif (l == "SB"):
            if looped == True:
                cpp_code += "\n\t\tcells[point] -= 1;"
            else:
                cpp_code += "\n\tcells[point] -= 1;"

        elif (l == "LS"):
            cpp_code += "\n\twhile (true) {"
            cpp_code += "\n\t\tif (cells[point] == 0) {\n\t\t\tbreak;\n\t\t}"
            looped = True

        elif (l == "LE"):
                cpp_code += "\n\t};"
                looped = False

        elif (l == "IN"):
                cpp_code += "" #add in v2

        elif (l == "OT"):
                if looped == True:
                    cpp_code += "\n\t\tcout << (char)cells[point];"
                else:
                    cpp_code += "\n\tcout << (char)cells[point];"

    cpp_code += "\n\treturn 0;\n}"

    # write to cpp file
    with open(file_name, "w") as file:
        file.write(cpp_code)

# func run
file_contents = read_file("main.bf")
compile(file_contents)
