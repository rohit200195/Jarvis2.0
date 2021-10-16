import ctypes
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from pywikihow import search_wikihow
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import time
import pyjokes
import pyautogui
from newsapi import NewsApiClient
import pycountry
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import webbrowser, urllib, re
import urllib.parse
import urllib.request


engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
print(voices[0].id)

#Text to speach
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#vcoice to Text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listning....')
        r.pause_threshold = 1
        audio = r.listen(source,timeout=4,phrase_time_limit=7)

    try:
        print('Recogninzing...')
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}")
    except Exception as e:
        return 'none'
    query = query.lower()
    return query


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour >=0 and hour <12:
        speak(f'Good Morning Rohit , currently it is {tt}')
    elif hour>=12 and hour<18:
        speak(f'Good afternoon Rohit , currently it is {tt}')
    else:
        speak(f'Good evening Rohit , currently it is {tt}')

    speak("I am Jarvis  How can I help you sir ")


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}
def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
        headers=headers)
    speak("wait a second i am searching sir")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    speak(f"The city of {location} on {time}  is {info} at {weather} degree Celsius")



def TaskExecution():
    wish()
    while True:
        query = takecommand()


        #LOGIC BUILDING
        if 'open notepad' in query:
            path = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(path)


        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to Rohit. further It's a secret")


        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif 'close notepad' in query:
            try:
                speak('okay closing notepad sir')
                os.system("taskkill /f /im notepad.exe")
            except Exception as e:
                speak('you don not have notepad open sir  do you want to open it')


        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'close command prompt' in query:
            try:
                speak('okay closing command prompt sir')
                os.system("taskkill /f /im cmd.exe")
            except Exception as e:
                speak('you don not have command prompt open sir do you want to open it')



        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(10)

                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "i want to code" in query:
            try:
                speak('Which code interpreter you have pycharm and vscode')
                cm = takecommand().lower()
                print(cm)
                if cm == "pycharm":
                    path_pycharm = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe'
                    os.startfile(path_pycharm)

                elif cm == "visual studio":
                    speak('here you go sir')
                    path_vscode = 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe'
                    os.startfile(path_vscode)
            except Exception as e:
                print(e)
                speak("sorry sir i could not open it")

        elif "what is my ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")



        elif "where i am" in query or "where are we" in query or 'where am i' in query:
            speak('wait sir let me check')
            try:
                ipAdd = requests.get('http://api.ipify.org/').text
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geodata= geo_requests.json()
                city = geodata['city']
                region = geodata['region']
                country = geodata['country']
                speak(f'we are in {city} {region} in {country}')

            except Exception as e:
                speak('sorry i could not find sir beacause of network issue')





        elif "wikipedia" in query:
            speak("searching on wikipedia wait a second   ")

            query = query.replace("wikipedia","")
            print(query)
            results = wikipedia.summary(query,sentences=3)
            speak("according to wikipedia ")
            speak(results)

        elif "write a note" in query:
            speak("What should i write, sir")

            note = takecommand().lower()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand().lower()
            if 'yes' in snfm or 'sure' or 'yeah' or 'ya' or 'ok' or 'yah' in snfm:
                # strTime = datetime.datetime.now().strftime("% H:% M:% S")
                # file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('note saved sir as Jarvis text file ')
            else:
                file.write(note)
                speak('note saved sir do as Jarvis text file')



        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))




        elif "open game" in query:
            play_path = 'C:\\Users\\rmohi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\eFootball PES 2021 SEASON UPDATE.url'
            os.startfile(play_path)


        elif "open youtube" in query:
            webbrowser.open("http://www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("http://www.facebook.com")

        elif "open stack overflow" in query:
            speak('what do you want to search sir')
            cm = takecommand().lower()
            driver = webdriver.Chrome()
            path = "http://stackoverflow.com/"
            driver.get(path)
            seracrc = driver.find_element_by_xpath('/html/body/header/div/form/div/input')
            seracrc.send_keys(cm)
            pyautogui.click()







        elif "open google" in query:
            speak("sir what should i search on google ")
            cm = takecommand().lower()
            print(cm)
            webbrowser.open(cm)


        elif "tell me the news" in query:
            try:
                newsapi = NewsApiClient(api_key='c2715b77580641aa986162351e8938c1')
                speak("which country are you interested to hear news about")
                input_country = takecommand().lower()
                speak('Which category are you interested in?   Business  Entertainment  General  Health  Science Technology')
                option = takecommand().lower()

                input_countries = list(input_country.split(" "))
                countries = {}
                for country in pycountry.countries:
                    countries[country.name] = country.alpha_2

                codes = [countries.get(country.title(), 'Unknown code')
                         for country in input_countries]


                top_headlines = newsapi.get_top_headlines(category=f'{option.lower()}',
                                                          language='en', country=f'{codes[0].lower()}')

                Headlines = top_headlines['articles']
                print(Headlines)
                if Headlines:
                    for articles in Headlines:
                        b = articles['title'][::-1].index("-")
                        if "news" in (articles['title'][-b+1:]).lower():
                            speak(f"{articles['title'][-b+1:]}: {articles['title'][:-b-2]}.")
                        else:
                            speak(f"{articles['title'][-b + 1:]} News: {articles['title'][:-b - 2]}.")
                else:
                    speak(f"Sorry no articles found for {input_country}, Something Wrong")

            except Exception as e:
                print(e)
            finally:
                speak("do you want to try sarching again")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke(category='all')
            speak(joke)


        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif "shut down the system" in query or 'shutdown' in query or 'close the system' in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")



        elif "switch the window" in query:
            try:

                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            except Exception as e:
                speak('you only have one tab open sir')


        elif "weather" in query or "whether" in query or "temperature" in query:
            speak("which city you want to know the weather about sir")
            city = takecommand().lower()
            city = city + " weather"
            weather(city)

        elif "activate how to do mode" in query or "activate how to do mod" in query:
            speak("how to do mode is activated ")
            while True:
                speak("please tell me what you want to know")
                how = takecommand()
                try:
                    if "exit" in how or "close" in how or "stop" in how:
                        speak("okay sir closing how to do mode")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how,max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am not able to find this")



        elif "convert to morse code" in query or "morse code" in query:
            speak("ok I can help you with this")
            while True:
                speak("what do you want to convert sir")
                text = takecommand()
                print(text)
                try:
                    if "exit" in text or "close" in text or "stop" in text or "nothing" in text:
                        speak("okay sir closing converter")
                        break
                    else:
                        MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                                           'C': '-.-.', 'D': '-..', 'E': '.',
                                           'F': '..-.', 'G': '--.', 'H': '....',
                                           'I': '..', 'J': '.---', 'K': '-.-',
                                           'L': '.-..', 'M': '--', 'N': '-.',
                                           'O': '---', 'P': '.--.', 'Q': '--.-',
                                           'R': '.-.', 'S': '...', 'T': '-',
                                           'U': '..-', 'V': '...-', 'W': '.--',
                                           'X': '-..-', 'Y': '-.--', 'Z': '--..',
                                           '1': '.----', '2': '..---', '3': '...--',
                                           '4': '....-', '5': '.....', '6': '-....',
                                           '7': '--...', '8': '---..', '9': '----.',
                                           '0': '-----', ', ': '--..--', '.': '.-.-.-',
                                           '?': '..--..', '/': '-..-.', '-': '-....-',
                                           '(': '-.--.', ')': '-.--.-'}

                        def encrypt(message):
                            cipher = ''
                            for letter in message:
                                if letter != ' ':

                                    cipher += MORSE_CODE_DICT[letter] + ' '
                                else:
                                    cipher += ' '

                            return cipher

                        result = encrypt(text.upper())
                        for i in result:
                            if '.' in i:
                                speak("dot")
                            elif '-' in i:
                                speak("dash")
                            else:
                                speak('space')
                        print(text,result)
                        speak("anything else you want to convert to morse code sir")

                except Exception as e:
                        speak("sorry sir I am not able to convert sir try again")




        elif "you can sleep now" in query or "sleep now" in query:
            speak("thanks for using me sir, we will meet soon")
            # sys.exit()
            break
        else:
            pass
if __name__ == "__main__":
    while True:
        permission = takecommand()
        if "wake up" in permission:
            speak("Initializing Jarvis")
            speak("Wait a moment sir")
            time.sleep(2)
            speak("Checking the internet connection")
            speak("All systems have been activated")
            speak("Now I am online")
            TaskExecution()
        elif "terminate now" in permission:
            speak('ok sir, i am shutting down the system')
            sys.exit()