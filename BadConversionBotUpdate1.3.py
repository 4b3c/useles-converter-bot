#import the neccesary libraries
import random, time, praw, sys, linecache, login_info
from praw.models import Comment

#create the reddit instance
reddit = login_info.reddit

#store the words we are looking for in the comments
units = ["meters", "feet", "yards", "miles", "inches", "meter", "yard", "mile", "inch"]
units_weight = ["grams", "kilograms", "pounds", "lbs", "tons", "gram", "kilogram", "pound"]
#create a variable to store the old unit's measurement
old_unit = 0
#create a list to store comments we've already replied to
old_comments = []
#create a list to store downvoted comments we mean to delete
bad_comments = []
#create a list to store mentions we've replied to
mention_ids = []
#declare the variable we will use to count the times the while loop has repeated
x = 0
#declare a boolean that determines whether the main code runs or not
running = True
run = True
error_reported = False

#this function changes the meters into a weird random measurement and then puts it into a string that we can use to comment
def meters_to_random_unit_then_create_comment(old_unit):
    #first we get a random number between 0 and 7
    new_unit = random.randint(0, 10)

    #if the random number was 0, we convert it to toy cars
    if (new_unit == 0):
        new_record = " is  " + str(round(old_unit / 0.313, 2)) + " RTX 3090 graphics cards lined up."
        return new_record
    #if the random number was 1, we convert it to puzzles
    elif (new_unit == 1):
        new_record = " is about the length of " + str(round(old_unit / 0.6731, 2)) + " 'EuroGraphics Knittin' Kittens 500-Piece Puzzles' next to each other."
        return new_record
    #if the random number was 2, we convert it to ford f150 floor liners
    elif (new_unit == 2):
        new_record = " is the length of about " + str(round(old_unit / 1.089914, 2)) + " 'Ford F-150 Custom Fit Front FloorLiners' lined up next to each other."
        return new_record
    #if the random number was 3, we convert it to samsung fridges
    elif (new_unit == 3):
        new_record = " is the height of " + str(round(old_unit / 1.736852, 2)) + " 'Samsung Side by Side; Fingerprint Resistant Stainless Steel Refrigerators' stacked on top of each other."
        return new_record
    #if the random number was 4, we convert it to lemon squeezers
    elif (new_unit == 4):
        new_record = " is the length of like " + str(round(old_unit / 0.22098, 2)) + " 'Zulay Premium Quality Metal Lemon Squeezers' laid next to each other."
        return new_record
    #if the random number was 5, we convert it to logitech keyboards
    elif (new_unit == 5):
        new_record = " is the same as " + str(round(old_unit / 0.5, 2)) + " 'Logitech Wireless Keyboard K350s' laid widthwise by each other."
        return new_record
    #if the random number was 6, we convert it to serving spoons
    elif (new_unit == 6):
        new_record = " is the length of approximately " + str(round(old_unit / 0.2286, 2)) + " 'Wooden Rice Paddle Versatile Serving Spoons' laid lengthwise."
        return new_record
    #if the random number was 7, we convert it to harmonicas
    elif (new_unit == 7):
        new_record = " is the length of exactly " + str(round(old_unit / 0.101854, 2)) + " 'Standard Diatonic Key of C, Blues Silver grey Harmonicas' lined up next to each other."
        return new_record
    #if the random number was 8, we convert it to the world record hot dog
    elif (new_unit == 8):
        new_record = " is " + str(round(old_unit / 203.606, 2)) + " of the hot dog which holds the Guinness wold record for 'Longest Hot Dog'."
        return new_record
    #if the random number was 9, we convert it to sting
    elif (new_unit == 9):
        new_record = " is the the same distance as " + str(round(old_unit / 0.69, 2)) + " replica Bilbo from The Lord of the Rings' Sting Swords."
        return new_record
    #if the random number was 10, we convert it to a bug bite poison removers
    elif (new_unit == 10):
        new_record = " is the length of " + str(round(old_unit / 0.127, 2)) + " 'Bug Bite Thing Suction Tool - Poison Remover For Bug Bites's stacked on top of each other."
        return new_record

