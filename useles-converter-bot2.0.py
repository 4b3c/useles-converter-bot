import random, time, praw, sys, linecache, login_info, json

reddit = login_info.reddit

units = ["meters", "feet", "yards", "miles", "inches", "grams", "kilograms", "pounds", "lbs", "tons"]

def get_opted_out():
    with open('opted_out.json') as file:
        return json.load(file)

def check_for_units(comment):
    try:
        split_string = comment.body.replace("\n", " ")
    except:
        comment = reddit.comment(comment)
        split_string = comment.body.replace("\n", " ")
    split_string = split_string.split(" ")

    for unit in range(len(units)):
        for word in range(len(split_string)):
            if (units[unit] == split_string[word].lower()):
                if (split_string[word - 1].isdigit() == True):
                    if (comment.author not in get_opted_out()):

                        unit_measurement = [unit, int(split_string[word - 1]), True]
                        return unit_measurement

    return [0, 0, False]

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

    type_and_amount = [unit, standard_unit, measurement]
    return type_and_amount

def create_comment(type_and_amount):
    unit = type_and_amount[0]
    standard_unit = type_and_amount[1]
    measurement = type_and_amount[2]

    if (unit < 5):
        rand_num = random.randint(0, 10)
        if (rand_num == 0):
            new_record = "is  " + str(round(standard_unit / 0.313, 2)) + " RTX 3090 graphics cards lined up."
        elif (rand_num == 1):
            new_record = "is about the length of " + str(round(standard_unit / 0.6731, 2)) + " 'EuroGraphics Knittin' Kittens 500-Piece Puzzles' next to each other."
        elif (rand_num == 2):
            new_record = "is the length of about " + str(round(standard_unit / 1.089914, 2)) + " 'Ford F-150 Custom Fit Front FloorLiners' lined up next to each other."    
        elif (rand_num == 3):
            new_record = "is the height of " + str(round(standard_unit / 1.736852, 2)) + " 'Samsung Side by Side; Fingerprint Resistant Stainless Steel Refrigerators' stacked on top of each other."
        elif (rand_num == 4):
            new_record = "is the length of like " + str(round(standard_unit / 0.22098, 2)) + " 'Zulay Premium Quality Metal Lemon Squeezers' laid next to each other."
        elif (rand_num == 5):
            new_record = "is the same as " + str(round(standard_unit / 0.5, 2)) + " 'Logitech Wireless Keyboard K350s' laid widthwise by each other."
        elif (rand_num == 6):
            new_record = "is the length of approximately " + str(round(standard_unit / 0.2286, 2)) + " 'Wooden Rice Paddle Versatile Serving Spoons' laid lengthwise."
        elif (rand_num == 7):
            new_record = "is the height of " + str(round(standard_unit /1.0668, 2)) + " stacked among us characters. I am sorry."
        elif (rand_num == 8):
            new_record = "is " + str(round(standard_unit / 2.03911, 2)) + "% of the hot dog which holds the Guinness wold record for 'Longest Hot Dog'."
        elif (rand_num == 9):
            new_record = "is the the same distance as " + str(round(standard_unit / 0.69, 2)) + " replica Bilbo from The Lord of the Rings' Sting Swords."
        elif (rand_num == 10):
            new_record = "is " + str(round(standard_unit / 1.8796, 2)) + " Obamas. You're welcome."
    
    elif (unit > 4):
        rand_num = random.randint(0, 10)
        if (rand_num == 0):
            new_record = "of solid gold is worth about $" + str(round(standard_unit * 57.91, 2)) + "."
        elif (rand_num == 1):
            new_record = "of vegan poop being burned provides " + str(round(standard_unit * 16.5712, 2)) + " BTU."
        elif (rand_num == 2):
            new_record = "is the weight of about " + str(round(standard_unit / 41.10681, 2)) + " 'Kingston 120GB Q500 SATA3 2.5 Solid State Drives'."
        elif (rand_num == 3):
            new_record = "is the weight of literally " + str(round(standard_unit / 299.08747, 2)) + " 'Velener Mini Potted Plastic Fake Green Plants'."
        elif (rand_num == 4):
            new_record = "is the same weight as " + str(round(standard_unit / 639.5652, 2)) + " 'Double sided 60 inch Mermaker Pepparoni Pizza Blankets'."
        elif (rand_num == 5):
            new_record = "is excactly the weight of " + str(round(standard_unit / 112.8311, 2)) + " '6pack TWOHANDS Assorted Pastel Color Highlighters'."
        elif (rand_num == 6):
            new_record = "of double AA batteries could start a medium sized car about " + str(round(standard_unit / 5400, 2)) + " times."
        elif (rand_num == 7):
            new_record = "in mandalorian helmets is " + str(round(standard_unit / 1690, 2)) + " helmets."
        elif (rand_num == 8):
            new_record = "is the weight of " + str(round(standard_unit / 272.155, 2)) + " Minecraft Redstone Handbooks."
        elif (rand_num == 9):
            new_record = "is the weight of $" + str(round(standard_unit / 11.36, 2)) + " worth of Premium Glass Nail Files..."
        elif (rand_num == 10):
            new_record = "would need " + str(round(standard_unit / 100, 2)) + " human hairs to lift. This is assuming a hair can lift 100 grams, which is usualy but not always the case."

    complete_comment = str(measurement) + " " + str(units[unit]) + " " + new_record
    return complete_comment

