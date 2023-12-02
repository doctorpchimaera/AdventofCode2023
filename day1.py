#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 18:03:44 2023

@author: donal
"""
import os
import re

path = "/mnt/Data/Tresorit/Puzzles+Games/Advent of Code 2023/Day 1"
inputFile = "input_1.1"

fileData = open(os.path.join(path, inputFile), 'r')

data = []
for dataline in fileData:
    data.append(dataline[0:-1])

### PART 1 ###
total = 0
    
for line in data:
    digits = re.findall(r'[0-9]', line)
    total = total+int(digits[0]+digits[-1])

### PART 2 ###
digitRef = [['zero', '0'], 
            ['one', '1'], 
            ['two', '2'],
            ['three', '3'],
            ['four', '4'],
            ['five', '5'],
            ['six', '6'],
            ['seven', '7'],
            ['eight', '8'],
            ['nine', '9']]

total2 = 0

# data = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', 
#         '4nineeightseven2', 'zoneight234', '7pqrstsixteen']

# For each line we need to find the left and rightmost instances of both numerical and text digits
# Once these 4 are found, determine which of the two left values is leftmost &
#       which of the two right values is rightmost

for line in data:
    # Start by finding out where the text digits are in the line
    first = []  # Index to first instances of each text digit in the line
    last = []   # Index to last instances of each text digit in the line
    
    for digit in digitRef:
        first.append(line.find(digit[0]))
        # Reverse the line and the search term to get the rightmost instance 
        # This will return an index relative to the end of the string so it must be switched around
        # What we actually end up with is the end of the digit text in the string which is ideal
        last.append(len(line) - line[::-1].find(digit[0][::-1]) - 1)
        
    # str.find() returns -1 when no match is found, so we need to deal with these
    # First instances should be set to the end of the string where they will 
    #       always be later than a subsequent numerical digit match on the left
    # Similarly last instances should be set to the start of the string
    checkF = 0      # check variables
    checkL = 0

    for i in range(0, 10):
        if first[i]  == -1:
            first[i] = len(line)
            checkF = checkF + 1     # Every time no match is found this increments
        if last[i] == len(line):
            last[i] = 0
            checkL = checkL + 1
    
    textPos = []        # Position of text digit in the string
    textDigit = []      # What the digit is
    
    # There are 10 digits, so if we have 10 failed matches, there are no text digits in the string in 
    #       that direction
    if checkF != 10:
        # We have at least one text digit, lets find it & replace with numeral
        textPos.append(min(first))
        textDigit.append(first.index(min(first)))

    if checkL != 10:
        # We have some more text digits, lets find the last one & replace with numeral
        textPos.append(max(last))
        textDigit.append(last.index(max(last)))

    # Now any text digits and their positions are known
    # Find the numerical digits with regex
    digits2 = re.findall(r'[0-9]', line)
    digitPos = []   # We need to store the positions of these numerical digits later
    
    if len(digits2) > 0 and len(textPos) > 0:
        # We have text and numerical digits so we see which are first/last
        # Find the position of the numerical digits (since they exist)
        digitPos.append(line.find(digits2[0]))
        digitPos.append(len(line) - 1 - line[::-1].find(digits2[-1]))
        
        # Leftmost digit comparison
        if digitPos[0] < textPos[0]:
            # A numerical digit is first
            leftVal = digits2[0]
        else:
            # A text digit is first
            leftVal = str(textDigit[0])
        
        # Rightmost digit comparison
        if digitPos[-1] > textPos[-1]:
            # A numerical digit is last
            rightVal = digits2[-1]
        else:
            rightVal = str(textDigit[-1])
            
    elif len(digits2) == 0:
        # No numerical digits, we only have text digits
        leftVal = str(textDigit[0])
        rightVal = str(textDigit[1])
    elif len(textDigit) == 0:
        # No text digits, we only have numerical digits
        leftVal = digits2[0]
        rightVal = digits2[-1]
    
    # leftVal and rightVal come out as strings, so we stick them together, convert to int and 
    #       add to the running total
    total2 = total2 + int(leftVal + rightVal)
    
    # print(line)
    # print(leftVal + rightVal)
    # print(str(total2))
    # print('\n')
 
### PRINT OUT RESULTS ###
print("Total Part 1 is: ")
print(total)
print('\n')
print("Total Part 2 is: ")
print(total2)
print('\n')