#this function changes the grams into a weird random measurement and then puts it into a string that we can use to comment
def grams_to_random_unit_then_create_comment(old_unit):
    #first we get a random number between 0 and 6
    new_unit = random.randint(0, 10)

    #if the random number was 0, we convert it to gold
    if (new_unit == 0):
        new_record = " of solid gold is worth about $" + str(round(old_unit * 57.91, 2)) + "."
        return new_record
    #if the random number was 1, we convert it to vegan poop
    elif (new_unit == 1):
        new_record = " of vegan poop being burned provides " + str(round(old_unit * 16.5712, 2)) + " BTU."
        return new_record
    #if the random number was 2, we convert it to SSDs
    elif (new_unit == 2):
        new_record = " is the weight of about " + str(round(old_unit / 41.10681, 2)) + " 'Kingston 120GB Q500 SATA3 2.5 Solid State Drives'."
        return new_record
    #if the random number was 3, we convert it to fake plants
    elif (new_unit == 3):
        new_record = " is the weight of literally " + str(round(old_unit / 299.08747, 2)) + " 'Velener Mini Potted Plastic Fake Green Plants'."
        return new_record
    #if the random number was 4, we convert it to pizza blankets
    elif (new_unit == 4):
        new_record = " is the same weight as " + str(round(old_unit / 639.5652, 2)) + " 'Double sided 60 inch Mermaker Pepparoni Pizza Blankets'."
        return new_record
    #if the random number was 5, we convert it to highlighters
    elif (new_unit == 5):
        new_record = " is excactly the weight of " + str(round(old_unit / 112.8311, 2)) + " '6pack TWOHANDS Assorted Pastel Color Highlighters'."
        return new_record
    #if the number was 6, we convert it to the number of double AA batteries it takes to start a car
    elif (new_unit == 6):
        new_record = " of double AA batteries could start a medium sized car about " + str(round(old_unit / 5400, 2)) + " times."
        return new_record
    #if the number was 7, we convert it to the weight of the mandalorians helmet
    elif (new_unit == 7):
        new_record = " in mandalorian helmets is " + str(round(old_unit / 1690, 2)) + " helmets."
        return new_record
    #if the number was 8, we convert it to the weight of a minecraft redstone handbook
    elif (new_unit == 8):
        new_record = " is the weight of " + str(round(old_unit / 272.155, 2)) + " Minecraft Redstone Handbooks."
        return new_record
    #if the number was 9, we convert it to the weight nail files (1 is $4.174, and weighs 0.02721554 kgs)
    elif (new_unit == 9):
        new_record = " is the weight of $" + str(round(old_unit / 11.36, 2)) + " worth of Premium Glass Nail Files..."
        return new_record
    #if the number was 10, we convert it to the weight hair can carry
    elif (new_unit == 10):
        new_record = " would need " + str(round(old_unit / 100, 2)) + " human hairs to lift. This is assuming a hair can lift 100 grams, which is usualy but not always the case."
        return new_record

