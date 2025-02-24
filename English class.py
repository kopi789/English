def program():
        def hello():
            print('************************************************************************')
            print('The English text reader')
        hello()
        def reading():
            import pyttsx3
            tts = pyttsx3.init()
            tts.setProperty('rate',125)
            tts.setProperty('volume',0.8)
            x = input('What do you want to say? : ')
            tts.say(x)
            tts.runAndWait()
            spell_question = input("Do you want your word's spell? (yes/no) : ").lower()
            if spell_question in ['yes','y']:
                spelled_out = "  ".join(x.upper())
                print('Spelling :',spelled_out)
                tts.setProperty('rate',95)
                tts.say(spelled_out)
                tts.runAndWait()
                tts.setProperty('rate',125)
        reading()
        def question():
            while True:
                user_input = input('Do you want to continue? (yes/no) : ').lower()
                if user_input == 'yes' or user_input == 'y':
                    reading()
                elif user_input == 'no' or user_input == 'n':
                    print('************************************************************************')
                    break
                else:
                    print('Invalid input! Please enter yes or no')
        question()
# Program 2 is starting from here
def program2():
    def hello():
        print('Hello')
        print('Teaching fine details based on the notes of Professor Mohammad Amir Sinafar.')
    hello()
    def words():
        print('We have 4 types of word in English :')
        print('nouns (n)')
        print('verbs (v)')
        print('adjectives (adj)')
        print('adverbs (adv)')
    def numbers():
        print('We have 2 types of numbers in English : ')
        print('1.Cardinal numbers like : 1,2,3,4,5,78,12')
        print('2.ordinal numbers like : first(1st),second(2nd),third(3rd),etc.....')
        print('*Important point* : in the ordinal numbers,after 3,we must add Th after number.for example :')
        print('4th,5th,6th,10th...................')
    def adverds():
        print('According to the notes,we have 3 types of adverbs :')
        print('The adverbs of time like : now , yesterday , soon , *sentence : I will call you tomorrow*')
        print('The adverbs of place like : here , there , everywhere , *sentence : The cat is outside*')
        print('The adverbs of manner like : quickly , slowly , carefully , *sentence : He runs quickly*')
    def start():
        while True:
            start_question = input("What do you like to read? (types of words,types of numbers or types of adverbs),or you can type exit to finish : ").lower()
            if start_question == 'types of words' or start_question == 'words':
                words()
            elif start_question == 'types of numbers' or start_question == 'numbers':
                numbers()
            elif start_question == 'types of adverbs' or start_question == 'adverbs':
                adverds()
            elif start_question == 'exit' or start_question == 'e':
                print('************************************************************************')
                break
    start()                

