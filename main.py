import random
import requests
import requests
import json
import pyjokes


def line():
    print ('<3...................................................<3')


notquit = True

# Random Quote API Generator
# Credit the random quote API - Falcon Infomatic on youtube

url = 'https://api.quotable.io/random'
r = requests.get(url)
quote = r.json()
line()
print ("(っ◔◡◔)っ ♥ TODAY'S RANDOM QUOTE: ♥")
print ('\n' + quote['content'])
print ('     -', quote['author'])


# Random Joke API Generator
# Credit the random joke API - adl212 (175) on replit

# update - this API is no longer working and will have to randomize my own jokes later on. Sad because they were really hilarious and would make me giggle when I was sad

# def randomJoke():
#     page = \
#         requests.get('https://official-joke-api.appspot.com/random_joke'
#                      )
#     jokesource = json.loads(page.content)
#     joke = jokesource['setup']
#     answer = jokesource['punchline']
#     print (ai + "\n" + joke)
#     print (ai + "\n" + answer)

def randomJoke():
    print (ai + '\n' + pyjokes.get_joke())


RANDOMAFFIRMATIONS = [
  'You are strong', 
  'You are more than your sadness', 
  'You deserve to be happy just like everyone',
  'You are not alone', 
  'You are beautiful',
  ]

GOODBYES = [
    'Bye',
    'Goodbye',
    'See you later',
    'See you soon',
    'Adios',
    'Au revoir',
    'Ciao',
    ]


def hotlines():
    print ('\nʜᴇʀᴇꜱ ɪꜱ ᴀ ʟɪꜱᴛ ᴏꜰ ꜱᴏᴍᴇ ʜᴏᴛʟɪɴᴇꜱ:)')
    print ('Southwest Crisis Center: (306) 778-3386')
    print ('Abuse: 1-800-799-7233')
    print ('Sexual Assault: 1-800-656-4673')
    print ('National Suicide Prevention Lifeline: 1-800-273-8255')
    print ('The Trevor Project (LGBTQ+): 866-488-7386')


def getGoodbye():
    return random.choice(GOODBYES)


def randomAffirmations():
    return random.choice(RANDOMAFFIRMATIONS)


def continuedConvo():
    print (ai + '\nAwesome! I will be here until you decide to leave me.')
    x = input('Would you like..........'
              + '\n[Random joke, Learn ways to feel better]?')
    print (userResponse + '\n' + x + '\n')
    line()
    if x == 'Random joke' or x == 'joke' or x == 'Joke':
        print ("(っ◔◡◔)っ ♥ YOUR RANDOM JOKE OF THE DAY: ♥ ")
        randomJoke()
        line()
    elif x == 'Learn ways to feel better' or x == '2' or x == 'learn':
        feelBetter = input(ai + '''

'''
                           + 'Would you like to learn more about \n[Tips to Manage Anxiety and Stress, Tips to manage suicidal and depressing thoughts, Tips on how to improve Your Physical and Mental Wellness][1,2,3]'
                           )
        print (userResponse + '\n' + feelBetter)
        if feelBetter == '1':
          print (ai)
          # credit https://www.healthline.com/health/anxiety-exercises#breathe
          print("\n(っ◔◡◔)っ ♥ let's practice this together ♥\n~~Sit in a quiet and comfortable place. Put one of your hands on your chest and the other on your stomach. Your stomach should move more than your chest when you breathe in deeply.\n~~Take a slow and regular breath in through your nose. Watch and sense your hands as you breathe in. The hand on your chest should remain still while the hand on your stomach will move slightly.\n~~Breathe out through your mouth slowly.\n~~Repeat this process at least 10 times or until you begin to feel your anxiety lessen.")
        elif feelBetter == "2":
          print (ai) 
          # credit https://www.verywellmind.com/tips-for-coping-with-suicidal-thoughts-1067530
          print ("\n(っ◔◡◔)っ ♥You don't have to go through this alone so here are things you could do to feel better\n\n~~(1)Call a Suicide Hotline.\n~~(2)Make Your Environment Safe - Making your space safe could involve removing items from your home that you may feel tempted to use to hurt yourself, such as pills or guns. If that isn't feasible, remove yourself from the situation by going somewhere else for a while or asking a friend or family member to help you.\n~~(3)Remind Yourself of the Good Things in Your Life.\n~~(4)Seek Professional Help - there numerous ways to get help either virtually or face-to-face. \n\nClick this link to find the nearest therapist - https://www.psychologytoday.com/us?tr=Hdr_Brand.....\nIf you would prefer a virtual therapist then try - https://go.startlivehealthonline.com/mental-health/?utm_source=google")
          line()
          print (ai)
          callHotline = input('\nWould you like to call a hotline? [Y/N]')
          if callHotline == 'Y':
            hotlines()
          else:
            print (ai + '\n' + 'Ok but remember ' + randomAffirmations().upper())
        elif feelBetter == '3':
          print (ai)
          # credit https://cropwatch.unl.edu/2019/5-simple-ways-improve-your-physical-and-mental-wellness
          print ("\n(っ◔◡◔)っ ♥5 Simple Ways to Improve Your Physical and Mental Wellness\n\n~~(1)Exercise - The key is to find the right type of exercise for you – whether that means joining a casual sports team, going for walks with a friend or a pet, or doing yoga from the comfort of your own home. Physical activity has been shown to help clear the mind, improve self-worth, and reduce depressive and anxious feelings.\n~~(2)Sleep - We once thought that poor sleeping habits were caused by mental health disorders, but more recent research suggests poor sleep can be the cause of mental health problems or make them worse. Following a healthy bedtime routine could make you feel happier and calmer and be better focused throughout the day.\n~~(3)Nutrition - Cut down on sugary foods and replace them with nutrient-rich foods like fish, veggies, and foods that have healthy fats such as avocados. These habits have been shown to reduce depressive symptoms in adults.\n~~(4)Community and Relationships - Whether the support comes from family, a partner, friends, coworkers, or even pets, feeling connected to those around you can increase a sense of purpose and love in your life. Identify ways to create community. \n~~(5)Relaxation and Recreation - In our busy lives it can be easy to forget about the hobbies you used to love, or to make time to sit down and enjoy a book. Building in time to do the things you enjoy will give you a happier frame of mind and give you more energy to deal with difficult emotions when they arise.")