#this function takes a comment and determines if it has a unit of measurement and a number associated with it
def contains_measurement(units, comment, old_comments):
    #we split the comment into a list of words
    split_string = comment.body.replace("\n", " ")
    split_string = split_string.split(" ")

    #we use a double for loop to check matching words between two lists
    for j in range(len(split_string)):
        for i in range(len(units)):
            #if the two words match it means that there is a unit of mesurement being used in this comment
            if (units[i] == split_string[j]):
                #we check if the word right before the unit of measurement is a number
                if (split_string[j - 1].isdigit() == True):
                    #if it is, we convert it to a number from a string and store the number in out "measurement" variable
                    measurement = int(split_string[j - 1])

                    #if we havn't replied to the comment
                    if (comment.id not in old_comments):
                        #if the comment was not made by a bot or an opted out person, we can still reply
                        opted_out_file = open("opted_out.txt", "r")
                        opted_out_authors = opted_out_file.read().split("\n")
                        opted_out_file.close()

                        if (str(comment.author).lower() not in opted_out_authors):
                            #basically if the unit in the comment is "meters"
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
                            #if the unit in the comment is "meter"
                            elif (i == 5):
                                old_unit = 1 * measurement
                            #if the unit in the comment is "yard"
                            elif (i == 6):
                                old_unit = 0.9144 * measurement
                            #if the unit in the comment is "mile"
                            elif (i == 7):
                                old_unit = 1609.34 * measurement
                            #if the unit in the comment is "inch"
                            elif (i == 8):
                                old_unit = 0.0254 * measurement

                            try:
                                #we try to comment the measurement, the unit, then the string after its conversion to a weird measurement
                                comment = comment.reply(str(split_string[j - 1]) + " " + str(split_string[j]) + meters_to_random_unit_then_create_comment(old_unit))
                                commented = True
                            except:
                                commented = False

                            #if we commented, we need to add the comment to our list of things we've commented on
                            if (commented == True):
                                #we open a text file and append the id of the comment we made
                                old_comments.append(comment.id)
                                my_comments_file = open("my_comments.txt", "a")
                                my_comments_file.write(comment.id + "\n")
                                my_comments_file.close()

                                return True

        for i in range(len(units_weight)):
            #if the two words match it means that there is a unit of mesurement being used in this comment
            if (units_weight[i] == split_string[j]):
                #we check if the word right before the unit of measurement is a number
                if (split_string[j - 1].isdigit() == True):
                    #if it is, we convert it to a number from a string and store the number in out "measurement" variable
                    measurement = int(split_string[j - 1])

                    #if we havn't replied to the comment
                    if (comment.id not in old_comments):
                        #if the comment was not made by a bot or an opted out person, we can still reply
                        opted_out_file = open("opted_out.txt", "r")
                        opted_out_authors = opted_out_file.read().split("\n")
                        opted_out_file.close()

                        if (str(comment.author).lower() not in opted_out_authors):
                            #if the unit in the comment is "grams"
                            if (i == 0):
                                old_unit = 1 * measurement
                            #if the unit in the comment is "kilograms"
                            elif (i == 1):
                                old_unit = 1000 * measurement
                            #if the unit in the comment is "pounds"
                            elif (i == 2):
                                old_unit = 453.592 * measurement
                            #if the unit in the comment is "lbs"
                            elif (i == 3):
                                old_unit = 453.592 * measurement
                            #if the unit in the comment is "tons"
                            elif (i == 4):
                                old_unit = 907185 * measurement
                            #if the unit in the comment is "gram"
                            if (i == 5):
                                old_unit = 1 * measurement
                            #if the unit in the comment is "kilogram"
                            elif (i == 6):
                                old_unit = 1000 * measurement
                            #if the unit in the comment is "pound"
                            elif (i == 7):
                                old_unit = 453.592 * measurement

                            try:
                                #we try to comment the measurement, the unit, then the string after its conversion to a weird measurement
                                comment = comment.reply(str(split_string[j - 1]) + " " + str(split_string[j]) + grams_to_random_unit_then_create_comment(old_unit))
                                commented = True
                            except:
                                commented = False

                            #if we commented, we need to add the comment to our list of things we've commented on
                            if (commented == True):
                                #we open a text file and append the id of the comment we made
                                old_comments.append(comment.id)
                                my_comments_file = open("my_comments.txt", "a")
                                my_comments_file.write(comment.id + "\n")
                                my_comments_file.close()

                                return True




#this function checks for downvoted comments in our text file
def check_for_bad_comments(bad_comments):
    #open the file
    my_comments_file = open("my_comments.txt", "r")
    my_comments = my_comments_file.read()
    my_comments = my_comments.split("\n")

    #iterate through the comments
    for i in my_comments:
        try:
            comment = reddit.comment(i)
            #check if the comment got downvotes
            if (comment.score < 0):
                #if it was downvoted, delete it
                comment.delete()
                bad_comments.append(comment.id)
            elif (comment.score > 10):
                bad_comments.append(comment.id)
            if (time.time() - comment.created_utc > 10800):
                bad_comments.append(comment.id)
        except:
            pass

    my_comments_file.close()

    #return the updated list of bad comments, and all comments
    return bad_comments, my_comments

#this function rewrites our text file with only the good comments
def rewrite_text_file(bad_comments, my_comments):
    #remove all deleted comments from a list of all comments
    for i in bad_comments:
        if (i in my_comments):
            my_comments.remove(i)

    #try removing empty space
    for i in my_comments:
        if ("" in my_comments):
            my_comments.remove("")

    #rewrite the text file without the bad comments
    my_comments_file = open("my_comments.txt", "w")
    #rewrite the actual file
    for i in my_comments:
        my_comments_file.write(str(i) + "\n")
    my_comments_file.close()

