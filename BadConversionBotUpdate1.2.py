#import the neccesary libraries
import random, time, praw, sys, linecache, login_info
from praw.models import Comment

#create the reddit instance
reddit = login_info.reddit

#store the words we are looking for in the comments
units = ["meters", "feet", "yards", "miles", "inches"]
units_weight = ["grams", "pounds", "lbs", "tons"]
#create a variable to store the old unit's measurement
old_unit = 0
#create a list to store comments we've already replied to
old_comments = []
#create a list to store downvoted comments we mean to delete
bad_comments = []
#create a list to store replies to replies
unread = []
#create a list to store mentions we've replied to
mention_ids = []
#declare the variable we will use to count the times the while loop has repeated
x = 0
#declare a boolean that determines whether the main code runs or not
running = True
run = True
error_reported = False

#this function takes our unit and our measurement and converts it to meters
def convert_to_meters(i, measurement):
    #basically if the unit in the comment contained "meter"
    if (i == 0):
        if (split_string[j][3] == "e"):
            old_unit = 1 * measurement
        elif ("kilometer" in split_string[j]):
            old_unit = 1000 * measurement
        elif ("centimeter" in split_string[j]):
            old_unit = 0.01 * measurement
        elif ("millimeter" in split_string[j]):
            old_unit = 0.0001 * measurement
    #if the unit in the comment contained "feet"
    elif (i == 1):
        old_unit = 0.3048 * measurement
    #if the unit in the comment contained "yard"
    elif (i == 2):
        old_unit = 0.9144 * measurement
    #if the unit in the comment contained "mile"
    elif (i == 3):
        old_unit = 1609.34 * measurement
    #if the unit in the comment contained "inch"
    elif (i == 4):
        old_unit = 0.0254 * measurement
    else:
        old_unit = 0

    #we return the measurement of whatever the comment said but in meters
    return old_unit

#this function changes the meters into a weird random measurement and then puts it into a string that we can use to comment
def meters_to_random_unit_then_create_comment(old_unit):
    #first we get a random number between 0 and 4, the 4 is of no use to us but it helps so we dont over-comment
    new_unit = random.randint(0, 7)

    #if the random number was 0, we convert it to toy cars
    if (new_unit == 0):
        new_record = " is about the length of " + str(round(old_unit / 0.16002, 2)) + " 'Sian FKP3 Metal Model Toy Cars with Light and Sound' lined up"
        return new_record
    #if the random number was 1, we convert it to puzzles
    elif (new_unit == 1):
        new_record = " is about the length of " + str(round(old_unit / 0.6731, 2)) + " 'EuroGraphics Knittin' Kittens 500-Piece Puzzles' next to each other"
        return new_record
    #if the random number was 2, we convert it to ford f150 floor liners
    elif (new_unit == 2):
        new_record = " is the length of about " + str(round(old_unit / 1.089914, 2)) + " 'Ford F-150 Custom Fit Front FloorLiners' lined up next to each other"
        return new_record
    #if the random number was 3, we convert it to samsung fridges
    elif (new_unit == 3):
        new_record = " is the height of literally " + str(round(old_unit / 1.736852, 2)) + " 'Samsung Side by Side; Fingerprint Resistant Stainless Steel Refrigerators' stacked on top of each other"
        return new_record
    #if the random number was 4, we convert it to lemon squeezers
    elif (new_unit == 4):
        new_record = " is the length of like " + str(round(old_unit / 0.22098, 2)) + " 'Zulay Premium Quality Metal Lemon Squeezers' laid next to each other"
        return new_record
    #if the random number was 5, we convert it to logitech keyboards
    elif (new_unit == 5):
        new_record = " is the length of approximately " + str(round(old_unit / 0.5, 2)) + " 'Logitech Wireless Keyboard K350s' laid widthwise by each other"
        return new_record
    #if the random number was 6, we convert it to serving spoons
    elif (new_unit == 6):
        new_record = " is the length of approximately " + str(round(old_unit / 0.2286, 2)) + " 'Wooden Rice Paddle Versatile Serving Spoons' laid lengthwise"
        return new_record
    #if the random number was 7, we convert it to harmonicas
    elif (new_unit == 7):
        new_record = " is the length of exactly " + str(round(old_unit / 0.101854, 2)) + " 'Standard Diatonic Key of C, Blues Silver grey Harmonicas' lined up next to each other"
        return new_record