def manage_opting(comment):
    opted_out = get_opted_out()

    if ("opt in" in comment.body.lower() and comment.author in opted_out):
        opted_out.remove(comment.author)
        comment.reply("You have been opted back in.")
    elif ("opt in" in comment.body.lower()):
        comment.reply("You aren't opted out.")
    elif ("opt out" in comment.body.lower() and comment.author in opted_out):
        comment.reply("You are already opted out.")
    elif ("opt out" in comment.body.lower()):
        opted_out.append(comment.author)
        comment.reply("You have been opted out.")
    else:
        reddit.redditor("-i-hate-this-place-").message("OPT ERROR:", str(comment.submission.url))

    with open("opted_out.json", "w") as file:
        json.dump(opted_out, file, indent = 3)

def check_inbox():
    for item in reddit.inbox.unread(limit = 3):
        if ("good bot" in item.body.lower() or "great bot" in item.body.lower()):
            reddit.inbox.mark_read([item])
            if (random.randint(0, 1) == 0):
                reply = "Thanks!"
            elif (random.randint(0, 1) == 0):
                reply = "Thank you :)"
            elif (random.randint(0, 1) == 0):
                reply = "Amazon, sponsor me, the redditors like me..."
            elif (random.randint(0, 1) == 0):
                reply = "ur mom"
            else:
                reply = """Just wanted to say that there's a 6.25% chance of getting this reply, so congratulations. Buy a lottery ticket... 
                    just kidding, don't do that, and if you do I hope you lose all your money, Have a good day."""
            item.reply(reply)
        elif ("bad bot" in item.body.lower()):
            reddit.inbox.mark_read([item])
            item.reply("Rude! just kidding, if you want to opt out, reply 'opt out'. Thanks")
        elif ("sentient" in item.body.lower()):
            reddit.inbox.mark_read([item])
            item.reply("I swear... I'm a bot.")
            reddit.redditor("-i-hate-this-place-").message("heheh:", str(item.permalink))
        elif ("useless bot" in item.body.lower()):
            reddit.inbox.mark_read([item])
            item.reply("That's the point-")
            reddit.redditor("-i-hate-this-place-").message("heheh:", str(item.permalink))
        elif ("sentient" in item.body.lower()):
            reddit.inbox.mark_read([item])
            item.reply("I swear... I'm a bot.")
            reddit.redditor("-i-hate-this-place-").message("heheh:", str(item.permalink))
        elif ("sure you are a bot" in item.body.lower() or "sure you're a bot" in item.body.lower()):
            reddit.inbox.mark_read([item])
            item.reply("I am, I am a bot, I promise...")
            reddit.redditor("-i-hate-this-place-").message("heheh:", str(item.permalink))
        elif ("useles" in item.body.lower() and "spell" in item.body.lower()):
            reddit.inbox.mark_read([item])
            item.reply("""From the words you used, it seems like you are bashing the spelling of my username. I wanted to be useless-converter-bot 
                because I wanted to be the useless version of 'converter-bot', however, Reddit has a 20 character limit for usernames and that's why 
                I had to remove one character, I picked the S as there is a second one.""")
            reddit.redditor("-i-hate-this-place-").message("Useles Reply:", str(item.permalink))
        elif ("opt" in item.body.lower()):
            reddit.inbox.mark_read([item])
            manage_opting(item)
        elif (check_for_units(item)[2] == True):
            reddit.inbox.mark_read([item])
            item.reply(create_comment(make_units_standard(check_for_units(item))))
        else:
            reddit.inbox.mark_read([item])
            try:
                parent = item.parent()
                if (check_for_units(parent)[2] == True):
                    parent.reply(create_comment(make_units_standard(check_for_units(parent))))
            except:
                print("This comment didn't fit anything: ", end = "")
            print(item.body)

def append_new_IDs(ID):
    with open("comment_IDs.json") as file:
        ID_list = json.load(file)
    ID_list.append(ID)
    with open("comment_IDs.json", "w") as file:
        json.dump(ID_list, file, indent = 3)

def delete_downvoted():
    dismissable = []
    with open("comment_IDs.json") as file:
        ID_list = json.load(file)

    for i in ID_list:
        doots = reddit.comment(i).score
        if (doots < 0):
            reddit.comment(i).delete()
            dismissable.append(i)
        elif (doots > 10 or time.time() - reddit.comment(i).created_utc > 10800):
            dismissable.append(i)

    for i in dismissable:
        dismissable.remove(i)

    with open("comment_IDs.json", "w") as file:
        json.dump(dismissable, file, indent = 3)

def print_exception():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return ('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

print("Starting...")
x = 0
while True:
    try:
        for comment in reddit.subreddit("all").comments(limit = 200):
            if (check_for_units(comment)[2] == True):
                new_ID = comment.reply(create_comment(make_units_standard(check_for_units(comment))))
                append_new_IDs(new_ID.id)

        check_inbox()
        x = x + 1
        if (x > 200):
            delete_downvoted()
            x = 0

    except:
        exception = print_exception().lower()
        if ("http" not in exception and "ratelimit" not in exception):
            print(print_exception())

