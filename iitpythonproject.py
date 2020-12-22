import random
# coding the introduction of the game
def intro():
    print("HELLO EVERYONE!")
    print("WELCOME TO THE BULL-COW GAME.\n")
    print("PLEASE READ THE GUIDE FOR THE GAME BEFORE CONTINUING.\n")
    print("PRESS 'r' AND THEN PRESS 'ENTER' TO SEE THE RULES")
    print("OR")
    print("PRESS 'ENTER' TO START THE GAME.")
intro()

# creating a dictionary of different words for the game
wordslist = {}
wordslist['list_words_level1'] = ['jam', 'web','now','get','how','its','top','had','day','two','buy','her','jan','she','set','map','way','car','own','end','him','per','big','law','art','usa','old','why','low','man','job','men','box','gay','air','yes','hot','say','dec','san','tax','got','let','act','red','key','few','age','oct','pay','war','nov','fax','yet','sun','run','net','put','try','log','faq','fun','feb','sep','lot','ask','due','mar','pro','url','aug','ago','apr','via','bad','far','jul','jun','oil','bit','bay','bar','dog','eur','pdf','usr','mon','com','gas','six','pre','sat','zip','bid','fri','wed','ltd','los','inc','win','bed','tue','thu','sea','cut','tel','kit','boy','est','son','mac','gmt','max','xml','bin','van','ads','int','hit','usb','etc','msn','las','min','aid','fat','saw','pst','tom','sub','led','fan','ten','cat','die','pet','guy','dev','cup','vol','fit','met','ice','sec','bus','bag','ibm','nor','bug','mid','jim','del','joe','cds','lab','cvs','des','lcd','ave','pic','tag','mix','vhs','fix','ray','dry','spa','con','ups','var','won','doc','row','usd','eat','aim','les','tip']
wordslist['list_words_level2'] = ['cake', 'bake', 'make', 'flux','muze','oman','rage','adsl','prix','avon','rays','walt','acne','libs','undo','halo','gays','maui','vids','yale','owen','bite','myth','oecd','dice','quad','dock','mods','hint','msie','buys','pork','barn','fare','bald','fuji','leon','mold','dame','herb','alot','idle','cove','incl','reid','flex','rosa','lazy','carb','pens','worm','deaf','mats','blah','usda','peas','urls','owns','zinc','levy','grad','bras','kyle','pale','gaps','tear','nest','nato','gale','stan','idol','cork','mali','dome','yang','dumb','feat','ntsc','conf','glow','oaks','erik','paso','norm','ware','jade','foul','keno','pose','mrna','goat','sail','sega','cdna','bolt','urge','smtp','kurt','ours','lone','cope']
wordslist['list_words_level3'] = ['beans','snake','julia','ought','fixes','timer','tyler','racks','nasty','tumor','forty','tubes','floyd','exams','welsh','sonic','thumb','ranks','debut','ivory','remix','spice','trash','manor','diane','disco','endif','minus','milan','shade','lions','lyric','grave','devon','punch','lucas','mardi','shake','mercy','shame','flesh','witch','cohen','kathy','satin','tunes','lucia','locks','euros','hired','hindu','slope','nails','whats','rides','rehab','merit','fairy','shaft','casio','drain','monte','fires','panic','beats','scuba','derby','steal','fears','tuner','alike','sagem','scout','dealt','bucks','badge','wrist','lexus','realm','rouge','yeast','yukon','singh','wives','viral','laden','edgar','dubai','sperm','filme','craps','frost','yacht','tracy','whale','shark','grows','shine','wendy','serum','swift','inbox','focal','wound','cindy','lined','boxed','chevy','tions','flyer','baths','emacs','climb','sparc','dover','token','kinda','dylan','belts','burke','flush','hayes','johns','ruled','funky','joins','scary','mpegs','cakes','mixer','sbjct','drove','upset','mines','logan','lance','lanes','purse','align','crest','plots','tulsa','casey','draws','surge','tahoe','spank','vault','wires','mails']
wordslist['list_words_level4'] = ['posing','urgent','gothic','graphs','patrol','mailto','boring','schema','prefix','typing','harold','namely','makeup','wicked','pushed','saturn','planes','tackle','ambien','builds','favors','strand','valued','luther','palmer','sewing','munich','harley','finals','parcel','flavor','hungry','curtis','charms','denial','thrown','nickel','coated','louise','beings','habits','unlock','dozens','varies','guards','breach','pastor','calvin','bumper','garlic','briefs','radios','hostel','employ','marvel','kinase','serbia','rounds','dosage','baking','brakes','sticky','jackie','brutal','yields','suited','blacks','curves','waiver','bufing','julian','brunei','slovak','remind','washer','mentor','fought','pencil','ratios','walnut','gently','fridge','blades','advert','travis','forbes','gerald','hunger','naples','prozac','newark','warned','neural','movers','verbal','bryant','voyuer','garmin','carmen','impose','favour','roland','mounts','michel','subtle','cradle','virtue']

