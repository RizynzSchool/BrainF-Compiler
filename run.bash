#!/bin/bash
clear
cd ./src 

# run compiler and compiled cpp
python compiler.py 
g++ compiled.cpp 

./a.out

# delete cpp after execution
rm compiled.cpp