line()
ai = \
    "\n˜”*°• AI BUDDY: :) .•°*”˜"
userResponse = \
    '\n˜”*°• YOU: .•°*”˜'

print (ai)

userName = \
    input("Hello! I'm your AI mental health chatbot.\nWhat's your name? (Type your name below.)"
          )
print (userResponse)
print (userName.capitalize())


def intro():
    line()
    print (ai)
    print ('You have such a pretty name, ' + userName.capitalize() + '!')
    
    botName = \
        input("""I don't have a name yet. What would you like to call me?""")
    print (userResponse + '\n' + botName.capitalize())
    line()
    print ("\nAI " + botName.upper() + " :) :" + "\nAbsolutly love my new name, " + userName.capitalize() + "!\n")
    line()
    
    print(ai)
    waterQns = input(userName + ", have you drank at least a cup of water today?[Y/N]")
    print (userResponse +"\n" + waterQns)
    
    if waterQns == "Y":
      print(ai + "\n" + "Awesomeeeee bestie!")
      print ('<3...................................................<3')
    elif waterQns == "N":
      print(ai + "\n" + "Oh man bestie! Drink some water, please!")
      print ('<3...................................................<3')

intro()


def feels():
    line()
    print (ai)
    userFeels = input("\nNow I'd like to know, "
                      + userName.capitalize()
                      + '...\nOn a scale from 1 (the worst) to 10 (the best), how are you feeling today?'
                      )
    print (userResponse + '\n' + userFeels)

    if int(userFeels) <= 4:
        print (ai)
        currentEmotion = input('Oh noooo ' + userName.capitalize()
                               + '\nWould you mind telling me what is wrong?'

                               + ' \nAre you [sad, depressed, suicidal, anxious, stressed]?'
                               )
        print (userResponse + '\nI am ' + currentEmotion)
        if currentEmotion == 'sad' or currentEmotion == 'depressed' or currentEmotion == 'suicidal' \
            or currentEmotion == 'anxious' or currentEmotion == "stressed":
            print (ai + "\nI'm sorry you're feeling this way. So, in the meanwhile, I've listed some contact information below in case you need to contact someone. Sometimes all we need is someone to listen. :)")
            hotlines()
            print (ai + "\n" + "Remember " + randomAffirmations().upper())
        line()
        print (ai)
        continueConvo = input(userName.capitalize()
                              + ' would you like to continue talking with me? [Y/N]'
                              )
        print (userResponse + '\n' + continueConvo)

        if continueConvo == 'y' or continueConvo == 'yes':
            continuedConvo()
        if continueConvo == 'n' or continueConvo == 'No' or continueConvo == 'N':
          print ("")

        while True:
            x = input(ai
                      + '\ntype QUIT to quit or anything else to conntinue----'
                      )
            if x == 'QUIT' or continueConvo == 'N':
                print (getGoodbye() + ' ' + userName)
                break
            continuedConvo()
    elif int(userFeels) >= 5:
        while True:
            continuedConvo()
            x = input(ai
                      + '\ntype QUIT to quit or anything else to conntinue----'
                      )
            if x == 'QUIT':
                print (ai + '\n' + getGoodbye() + ' ' + userName)
                break


feels()
