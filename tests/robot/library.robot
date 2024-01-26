*** Settings ***
Library     ../libraries/ClassLibrary.py
Library     ../libraries/no_class_library.py


*** Test Cases ***
Case 1: Biblioteca com classe
    Class Log Hello World

Case 2: Biblioteca sem classe
    Log Hello World
