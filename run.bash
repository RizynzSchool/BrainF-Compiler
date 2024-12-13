#!/bin/bash

cd /workspaces/codespaces-blank/src
python compiler.py
g++ compiled.cpp
clear
./a.out