#this function takes a comment and determines if it has a unit of measurement and a number associated with it
def contains_measurement(units, comment):
    #we split the comment into a list of words
    split_string = comment.body.replace("\n", " ")
    split_string = split_string.split(" ")

    #we use a double for loop to check matching words between two lists
    for i in range(len(units)):
        for j in range(len(split_string)):
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

                            #basically if the unit in the comment contained "meter"
                            if (i == 0):
                                if (split_string[j][3] == "e"):
                                    old_unit = 1 * measurement
                                elif ("kilometer" in split_string[j]):
                                    old_unit = 1000 * measurement
                                elif ("centimeter" in split_string[j]):
                                    old_unit = 0.01 * measurement
                                elif ("millimeter" in split_string[j]):
                                    old_unit = 0.0001 * measurement
                            #if the unit in the comment contained "feet"
                            elif (i == 1):
                                old_unit = 0.3048 * measurement
                            #if the unit in the comment contained "yard"
                            elif (i == 2):
                                old_unit = 0.9144 * measurement
                            #if the unit in the comment contained "mile"
                            elif (i == 3):
                                old_unit = 1609.34 * measurement
                            #if the unit in the comment contained "inch"
                            elif (i == 4):
                                old_unit = 0.0254 * measurement
                            else:
                                old_unit = 0

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


#this function checks for downvoted comments in our text file
def check_for_bad_comments(bad_comments):
    #open the file
    my_comments_file = open("my_comments.txt", "r")
    my_comments = my_comments_file.read()
    my_comments = my_comments.split("\n")

    print("Checking for bad comments...")
    #iterate through the comments
    for i in my_comments:
        try:
            comment = reddit.comment(i)
            #check if the comment got downvotes
            if (comment.score < 1):
                #if it was downvoted, delete it
                comment.delete()
                print("Deleted a comment")
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
    for i in my_comments:
        my_comments_file.write(str(i) + "\n")
    my_comments_file.close()

#this function checks the inbox
def check_inbox():
    unread = []
    #get 35 unread items
    for item in reddit.inbox.unread(limit = 50):
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
                unread.append(item)

            #and the comment says useless bot, or useless
            elif (item.body.lower() == "useless bot" or item.body.lower == "useless"):
                #pick a random number to determine whether we reply
                item.reply("that's the- that's the point :/")
                unread.append(item)

            #and the comment says bad bot
            elif (item.body.lower() == "bad bot" or item.body.lower() == "bad bot."):
                #pick a random number to decide whether to reply or not
                reply_chance = random.randint(0, 10)
                if (reply_chance < 3):
                    item.reply("I'm just doing my job, and that is to give out useless information :(")
                unread.append(item)

            #and the comment says lmao or lmfao
            elif (item.body.lower() == "lmao" or item.body.lower() == "lmfao"):
                #pick a random number to decide whether to reply or not
                reply_chance = random.randint(0, 10)
                if (reply_chance < 3):
                    item.reply("i'm glad i made you laugh, please pick up your butt before someone steals it")
                    print("I replied to a 'lmao': " + item.submission.url)
                    reddit.redditor("Abe_rah_ham_liyn_con").message("Replied to a 'lmao':", item.submission.url)
                unread.append(item)

            #and the comment critizes our spelling
            elif ("spell" in item.body.lower() and "useles" in item.body.lower()):
                item.reply("www.reddit.com/user/useles-converter-bot/comments/obemcc/smh/")
                print("I replied to a 'criticize': " + item.submission.url)
                unread.append(item)
                reddit.redditor("Abe_rah_ham_liyn_con").message("Replied to a 'criticize':", item.submission.url)

    reddit.inbox.mark_read(unread)

