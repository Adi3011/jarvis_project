# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:18:01 2021

@author: aditya kumar
"""

import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
#import webbrowser
import os
import random
import smtplib
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak("good morning1")
        
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good Evening")
        
    speak("I am Joseph Sir!. How can I help you")    


def takeCommand():
    #it taks microphone input from the user and returns string output
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio=r.listen(source)
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n" )
        
    except Exception as e:
        print(e)
        
        print("say that again please...")
        return "None"
    
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',465)
    server.ehlo()
    server.starttls()
    server.login('aditya1207khare@gmail.com','kumaraditya3011')
    server.sendmail("aditya1207khare@gmail.com",to,content)
    server.close()    

def sendMessage(content):
 driver = webdriver.Chrome(r'''E:\\chromedriver''') 
 driver.get("https://web.whatsapp.com/")
 
 wait = WebDriverWait(driver, 600) 

 target = '"Chanchal Cu"'
 #Write Message which you want to send
 string = content
 
 x_arg = '//span[contains(@title,' + target + ')]'

 group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
 #Now we perform the click task of the group_title to check every condition
 group_title.click()
 #Here input text xpath should be given for your input text message box
 inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'

 input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

 for i in range(100):
      input_box.send_keys(string + Keys.ENTER)
     
      time.sleep(1)
        

if __name__=="__main__":
    wishMe()
    c=webdriver.Chrome('E:\\chromedriver')
    
    while True:
        query=takeCommand().lower()
        #logic for executing tasks based on query
        
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            c.get("https://youtube.com/")
            
        elif 'open google'  in query:
            c.get("https://google.com/")
            
        elif 'open stackoverflow'  in query:
            
            c.get("https://stackoverflow.com/")  
            
        elif 'play music' in query:
            music_dir="D:\\video song"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randrange(0,len(songs)-1)]))
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir! the time is {strTime}")
            
        elif 'open vs code' in query:
            codepath="C:\\Users\\aditya kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            
        elif 'open blackboard' in query:
            c.get("https://cuchd.blackboard.com/")
            
        elif 'open cuims'in query:
            c.get("https://cuims.in/")
            
        elif 'send email' in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to="19bcs1084@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("unable to send email")
                
        elif 'send message' in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                sendMessage(content)
                speak("Message has been sent!")
            except Exception as e:
                print(e)
                speak("unable to send Message")
                
        
            
        elif 'close' in query:
             sys.exit()  
             
             