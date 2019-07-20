import numpy as np
import random
import ngender
import name_dictionary as nd

lower_name_boys = [names.lower() for names in nd.boys]
lower_name_girls = [names.lower() for names in nd.girls]
# need to add feedback system for detectors

# change dictionaries here
# if lexicons are kids,junior,high_school,university,Master,Native_speaker
kids = {1:'a', 2:'b', 3:'c',4:'d',5:'e',6:"f",7:'g',8:"h",9:"i",10:"j",11:"k"}
junior = {1:'a', 2:'b', 3:'c',4:'d',5:'e',6:"f",7:'g',8:"h",9:"i",10:"j",11:"k"}
high_school = {1:'a', 2:'b', 3:'c',4:'d',5:'e',6:"f",7:'g',8:"h",9:"i",10:"j",11:"k"}
university = {1:'a', 2:'b', 3:'c',4:'d',5:'e',6:"f",7:'g',8:"h",9:"i",10:"j",11:"k"}
Master = {1:'a', 2:'b', 3:'c',4:'d',5:'e',6:"f",7:'g',8:"h",9:"i",10:"j",11:"k"}
Native_speaker = {1:'a', 2:'b', 3:'c',4:'d',5:'e',6:"f",7:'g',8:"h",9:"i",10:"j",11:"k"}

# message for user if they entered wrong for level
level_enter_correct = "Okay~ so let's start the quiz to see if this level may fits you well"
#dictionary list
lexicon_list = [kids,junior,high_school,university,Master,Native_speaker]
lexicon_list_No = [1,2,3,4,5,6]

#quiz times, final results, correct times, wrong times
times = 0
result = False
correct = 0
wrong = 0
gender_quiz = str()


# welcome speech
print("Welcome to easy reading! Please let me know who you are and which level you are now!")
# get user name
name = input("\nPlease enter your name here: ")

# Chinese Name only
if '\u4e00' <= name <= '\u9fa0':

    gender = ngender.guess(name)[0]
    if gender == 'male':
        gender = 'boy'
    else:
        gender = 'girl'
        
    flag = False
    while flag == False:
        question = "Are you a " +gender+" ?(Y/N)"
        gender_confirmation = input(question)
        if gender_confirmation.lower() == 'y' or gender_confirmation.lower() == 'n':
            flag = True
        else:
            flag = False
            print('please re-enter Y / N, thanks')
# for english name
elif name.isalpha():
    if name in lower_name_boys:
        gender_quiz = input("Are you a boy?: Y/N ")
        if gender_quiz =='Y':
            gender = 'boy'
        else:
            gender = 'girl'
    else:
        gender_quiz = input("Are you a girl?: Y/N")
        if gender_quiz == 'Y':
            gender = 'boy'
        else:
            gender = 'girl'
else:
    print('please re-enter with your Chinese or English name')




### need to add a function to guess user's sex ###
### need to add a function to guess user's sex ###
### need to add a function to guess user's sex ###

# let user select a level & tell if the input is correct
level = input("Level: 1 for junior, 2 for CET4, 3 for CET6, 4 for master, 5 for English speakers, 6 for 'I am not here to learn English'" 
              "\nPlease enter which level you are in now"
              "\n"
              ": ")
if level.isnumeric() and (int(level) in lexicon_list_No):
    level = int(level)
    print(level_enter_correct)
else:
    print("please re-enter the number for the level, thanks.")
    level = input("Level: 1 for junior, 2 for CET4, 3 for CET6, 4 for master, 5 for English speakers, 6 for 'I am not here to learn English'" 
              "\nPlease enter which level you are in now"
              "\n"
              ": ")
    if level.isnumeric() and (int(level) in lexicon_list_No):
        level = int(level)
        print(level_enter_correct)
    else:
        level = 0
        print("OK, then let's play a game to see how good you are~")


# quiz main function
def quiz(lexicon):
    a = random.randint(0, len(lexicon)-1)
    b = list(lexicon.keys())[a]
    c = random.sample(range(0,10),7)
    print("\nWhat's the meaning of ", b, "?")
    
    #change the format to create real answer selections
    answer = input("Please enter one from below: {},{},{},{},{},{},{}:".format(
                   lexicon[list(lexicon.keys())[c[0]]],
                   lexicon[list(lexicon.keys())[c[1]]],
                   lexicon[list(lexicon.keys())[c[2]]],
                   lexicon[list(lexicon.keys())[c[3]]],
                   lexicon[list(lexicon.keys())[c[4]]],
                   lexicon[list(lexicon.keys())[c[5]]],
                   "不知道"))
    
    if answer == lexicon[b]:
        print("bingo! I knew you can nail it! let's see another one!")
        return True
    else:
        print("sorry, the correct answer should be ", lexicon[b] , "\nlet's try another one")
        return False

# quiz loop function
def quiz_logic(level, times):
    global correct, wrong
    while correct <= level and wrong < 2:
            if quiz(lexicon_list[level-1]) is True:
                correct += 1
                times += 1
            else:
                wrong += 1
                times += 1

#program main function           
def main():
    global level, times, result, correct, wrong

    # 10 questions and level not in top, then keep the quiz go
    while times < 10 and level < len(lexicon_list) and wrong<2:

        if correct >= level:
            level += 1
            correct = 0
            print("\nCongratulations! Level up!!! Now it's Level {}".format(level))
        else:
            quiz_logic(level, times)

    ### needs to update
    while times < 10 and level == len(lexicon_list) and wrong<2:
        # time return to 0
        times = 0

        if correct > level:
            print("Congratulations! Looks like we have a native speaker here :)")
            break
        elif wrong>=2:
            print('Sorry, you are not there yet~')
            break
        else:
            quiz_logic(level, times)


    print("Finally, we believe your level should be {}".format(level))
    return (level)

#run main
main()
