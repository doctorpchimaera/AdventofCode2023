#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 11:31:24 2023

@author: donal
"""
import os
import re

### GET INPUT DATA FROM FILE ###
path = "/mnt/Data/Tresorit/Puzzles+Games/Advent of Code 2023/Day 2"
inputFile = "input_2"

fileData = open(os.path.join(path, inputFile), 'r')

data = []

for dataline in fileData:
    data.append(dataline.split('\n')[0])    # Strip out newlines now

fileData.close()

### PARTS 1 & 2 RUNNING SIDE BY SIDE ###
limits = [12, 13, 14]   # R, G, B limits for a valid game in Part 1

total = 0       # Total score for Part 1
powerTotal = 0  # Total power score for Part 2

for line in data:   # Processes each line of data from the input file
    gameStatus = 'FAIL'     # Game status for printing, defaults to FAIL
    # Turn tracking: if Status == Count, every turn in that line has passed
    turnStatus = 0      # Adds 1 each time a turn is valid
    turnCount = 0       # Adds 1 for every turn
    
    # Break up the line into its components
    firstSplit = line.split(':')   # Split Game # from colour triads
    secondSplit = firstSplit[1].split(';') # Split out colour triads as a set
    
    # Pull out the game number from the text
    gameNum = int(re.findall(r'[0-9]+', firstSplit[0])[0])
    
    # Initialise colour running totals
    redVal = 0
    greenVal = 0
    blueVal = 0
    
    redCount = []
    greenCount = []
    blueCount = []       
    
    # Parse each colour triad in the line, find out how many of each are present and add them up
    for game in secondSplit:
        turnCount += 1  # Count this turn
        # Each game variable is a single turn in a single string
        # Split game string into individual colours
        colours = game.split(',')   # Splits game string into individual colours (qty + colour)
        
        for colour in colours:
            colour = colour.replace(" ","")     # Get rid of spaces 
            colourVal = re.findall(r'[0-9]+', colour)[0]    # Extract quantity
            colourText = colour[(colour.find(colourVal) + len(colourVal)):].replace(" ", "")    # Extract text
            
            # Colour assignment: assign colourVal to the correct variable and add this to the count list
            # We need the count list for part 2
            if colourText == 'red':
                redVal = int(colourVal)
                redCount.append(redVal)
            elif colourText == 'green':
                greenVal = int(colourVal)
                greenCount.append(greenVal)
            elif colourText == 'blue':
                blueVal = int(colourVal)
                blueCount.append(blueVal)
        
        # If all three colour totals are less than the specified limits, 
        #       this turn is good and is added to the status total
        if redVal <= limits[0] and greenVal <= limits[1] and blueVal <= limits[2]:
            turnStatus += 1    
                    
    
    if turnStatus == turnCount:
        # All turns in this game line are valid, therefore the game is valid => add it to the total
        total += gameNum
        gameStatus = 'PASS'
        
    # Calculate power for this game line and add it to the total
    # Max of each colour's value is the minimum #cubes needed to play this line
    power = max(redCount) * max(greenCount) * max(blueCount)
    powerTotal += power
    
    print("<< Game Number {} >>".format(gameNum))
    print("Outcome: {}\n".format(gameStatus))
   
print("\nGame Total: {}".format(total))
print("Power: {}".format(powerTotal))    