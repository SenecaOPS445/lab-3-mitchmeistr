#!/usr/bin/env python3
'''
Author: Mitchell Gregoris
Student ID: 133349191
Email: mgregoris2@myseneca.ca
Program Name: lab3c.py
Date: 2024-05-14
Description: function operations
'''

import subprocess

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = p.communicate()
    # The above stdout is stored in bytes
    # Convert stdout to a string and strip off the newline characters
    stdout = output[0].decode('utf-8').strip()
    return stdout