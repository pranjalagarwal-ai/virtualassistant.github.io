from cgi import print_exception
import shutil
import subprocess
import wolframalpha
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib
import datetime
import requests
import random
import bs4 as bs
import urllib.request
import pyautogui
import time
from bs4 import BeautifulSoup

voiceEngine = pyttsx3.init('sapi5')
voices = voiceEngine.getProperty('voices')
voiceEngine.setProperty('voice', voices[1].id)
rate = voiceEngine.getProperty('rate')
voiceEngine.setProperty('rate', 270)


def speak(text):
    voiceEngine.say(text)
    voiceEngine.runAndWait()


def wish():
    print("Wishing.")
    time = int(datetime.datetime.now().hour)
    global uname, asname
    if time >= 0 and time < 12:
        speak("Good Morning !")

    elif time < 18:
        speak("Good Afternoon !")

    else:
        speak("Good Evening !")

    asname = "Gideon"
    speak("I am "+asname+" ,your Virtual Assistant  ")
    

def getName():
    global uname
    speak("May I please know your name?")
    uname = takeCommand()
    print("Name:", uname)
    
    speak("I am glad to know you!")
    print("I am Gideon your Virtual Assistant, How can I help you?")

    columns = shutil.get_terminal_size().columns

    speak("How can i Help you, ")
    speak(uname)


def takeCommand():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening to the user")
        recog.pause_threshold = 0.9
        userInput = recog.listen(source)

    try:
        print("Recognizing the command")
        command = recog.recognize_google(userInput, language='en-in')
        print(f"Command is: {command}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize the voice.")
        return "None"

    return command


def search(query):
    try:
        speak("Searching for "+query)
        print("Searching for "+query)
        result = wikipedia.summary(query, sentences=2)
        print(result)
        speak(result)
    except Exception as e:
        print(str(e))
        speak("I am sorry, I could not find any results for "+query)
        print("I am sorry, I could not find any results for "+query)


def getNews():
    try:
        response = requests.get('https://www.bbc.com/news')

        b4soup = BeautifulSoup(response.text, 'html.parser')
        headLines = b4soup.find('body').find_all('h3')
        unwantedLines = ['BBC World News TV', 'BBC World Service Radio',
                         'News daily newsletter', 'Mobile app', 'Get in touch']

        for x in list(dict.fromkeys(headLines)):
            if x.text.strip() not in unwantedLines:
                print(x.text.strip())
    except Exception as e:
        print(str(e))