#this function checks comments you give it for  people opting in or out and does it automatically
def opt_in_and_out(comment):
    #first we open the file and get all the authors
    opted_out_file = open("opted_out.txt", "r")
    opted_out_authors = opted_out_file.read().split("\n")
    opted_out_file.close()

    #we check if the comment contains "opt out"
    if ("opt out" in comment.body.lower()):
        #then we check if the person is opted out already
        if (comment.author in opted_out_authors):
            #if they are, we tell them
            comment.reply("You are already opted out. (If you wanted to opt in, you can comment 'u/useles-converter-bot opt in')")
        #if they aren't opted out
        elif (comment.author not in opted_out_authors):
            #we add them to the file
            opted_out_file = open("opted_out.txt", "a")
            opted_out_file.write(str(comment.author) + "\n")
            opted_out_file.close()
            #and we tell them they have been opted out
            comment.reply("You have been opted out, I will no longer reply to your comments, (If you change your mind, you can comment 'u/useles-converter-bot opt in')")
        return True
            
    #we do the same thing but for opting in
    elif ("opt in" in comment.body.lower()):
        #if they are opted out
        if (comment.author in opted_out_authors):
            #we remove them from the opted out list
            opted_out_authors.remove(comment.author)
            opted_out_file = open("opted_out.txt", "w")
            #then we rewrite the file
            for i in opted_out_authors:
                opted_out_file.write(str(i) + "\n")
            opted_out_file.close()
            #we reply to them to let them know 
            comment.reply("You have been opted back in, I will now reply to your comments when I see them")
        #if they were never opted out
        elif (comment.author not in opted_out_authors):
            #we tell them
            comment.reply("You aren't opted out. I will try to reply to your comments when I see them. If you would like to opt out please use 'opt out' instead.")
        return True

#this function checks the inbox
def check_inbox():
    #get 25 unread items
    for item in reddit.inbox.unread(limit = 25):
        #if the item is a comment
        if (isinstance(item, Comment)):
            #and the comment says good bot
            if (item.body.lower() == "good bot" or item.body.lower() == "good bot."):
                #pick a random thank you message
                reply_chance = random.randint(0, 2)
                if (reply_chance == 0):
                    item.reply("thank you :)")
                elif(reply_chance == 1):
                    item.reply("thanks :)")
                

            #and the comment says useless bot, or useless
            elif (item.body.lower() == "useless bot" or item.body.lower == "useless"):
                #pick a random number to determine whether we reply
                comment = item.reply("that's the- that's the point :/")
                my_comments_file = open("my_comments.txt", "a")
                my_comments_file.write(comment.id + "\n")
                my_comments_file.close()
                

            #and the comment says bad bot
            elif (item.body.lower() == "bad bot" or item.body.lower() == "bad bot."):
                #pick a random number to decide whether to reply or not
                reply_chance = random.randint(0, 10)
                if (reply_chance < 3):
                    comment = item.reply("I'm just doing my job, and that is to give out useless information :(")
                    my_comments_file = open("my_comments.txt", "a")
                    my_comments_file.write(comment.id + "\n")
                    my_comments_file.close()
                

            #and the comment says lmao or lmfao
            elif (item.body.lower() == "lmao" or item.body.lower() == "lmfao"):
                #pick a random number to decide whether to reply or not
                reply_chance = random.randint(0, 10)
                if (reply_chance < 3):
                    item.reply("i'm glad i made you laugh, please pick up your butt before someone steals it")
                    print("I replied to a 'lmao': " + str(item.submission.permalink))
                    reddit.redditor("-i-hate-this-place-").message("Replied to a 'lmao':", item.submission.permalink)
               

            #if the comment is contradicting the username miss-spelling
            elif ("useles" in item.body.lower() and "spell" in item.body.lower()):
                comment = item.reply("""From the words you used, it seems like you are bashing the spelling of my u/. I wanted to be useless-converter-bot 
                    because I wanted to be like a useless version of converter-bot, however, Reddit has a username character limit of 20 characters 
                    and so I had to remove one character and that S seemed like the best one to remove, as there is a second S to make up for it.""")
                #message me so I know
                reddit.redditor("-i-hate-this-place-").message("Replied to a 'useles':", comment.submission.permalink)
                

            #we run the function that opts people in and out
            elif ("opt" in item.body.lower()):
                opt_in_and_out(item)

            #otherwise we look for measurements to convert
            else:
                contains_measurement(units, item, old_comments)

    #mark it as read
    reddit.inbox.mark_all_read()