def program3():
    def hello():
        print('The grammer teacher')
        print("Acording mr Sinafar's notes")
    hello()
    def grammers():
        simple_present = """Simple present grammer:
Where is it used? : We use simple present grammer to speak about our habits.
------------------------------------------------------------------------------------------------
Grammar formula : positive (subject + verb),negetive (subject + does not,do not + verb),question (Do,does + subject + verb)
------------------------------------------------------------------------------------------------
examples : I play football , She doesn't play violin , Do They swim at 7:20?
------------------------------------------------------------------------------------------------
important Points : If you want to use this grammer for (he,she,it) You should add s or es In The last of your verb""".strip()
        present_continuous = """Present continuous or present prograssive :
Where is it used? : We use pesent continuous to speak about express actions that are currently being performed.
------------------------------------------------------------------------------------------------
Grammer formula : positive (Subject + tobe verb + ing),negetive (Subject + not + tobe verb + ing),question (Tobe verb + subject + verb + ing)
------------------------------------------------------------------------------------------------
examples : I'm playing football , She isn't swimming , Are you studying?
------------------------------------------------------------------------------------------------
Important points : If there's vowel sound in the last of a word,that word + ing but we add two of last letter.For Example :
run + ing = running"""
        simple_past = """Simple past grammer :
Where is it used? : We use simple past to express actions that have been completed in the past.
------------------------------------------------------------------------------------------------
Grammer point : For using this grammer,We have 2 types of verbs ; regular : We must add d or ed in last of our verb : played,lived
And iregular : These types are memorable : go = went , write = wrote
------------------------------------------------------------------------------------------------
Grammer formula : positive (Subject + past verb),negetive (Subject + did not + past verb),quetion (Did + subject + past verb)
------------------------------------------------------------------------------------------------
Important points : To express the exact time of an action, adverbs of time such as "yesterday," "last week," "in 2010," etc., are usually used.
In negative and interrogative sentences, the main verb is in its base form."""
        past_continuous = """Past continuous grammer :
Where is it used? : We use past continuous to describe actions that were ongoing at a specific time in the past.
------------------------------------------------------------------------------------------------
Grammer formula : positive (Subject + was/were + verb + ing),negetive (Subject + not + was/were + verb + ing),question (Was/were + subject + verb + ing)
------------------------------------------------------------------------------------------------
Examples : She was studying , They weren't watching TV , Were you sleeping?
------------------------------------------------------------------------------------------------
Important points : The Past Continuous tense emphasizes the duration or continuity of an action in the past.
This tense is formed using the verb "tobe" in the past (was/were) and adding -ing to the main verb."""
        simple_future = """Simple future (will) :
Where is it used? : We use simple future to describe actions that will be performed in the future.
------------------------------------------------------------------------------------------------
Grammer formula : positive (Subject + will + verb),negetive (Subject + won't + verb),questoin (Will + subject + verb)
------------------------------------------------------------------------------------------------
Examples : I will go tomorrow , He won't come , Will you come with us?
------------------------------------------------------------------------------------------------
Important points : The Simple Future tense is formed simply using "will" and the main verb.
In spoken language, "will" is usually shortened to 'll  (for example: I'll, you'll)."""
        present_perfect = """Present perfect grammer :
Where is it used? : We use present perfect to describe actions that have been completed in the past and have an effect or connection to the present.
------------------------------------------------------------------------------------------------
Grammer formula : positive (Subject + have/has + past verb),negetive (Subject + not + have/has + past verb),question (Have/has + subject + past verb)
------------------------------------------------------------------------------------------------
Examples : T have read a book , He hasn't eaten yet , Have you see this movie?
------------------------------------------------------------------------------------------------
Important points : The Present Perfect tense does not refer to the exact time of the action in the past; rather, it emphasizes the result or effect of that action on the present.
Some verbs (such as "know," "believe," "love") are usually used in the Present Perfect tense because they indicate a state or condition."""
        past_progressive = """Past progressive grammer :
Where is it used? : The past progressive tense is used to describe actions that were ongoing at a specific time in the past.
This tense is typically used to express activities that were in progress and may have been interrupted by another action.
------------------------------------------------------------------------------------------------
Grammer formula : positive (Subject + was/were + verb with ing),negetive (Subject + not + was/were + verb with ing),question (Was/were + subject + verb with ing).
------------------------------------------------------------------------------------------------
Examples : She was reading a book , We weren't talking , Was he working?
------------------------------------------------------------------------------------------------
Important points : The past progressive tense is usually accompanied by specific times in the past, such as *at 5 o'clock* or *yesterday*.
This tense is usually not used for verbs that indicate a state or condition (such as *know* or *believe*)."""
        def question():
            cs = input('Which grammer do you want to practice? : ').lower()
            if cs in ['simple present']:
                print('************************************************************************')
                print(simple_present)
            elif cs in ['present continuous']:
                print('************************************************************************')
                print(present_continuous)
            elif cs in ['simple past']:
                print('************************************************************************')
                print(simple_past)
            elif cs in ['past continuous']:
                print('************************************************************************')
                print(past_continuous)
            elif cs in ['simple future','will']:
                print('************************************************************************')
                print(simple_future)
            elif cs in ['present perfect']:
                print('************************************************************************')
                print(present_perfect)
            elif cs in ['past progressive']:
                print('************************************************************************')
                print(past_progressive)
            else:
                print('Sorry! This grammer is not defined')
        def start():
            while True:
                question()
                v1 = input('Do you want to continue? (y/n) : ').lower()
                if v1 in ['y','yes']:
                    question()
                elif v1 in ['n','no']:
                    print('****************************************************************************')
                    break
                else:
                    print('Please enter y or n')
        start()                    
    grammers()                                           

def starting():
    def hello():
        print('Hello,Dear teachers')
        print('This program is given as a gift to my dear teacher at Bammad Danesh School,Mr Sinafar')
        print('This app has 2 options,teaching(teach),text reader(t) and grammer teacher (g)')
    hello()
    def question():
        while True:
            question1 = input("Which option Do you like to use? (if you don't want to use any option,press enter) : ").lower()
            if question1 == 't' or question1 == 'text reader':
                program()
            elif question1 == 'teach': 
                program2()
            elif question1 in ['G','g']:
                program3()    
            elif question1 == "":
                print('Ok,Goodbye')
                break    
            else:
                print("Sorry! This option isn't defined")
                continue
    question()        
starting()  