# creating another dictionary from which a random word will be choosen as per the level requirement.
answer_dict = {}
answer_dict[1] = random.choice(wordslist['list_words_level1'])
answer_dict[2] = random.choice(wordslist['list_words_level2'])
answer_dict[3] = random.choice(wordslist['list_words_level3'])
answer_dict[4] = random.choice(wordslist['list_words_level4'])

# coding the conditions part
def conditions(l):
    print("Level : " + str(l))
    print("Conditions:-\n")
    print("There are " + str(len(answer_dict[l])) + " letters in the word.")
    print("First letter of the word is " + (answer_dict[l])[0] + ".")
    print("Input your answer in small letters.")
    print("You have " + str(len(answer_dict[l])*2) + " lives.\n")

# printing the rules of the game
def Rules():
    print("RULES:-\n")
    print("You will be provided with some conditions\nfor an unknown word whose all the\nletters are different.")
    print("Your task is to guess that word.\n")
    print("You get one 'BULL' if one of the letters")
    print("of your guess matches with the correct word's")
    print("letter and also if it is at the correct place.\n")
    print("You get one 'COW' if one of the letters")
    print("of your guess matches with the correct word's")
    print("letter but it is not at the correct place.\n")
    print("For example, if the correct answer is 'blue'")
    print("and your guess is 'bule' then you get")
    print("one bull for 'b', one bull for 'e',")
    print("one cow for 'l' and one cow for 'u'.\n")
    print("During the game you will be provided only with count of")
    print("Bulls and Cows for your previous guess.\n")
    print("You have to make assumptions on the basis of")
    print("the count of the bulls and cows of your previous guess.\n")
    print("You will have a limited number of lives to guess the answer.\n")
    print("For each incorrect guess, you will lose a life.\n")
    print("If all your lives are over, you lose the game.\n")
    print("If you guess the correct word, you will move on to the next level.\n")
    print("There are total 4 levels in the game.\n")
    print("To win this game, you have to pass all the 4 levels.")
    print("\n")
    print("Press enter to continue")
    x = input()
    while x!= "":
        print("Please press 'ENTER'")
        x = input()
    print()
    conditions(1)

# coding the first action needed on starting the game.
def welcome():
    x  = input()
    if x == "":
        print()
        conditions(1)
    elif x =="r":
        print()
        Rules()
welcome()

# most important part of the game, checking wether the guess is correct and how many bulls and cows are gained.
def GuessCheck(level):
    
    print("Type your word and then press 'ENTER'\n")
    lives = 2*len(answer_dict[level])
    
    while lives > 0:
        guess = input()
        if len(guess) == len(answer_dict[level]):
            for i in guess:
                t = 0
                if guess.count(i) > 1:
                    t = t + 1
            if t > 0 :
                print("All the letters in the word are different, continue guessing.")
            else :         
                bullcowcount = 0
                bullcount = 0
                cowcount = 0
                for letter in guess:
                    if letter in answer_dict[level]:
                        bullcowcount = bullcowcount + 1
                for index in range(len(answer_dict[level])):
                    if guess[index] == (answer_dict[level])[index]:
                        bullcount = bullcount + 1
                cowcount = bullcowcount - bullcount
                print("Your Guess: " + guess + ", BULL COUNT = " + str(bullcount) + ", COW COUNT = " + str(cowcount))
                if guess == answer_dict[level]:
                    print("\nCorrect Answer")
                    if level < 4:
                        level = level + 1
                        print("Lets move on to the next level\n")
                        print("Press enter to continue\n")
                        input_ = input()
                        if input_ == "":
                            conditions(level)
                            GuessCheck(level)
                    else :
                        print("Congratulations, You won the game!")
                        print("Press 'esc' to Quit the game")
                        u = input()
                        print(u)
                    break
                else :
                    lives = lives - 1
                    print("Lives Left = " + str(lives) + "\n")
                if lives == 0:
                    print("You lose!")
                    print("The correct answer was: " + answer_dict[level])
                    print("Press 'esc' to Quit the game")
                    u = input()
                    print(u)
                else :
                    print("Continue guessing\n")
        else :
            print("Please check the length of the word!")
GuessCheck(1)