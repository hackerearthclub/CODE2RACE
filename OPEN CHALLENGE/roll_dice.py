# Reads strings and rolls dice based on those strings.
# Inputs are in the traditional DnD dice rolling format, or ndx, where n is the number of dice to roll and x is the number of sides on each die.
# Valid input examples: "1d6", "2d4", "2d6+5", "3d20+6d4", "1d15+4d7+13"

import random
import re

def roll(inputString):
    validity_check = re.match('((\d*d\d+\+?)+(\d)*)', inputString)
    if not validity_check:
        return "Invalid argument: {}".format(inputString)
    argument = validity_check.group(1)
    sections = argument.split('+')
    all_dice = ""
    total = 0
    addAmount = ""
    if not re.match('\d*d+\d+', sections[-1]):
        addAmount = " + " + sections[-1]
        total += (int) (sections[-1])
        del sections[-1]
    for die in sections:
        nums = die.split('d')
        if nums[0] == "":
            nums[0] = '1'
        for i in range(0, (int) (nums[0])):
            sides = (int) (nums[1])
            if sides < 1:
                return "Invalid argument: {}".format(inputString)
            result = random.randint(1, sides)
            if i > 0:
                all_dice += " + "
            total += result
            if sides == 20:
                all_dice += (str) (result)
            elif sides == 6:
                all_dice += (str) (result)
            elif sides == 4:
                all_dice += (str) (result)
            else:
                for num in (str) (result):
                    all_dice += num
        all_dice += " + "
    all_dice = all_dice[:-3]
    if len(sections) > 1 or (int) (nums[0]) > 1 or addAmount != "":
        return all_dice + addAmount + " = " + (str) (total)
    else:
        return all_dice

if __name__ == "__main__": 
    inputString = input("Enter some dice to roll: ")
    print (roll(inputString)) 