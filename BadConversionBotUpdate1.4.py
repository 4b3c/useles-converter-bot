import random, time, login_info
reddit = login_info.reddit

units = ["meters", "feet", "yards", "miles", "inches", "grams", "kilograms", "pounds", "lbs", "tons"]

with open('opted_out.json') as file:
    opted_out = json.load(file)

def check_for_units(comment, units, opted_out):
	split_string = comment.body.replace("\n", " ")
    split_string = split_string.split(" ")

    for unit in range(len(units)):
    	for word in range(len(split_string)):
    		if (units[unit] == split_string[word].lower()):
    			if (split_string[word - 1].isdigit() == True):
    				if (comment.author not in opted_out):

                        unit_measurement = [unit, int(split_string[word - 1]), True]
    					return unit_measurement

def make_units_standard(unit_measurement):
    unit = unit_measurement[0]
    measurement = unit_measurement[1]

    if (unit == 0):
        standard_unit = 1 * measurement #meters
    elif (unit == 1):
        standard_unit = 0.3048 * measurement #feet
    elif (unit == 2):
        standard_unit = 0.9144 * measurement #yards
    elif (unit == 3):
        standard_unit = 1609.34 * measurement #miles
    elif (unit == 4):
        standard_unit = 0.0254 * measurement #inches
    elif (unit == 5):
        standard_unit = 1 * measurement #grams
    elif (unit == 6):
        standard_unit = 1000 * measurement #kilograms
    elif (unit == 7):
        standard_unit = 453.592 * measurement #pounds
    elif (unit == 8):
        standard_unit = 453.592 * measurement #lbs
    elif (unit == 9):
        standard_unit = 907185 * measurement #tons

    if (unit < 5):
        unit_type = "distance"
    elif (unit > 4):
        unit_type = "weight"

    type_and_amount = [unit_type, standard_unit]
    return type_and_amount

def create_comment(type_and_amount):
    unit_type = type_and_amount[0]
    standard_unit = type_and_amount[1]

    if (unit_type == "distance"):
        rand_num = random.randint(0, 10)
        if (rand_num == 0):
            new_record = " is  " + str(round(standard_unit / 0.313, 2)) + " RTX 3090 graphics cards lined up."
        elif (rand_num == 1):
            new_record = " is about the length of " + str(round(standard_unit / 0.6731, 2)) + 
            " 'EuroGraphics Knittin' Kittens 500-Piece Puzzles' next to each other."
        elif (rand_num == 2):
            new_record = " is the length of about " + str(round(standard_unit / 1.089914, 2)) + 
            " 'Ford F-150 Custom Fit Front FloorLiners' lined up next to each other."    
        elif (rand_num == 3):
            new_record = " is the height of " + str(round(standard_unit / 1.736852, 2)) + 
            " 'Samsung Side by Side; Fingerprint Resistant Stainless Steel Refrigerators' stacked on top of each other."
        elif (rand_num == 4):
            new_record = " is the length of like " + str(round(standard_unit / 0.22098, 2)) + 
            " 'Zulay Premium Quality Metal Lemon Squeezers' laid next to each other."
        elif (rand_num == 5):
            new_record = " is the same as " + str(round(standard_unit / 0.5, 2)) + 
            " 'Logitech Wireless Keyboard K350s' laid widthwise by each other."
        elif (rand_num == 6):
            new_record = " is the length of approximately " + str(round(standard_unit / 0.2286, 2)) + 
            " 'Wooden Rice Paddle Versatile Serving Spoons' laid lengthwise."
        elif (rand_num == 7):
            new_record = " is the length of exactly " + str(round(standard_unit / 0.101854, 2)) + 
            " 'Standard Diatonic Key of C, Blues Silver grey Harmonicas' lined up next to each other."
        elif (rand_num == 8):
            new_record = " is " + str(round(standard_unit / 203.606, 2)) + 
            "% of the hot dog which holds the Guinness wold record for 'Longest Hot Dog'."
        elif (rand_num == 9):
            new_record = " is the the same distance as " + str(round(standard_unit / 0.69, 2)) + 
            " replica Bilbo from The Lord of the Rings' Sting Swords."
        elif (rand_num == 10):
            new_record = " is the length of " + str(round(standard_unit / 0.127, 2)) + 
            " 'Bug Bite Thing Suction Tool - Poison Remover For Bug Bites's stacked on top of each other."
    
    elif (unit_type == "weight"):
        rand_num = random.randint(0, 10)
        if (rand_num == 0):
            new_record = " of solid gold is worth about $" + str(round(standard_unit * 57.91, 2)) + 
            "."
        elif (rand_num == 1):
            new_record = " of vegan poop being burned provides " + str(round(standard_unit * 16.5712, 2)) + 
            " BTU."
        elif (rand_num == 2):
            new_record = " is the weight of about " + str(round(standard_unit / 41.10681, 2)) + 
            " 'Kingston 120GB Q500 SATA3 2.5 Solid State Drives'."
        elif (rand_num == 3):
            new_record = " is the weight of literally " + str(round(standard_unit / 299.08747, 2)) + 
            " 'Velener Mini Potted Plastic Fake Green Plants'."
        elif (rand_num == 4):
            new_record = " is the same weight as " + str(round(standard_unit / 639.5652, 2)) + 
            " 'Double sided 60 inch Mermaker Pepparoni Pizza Blankets'."
        elif (rand_num == 5):
            new_record = " is excactly the weight of " + str(round(standard_unit / 112.8311, 2)) + 
            " '6pack TWOHANDS Assorted Pastel Color Highlighters'."
        elif (rand_num == 6):
            new_record = " of double AA batteries could start a medium sized car about " + str(round(standard_unit / 5400, 2)) + 
            " times."
        elif (rand_num == 7):
            new_record = " in mandalorian helmets is " + str(round(standard_unit / 1690, 2)) + 
            " helmets."
        elif (rand_num == 8):
            new_record = " is the weight of " + str(round(standard_unit / 272.155, 2)) + 
            " Minecraft Redstone Handbooks."
        elif (rand_num == 9):
            new_record = " is the weight of $" + str(round(standard_unit / 11.36, 2)) + 
            " worth of Premium Glass Nail Files..."
        elif (rand_num == 10):
            new_record = " would need " + str(round(standard_unit / 100, 2)) + 
            " human hairs to lift. This is assuming a hair can lift 100 grams, which is usualy but not always the case."

    return new_record

while True:
    for comment in reddit.subreddit("all").comments(limit = 200):
        if (check_for_units(comment, units)[2] == True):
            comment.reply(create_comment(make_units_standard(check_for_units(comments, units, opted_out))))