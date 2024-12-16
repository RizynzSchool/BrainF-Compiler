#!/bin/bash
clear
cd ./src 

# run compiler and compiled cpp
python compiler.py 
g++ compiled.cpp 

./a.out

# delete cpp and compiled file after execution
rm compiled.cpp
rm a.out 
