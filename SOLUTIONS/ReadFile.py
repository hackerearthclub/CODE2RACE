#!/usr/bin/python
import os

file = raw_input("Enter name of the file to read: ")
with open(file, "r") as file:
    data = file.read()
    String = data.split("\n")[0]

print String
