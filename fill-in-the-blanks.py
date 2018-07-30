# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

# sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
# adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
# don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
# tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

s_model = '''Model ___1___ is designed from the ground up to be the safest, 
most exhilarating sedan on the road. With unparalleled performance 
delivered through ___2___'s unique, all-electric powertrain, Model 
___1___ accelerates from 0 to ___3___ mph in as little as 2.5 seconds. 
Model ___1___ comes with Autopilot capabilities designed to make your 
highway driving not only safer, but stress free. The Model ___1___ is the 
best sedan in the entire ___4___'''
x_model = '''Model ___1___ is the safest, quickest, and most capable sport 
utility vehicle in history. Designed as a family car without compromise, 
Model ___1___ comes standard with all-wheel drive, ample seating for up 
to seven adults, standard active safety features, and up to ___2___ miles 
of range on a single charge. And it's the quickest SUV in production, 
capable of accelerating from zero to ___3___ miles per hour in 2.9 
seconds. The Model ___1___ is the best utility vehicle in the entire 
___4___'''
e_model = '''Designed to attain the highest safety ratings in every 
category, Model ___1___ achieves ___2___ miles of range while starting 
at only $___3___ before incentives. The Model ___1___ is the best 
sedan in the entire ___4___'''

s_answers_list_that_uses_its_values_to_fill_in_the_blanks = ["s", 'tesla', "60", 'world']
x_answers_list_that_uses_its_values_to_fill_in_the_blanks = ["x", "295", "60", 'world']
e_answers_list_that_uses_its_values_to_fill_in_the_blanks = ["e", "220", "35000", 'world']
user_input = input("What car would you like to drive? Model X, S, or E? ")

# this is the start of the game and when the game begins this is the first operation
print(user_input)


# this is the function that does the parsing of the user answer and replaces the text of the blank with the actual answer
def play_game(ml_string, parts_of_speech, replaced_text):
    """
    :param ml_string: this is the check space as it moves through the paragraph
    :param parts_of_speech: the value that was provided from the user
    :param replaced_text: once it is correct, this is what text is put into the return to the user
    """
    replaced = []
    ml_string = ml_string.split(' ')
    for parse in ml_string:
        parse = parse.replace(parts_of_speech, replaced_text)
        replaced.append(parse)
    replaced = " ".join(replaced)
    return replaced

# this is the core operating function
def quiz_function(model, answers):
    num_tries = 5
    current_blank = 0
    number_of_blanks = 4
    new_paragraph = model
    while num_tries != 0 and current_blank < number_of_blanks:  # as long as the 5 tries have not run out, this code is run to prompt the user for the answer and the answer is checked to see if it is right
        print (new_paragraph + "\nYou have " + str(num_tries) + " tries on each blank. \n Fill in the blanks!")
        answer_input = input("What is the answer for blank number " + str(current_blank + 1) + "?")
        if answer_input.lower() == answers[current_blank]:
            print("That's right!")
            new_paragraph = play_game(new_paragraph, "___" + str(current_blank + 1) + "___", answer_input)
            num_tries = 5
            current_blank += 1
        else:  # if all 5 tries are spent on the question the game is over and the user has to start all over again
            num_tries -= 1
    if num_tries == 0:
        print("You ran out of tries. Game Over")
    else:s_answers_list_that_uses_its_values_to_fill_in_the_blanks
    print(new_paragraph + "\nCongratulations, you WON!!")

if user_input in 'Ss':
    quiz_function(s_model, s_answers_list_that_uses_its_values_to_fill_in_the_blanks)
elif user_input in 'Xx':
    quiz_function(x_model, x_answers_list_that_uses_its_values_to_fill_in_the_blanks)
elif user_input in 'Ee':
    quiz_function(e_model, e_answers_list_that_uses_its_values_to_fill_in_the_blanks)