if __name__ == '__main__':

    uname = ''
    asname = ''
    os.system('cls')
    wish()
    getName()
    print(uname)

    while True:

        command = takeCommand().lower()
        print(command)

        if "gideon" in command:
            wish()

        elif 'how are you' in command:
            speak("I am fine, Thank you")
            speak("How are you, ")
            speak(uname)

        elif "good morning" in command or "good afternoon" in command or "good evening" in command:
            speak("A very" + command)
            speak("Thank you for wishing me! Hope you are doing well!")
            print("Thank you for wishing me! Hope you are doing well!")

        elif 'fine' in command or "good" in command or "nice" in command:
            speak("It's good to know that your fine")
            print("It's good to know that your fine")

        elif "who are you" in command:
            speak("I am your virtual assistant, Gideon")
            print("I am your virtual assistant, Gideon ")
        
        elif "what you can do" in command:
            speak("I can do many things, like searching for you on wikipedia, opening youtube, play music, search products on flipkart, google, and many more")
            print("I can do many things, like searching for you on wikipedia, opening youtube, play music, search products on flipkart, google, and many more")

        elif "original name" in command:
            speak("People call me")
            speak(asname)
            
        elif "change my name to" in command:
            speak("What would you like me to call you, Sir or Madam ")
            uname = takeCommand()
            speak('Hello again,')
            speak(uname)

        elif "change name" in command:
            speak("What would you like to call me, Sir or Madam ")
            assname = takeCommand()
            speak("Thank you for naming me!")

        elif "what is your name" in command:
            speak("People call me")
            speak(assname)

        elif 'time' in command:
            strTime = datetime.datetime.now()
            curTime = str(strTime.hour)+"hours "+str(strTime.minute) + \
                "minutes "+str(strTime.second)+"seconds"
            speak(f" the current time is {curTime}")
            print("The time is " + curTime)


        elif 'open google' in command:
            speak("Opening Google\n")
            webbrowser.open("google.com")

        elif 'play music' in command or "play song" in command:
            search_term = command.split("play music")[-1]
            url = "https://open.spotify.com/search/"+search_term
            webbrowser.get().open(url)
            speak("You are listening to" + search_term + "enjoy sir")

        elif 'joke' in command:
            res = requests.get(
                'https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
            if res.status_code == requests.codes.ok:
                speak(str(res.json()['joke']))
                print (str(res.json()['joke']))
            else:
                speak('oops!I ran out of jokes')
            speak(pyjokes.get_joke())
            print (pyjokes.get_joke())

        # elif 'diet plan' in command:
        #     speak("diet plan for you is to eat healthy and exercise daily for 30 minutes and drink lots of water and sleep for 8 hours")
        #     print("diet plan for you is to eat healthy and exercise daily for 30 minutes and drink lots of water and sleep for 8 hours")

        elif 'monday diet plan' in command:
            speak("in the morning you can have oats with milk and fruits and in the evening you can have rice with vegetables and in the night you can have a glass of milk and a banana")
            print("in the morning you can have oats with milk and fruits and in the evening you can have rice with vegetables and in the night you can have a glass of milk and a banana")
    
        elif 'tuesday diet plan' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
    
        elif 'wednesday diet plan' in command:
            speak("int he morning you can have salad with fruits and in the evening you can have roti with vegetables and in the night you can have a dosa with chutney")
            print("int he morning you can have salad with fruits and in the evening you can have roti with vegetables and in the night you can have a dosa with chutney")

    
        elif 'thursday diet plan' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
    
        elif 'friday diet plan' in command:
            speak("in the morning you can have oats with milk and fruits and in the evening you can have rice with vegetables and in the night you can have a glass of milk and a banana")
            print("in the morning you can have oats with milk and fruits and in the evening you can have rice with vegetables and in the night you can have a glass of milk and a banana")
    
        elif 'saturday diet plan' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
    
        elif 'sunday diet plan' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
    
        elif 'party diet plan' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
    
        elif 'gym diet plan' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
    
        elif 'night diet plan' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'morning diet plan' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'evening diet plan' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'afternoon diet plan' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'weekend diet plan' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'regular diet plan' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'healthy diet plan' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'unhealthy diet plan' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'diet plan for weight loss' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'diet plan for weight gain' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'diet plan for muscle gain' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'diet plan for muscle loss' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'diet plan for fat loss' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'diet plan for fat gain' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")

        elif 'diet plan for fasting' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'diet plan for vegetarian' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'diet plan for non vegetarian' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'diet plan for diabetic' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'diet plan for heart patient' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'diet plan for kidney patient' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
       
        elif 'diet plan for liver patient' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'diet plan for thyroid patient' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
        elif 'diet plan for cancer patient' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
       
       
        elif 'diet plan for asthma patient' in command:
            speak("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
            print("in the morning you can have a glass of milk and a banana and in the evening you can have rice with vegetables and in the night you can have oats with milk and fruits")
        
        elif 'meaning of' in command:
            search_term = command.split("meaning of")[-1]
            url = "https://www.merriam-webster.com/dictionary/"+search_term
            webbrowser.get().open(url)
            speak("Here is the defination of" + search_term)


        elif 'stock price' in command:

            search_term = command.split("of")[-1]
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            speak("Here is what I found for " + search_term + " on google")
        

        elif 'search' in command:
            search_term = command.split("for")[-1]
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            speak("Here is what I found for " + search_term + " on google")
        
        
        elif 'flipkart find' in command:
                
                search_term = command.split("flipkart find")[-1]
                url = "https://www.flipkart.com/search?q="+search_term
                webbrowser.get().open(url)
                speak("here is what i found for"+search_term + "on flipkart.com")

        elif 'youtube find' in command:
            search_term = command.split("youtube find")[-1]
            url = "https://www.youtube.com/results?search_query="+search_term
            webbrowser.get().open(url)
            speak("here is what i found for"+search_term + "on youtube")

        elif 'game' in command:
            rock = "rock"
            paper = "paper"
            scissors = "scissors"
            while True:
                speak("Rock, Paper, Scissors?")
                print("Rock, Paper, Scissors?")
                user_input = takeCommand().lower()
                if user_input == rock:
                    speak("You chose rock")
                    print("You chose rock")
                    break
                elif user_input == paper:
                    speak("You chose paper")
                    print("You chose paper")
                    break
                elif user_input == scissors:
                    speak("You chose scissors")
                    print("You chose scissors")
                    break
                else:
                    speak("I am sorry, I could not understand your choice")
                    print("I am sorry, I could not understand your choice")
                    continue
            while True:
                computer_input = random.choice(["rock", "paper", "scissors"])
                if computer_input == rock:
                    speak("The computer chose rock")
                    print("The computer chose rock")
                    break
                elif computer_input == paper:
                    speak("The computer chose paper")
                    print("The computer chose paper")
                    break
                elif computer_input == scissors:
                    speak("The computer chose scissors")
                    print("The computer chose scissors")

                    break
                else:
                    speak("I am sorry, I could not understand your choice")
                    print("I am sorry, I could not understand your choice")
                    continue
            if user_input == computer_input:
                speak("It's a tie")
                print("It's a tie")
            elif user_input == "rock" and computer_input == "paper":
                speak("You lose")
                print("You lose")
            elif user_input == "rock" and computer_input == "scissors":
                speak("You win")
                print("You win")
            elif user_input == "paper" and computer_input == "rock":
                speak("You win")
                print("You win")
            elif user_input == "paper" and computer_input == "scissors":
                speak("You lose")
                print("You lose")
            elif user_input == "scissors" and computer_input == "rock":
                speak("You lose")
                print("You lose")
            elif user_input == "scissors" and computer_input == "paper":
                speak("You win")
                print("You win")
            else:
                speak("I am sorry, I could not understand your choice")
                print("I am sorry, I could not understand your choice")
                continue

        elif 'toss' in command or 'coin' in command:
            speak("I am tossing a coin")
            coin = random.randint(0, 1)
            if coin == 0:
                speak("Heads")
                print("Heads")
            else:
                speak("Tails")
                print("Tails")

        elif 'exit' in command:
            speak("Thanks for giving me your time")
            print ("Thanks for giving me your time")
            exit()

        elif "i love you" in command:
            speak("Thank you!, It's a pleasure to hear it from you.")
            print("Thank you!, It's a pleasure to hear it from you.")
        
        elif "who made you" in command or "who created you" in command:
            speak("I have been created by Pranjal.")
            print("I have been created by Pranjal.")


        
        elif "weather" in command:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n Humidity in percentage is " +
                      str(current_humidiy) +
                      "\n Description  " +
                      str(weather_description))
                print(" Temperature in Kelvin unit = " +
                      str(current_temperature) +
                      "\n Humidity (in Percentage) = " +
                      str(current_humidiy) +
                      "\n Description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif "what is" in command or "who is" in command:

            client = wolframalpha.Client("2RG5E6-R38UK82WQX")
            res = client.query(command)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")


        elif "news" in command:
            getNews()
            speak("Here are the news")
            
            print("Here are the news", getNews())
        
        elif "switch the window" in command:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        
        elif "switch tab forward" in command:
            pyautogui.keyDown("ctrl")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("ctrl")
        
        elif "switch tab backward" in command:
            pyautogui.keyDown("ctrl")
            pyautogui.press("shift")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("ctrl")

        elif "log off" in command or "power off" in command or "shutdown" in command:
            speak(
                "Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "restart" in command:
            subprocess.call(["shutdown", "/r"])

        elif "sleep" in command:
            speak("Setting in sleep mode")
            subprocess.call("shutdown / h")

        
        elif "write a note" in command:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('Gideon.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        else:
            speak("Sorry, I am not able to understand you")