#this fuction checks mentions
def check_mentions(running):
    #open the text file where we
    mention_comments_file = open("mention_comments.txt", "r")
    mention_ids = mention_comments_file.read()
    mention_ids = mention_ids.split("\n")
    mention_comments_file.close()

    for mention in reddit.inbox.mentions(limit = 10):
        if (mention.id not in mention_ids):
            mention_ids.append(mention.id)
            
            if ("stop" in mention.body.lower()):
                if (mention.author == "Abe_rah_ham_liyn_con"):
                    if (running == True):
                        mention.reply("Stopping. . .")
                        print("Stopping. . .")
                        running = False
                    elif (running == False):
                        mention.reply("I was already stopped.")
                        print("I was already stopped.")

            elif ("start" in mention.body.lower()):
                if (mention.author == "Abe_rah_ham_liyn_con"):
                    if (running == False):
                        mention.reply("Starting. . .")
                        print("Starting. . .")
                        running = True
                    elif (running == True):
                        mention.reply("I was already running.")
                        print("I was already runnning.")

            elif ("status" in mention.body.lower()):
                if (mention.author == "Abe_rah_ham_liyn_con"):
                    if (running == True):
                        mention.reply("Running")
                        print("Running")
                    elif (running == False):
                        mention.reply("Not running")
                        print("Not running")

            elif ("opt out" in mention.body.lower()):
                opted_out_file = open("opted_out.txt", "a")
                opted_out_file.write(str(mention.author) + "\n")
                opted_out_file.close()
                mention.reply("You have been opted out, I will no longer reply to your comments, (If you change your mind, you can comment 'u/useles-converter-bot opt in')")
            
            elif ("opt in" in mention.body.lower()):
                opted_out_file = open("opted_out.txt", "r")
                opted_out_authors = opted_out_file.read().split("\n")
                if (mention.author in opted_out_authors):
                    opted_out_authors.remove(mention.author)
                    mention.reply("You have been opted back in, I will now reply to your comments when I see them")
                elif (mention.author not in opted_out_authors):
                    mention.reply("You aren't opted out. I will try to reply to your comments when I see them. If you would like to opt out please use 'opt out' instead.")

                opted_out_file.close()
                opted_out_file = open("opted_out.txt", "w")
                for i in opted_out_authors:
                    opted_out_file.write(str(i) + "\n")

                opted_out_file.close()

            else:
                if (contains_measurement(units, mention) != True):
                    try:
                        if (contains_measurement(units, mention.parent()) == True):
                            mention.reply("Thanks for showing me this hehe")
                        else:
                            mention.reply("I couldn't find the measurement you wanted me to convert.")
                    except:
                        pass

    #try removing empty space
    for i in mention_ids:
        if ("" in mention_ids):
            mention_ids.remove("")

    #try removing things that aren't comment ids
    for i in mention_ids:
        if ("\n" in mention_ids):
            mention_ids.remove("\n")

    mention_comments_file = open("mention_comments.txt", "w")
    for i in (mention_ids):
        mention_comments_file.write(str(i) + "\n")
    mention_comments_file.close()

    return running

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
            contains_measurement(units, comment)

        #everytime we loop, we increase this variable
        x = x + 1
        #and every 150 times we loop we run this part of the code
        if (x >= 150):
            #check for comments that were downvoted
            rewrite_list = check_for_bad_comments(bad_comments)

            #delete them and rewrite the text file
            rewrite_text_file(rewrite_list[0], rewrite_list[1])
            print("We checked all the comments.")

            #we check our inbox
            check_inbox()

            #set x to zero so we can count to 100 again
            x = 0

            #reset the old comments variable
            old_comments = [old_comments[-1]]

        #if mentions say to stop running, stay in this loop instead of commenting
        run = check_mentions(run)

        while (run == False):
            time.sleep(30)
            run = check_mentions(run)

        error_reported = False
    except:
        print(print_exception())
        try:
            if (error_reported == False):
                reddit.redditor("Abe_rah_ham_liyn_con").message("There was an error with useles-converter-bot:", "Here is the error: " + print_exception())
                error_reported = True
        except:
            pass
        time.sleep(60)
