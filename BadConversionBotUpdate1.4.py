import random, time, login_info
reddit = login_info.reddit

units = ["meters", "feet", "yards", "miles", "inches", "grams", "kilograms", "pounds", "lbs", "tons"]

def check_for_units(comment, units, opted_out):
	split_string = comment.body.replace("\n", " ")
    split_string = split_string.split(" ")

    for unit in range(len(units)):
    	for word in range(len(split_string)):
    		if (units[unit] == split_string[word].lower()):
    			if (split_string[word - 1].isdigit() == True):
    				if (comment.author not in opted_out):
    					return unit, int(split_string[word - 1])

def make_units_standard(check_for_units):
	#if the unit in the comment is "meters"
        if (i == 0):
            old_unit = 1 * measurement
        #if the unit in the comment is "feet"
        elif (i == 1):
            old_unit = 0.3048 * measurement
        #if the unit in the comment is "yards"
        elif (i == 2):
            old_unit = 0.9144 * measurement
        #if the unit in the comment is "miles"
        elif (i == 3):
            old_unit = 1609.34 * measurement
        #if the unit in the comment is "inches"
        elif (i == 4):
            old_unit = 0.0254 * measurement
        #if the unit in the comment is "grams"
        elif (i == 5):
            old_unit = 1 * measurement
        #if the unit in the comment is "kilograms"
        elif (i == 6):
            old_unit = 1000 * measurement
        #if the unit in the comment is "pounds"
        elif (i == 7):
            old_unit = 453.592 * measurement
        #if the unit in the comment is "lbs"
        elif (i == 8):
            old_unit = 453.592 * measurement
        #if the unit in the comment is "tons"
        elif (i == 9):
            old_unit = 907185 * measurement