#this fuction checks mentions
def check_mentions(running):
    #open the text file where we save mentions so we don't reply multiple times to them
    mention_comments_file = open("mention_comments.txt", "r")
    mention_ids = mention_comments_file.read().split("\n")
    mention_comments_file.close()

    #we get the last 10 mentions
    for mention in reddit.inbox.mentions(limit = 10):
        #check if we've seen them already or not
        if (mention.id not in mention_ids):
            #if "stop" is in a comment by me, stop the bot            
            if ("stop" in mention.body.lower()):
                if (mention.author == "-i-hate-this-place-"):
                    if (running == True):
                        mention.reply("Stopping. . .")
                        mention_ids.append(mention.id)
                        print("Stopping. . .")
                        running = False
                    elif (running == False):
                        mention.reply("I was already stopped.")
                        mention_ids.append(mention.id)
                        print("I was already stopped.")

            #if "start" is in a comment by me, start the bot
            elif ("start" in mention.body.lower()):
                if (mention.author == "-i-hate-this-place-"):
                    if (running == False):
                        mention.reply("Starting. . .")
                        mention_ids.append(mention.id)
                        print("Starting. . .")
                        running = True
                    elif (running == True):
                        mention.reply("I was already running.")
                        print("I was already runnning.")
                        mention_ids.append(mention.id)

            #if "status" is in a comment by me, tell me if the bot ir running or not
            elif ("status" in mention.body.lower()):
                if (mention.author == "-i-hate-this-place-"):
                    if (running == True):
                        mention.reply("Running")
                        mention_ids.append(mention.id)
                        print("Running")
                    elif (running == False):
                        mention.reply("Not running")
                        mention_ids.append(mention.id)
                        print("Not running")

            #if "opt" is in a comment, run the opt in and out function
            elif ("opt" in mention.body.lower()):
                if (opt_in_and_out(mention) == True):
                    mention_ids.append(mention.id)

            #otherwise, check for a measurement
            else:
                #check the very comment
                if (contains_measurement(units, mention, old_comments) != True):
                    try:
                        #if not, check the one above it
                        if (contains_measurement(units, mention.parent(), old_comments) == True):
                            mention.reply("Thanks for showing me this hehe")
                            mention_ids.append(mention.id)
                        #if theres still nothing, reply that nothing was found
                        else:
                            mention.reply("I couldn't find the measurement you wanted me to convert.")
                            mention_ids.append(mention.id)
                    #if it falls in none of the options, print it and remove it from unread mentions
                    except:
                        print(str(mention.body))
                        mention_ids.append(mention.id)

    #try removing empty space
    for i in mention_ids:
        if ("" in mention_ids):
            mention_ids.remove("")

    #try removing things that aren't comment ids
    for i in mention_ids:
        if ("\n" in mention_ids):
            mention_ids.remove("\n")

    #reduce the size of the text file
    while (len(mention_ids) > 20):
        del mention_ids[0]

    #rewrite the file
    mention_comments_file = open("mention_comments.txt", "w")
    for i in (mention_ids):
        mention_comments_file.write(str(i) + "\n")
    mention_comments_file.close()

    return running

#this function is one i stole to get the exception whenever i need it
def print_exception():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return ('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

#now that everything is defined, we can start the main loop
print("Starting. . .")
while True:
    try:
        #first we get 200 comments from r/all, and iterate through them all
        for comment in reddit.subreddit("all").comments(limit = 200):
            contains_measurement(units, comment, old_comments)

        #everytime we loop, we increase this variable
        x = x + 1
        #and every 150 times we loop we run this part of the code
        if (x >= 150):
            print("Checking for bad/old comments:", end = " ")
            #check for comments that were downvoted
            rewrite_list = check_for_bad_comments(bad_comments)

            #delete them and rewrite the text file
            rewrite_text_file(rewrite_list[0], rewrite_list[1])
            print("[Done]")

            #we check our inbox
            check_inbox()

            #set x to zero so we can count to 100 again
            x = 0

            #reset the old comments variable
            old_comments = [old_comments[-1]]

        #if mentions say to stop running, stay in this loop instead of commenting
        run = check_mentions(run)

        #if i turn the bot off, it stays in this loop
        while (run == False):
            time.sleep(30)
            run = check_mentions(run)

        #if we escape the not error loop, it means theres no error
        error_reported = False

    #if our attemps at running fail
    except:
        #and the reason is not a rate limit or a ban
        if ("HTTP" not in print_exception() and "ratelimit" not in print_exception().lower()):
            #print the reason
            print(print_exception())

            #report the error
            try:
                if (error_reported == False):
                    reddit.redditor("-i-hate-this-place-").message("There was an error with useles-converter-bot:", "Here is the error: " + print_exception())
                    error_reported = True

            #if we can't report the error, the wifi is off
            except:
                print("The wifi is probably off")
        time.sleep(60)
