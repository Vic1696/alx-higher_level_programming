#!/usr/bin/python3

# Initialize n as a global variable
n = 0

def magic_string():
    global n
    n += 1
    return ("BestSchool," * (n - 1) + "BestSchool")
