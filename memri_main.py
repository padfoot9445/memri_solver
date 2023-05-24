import numpy as np;import cv2;import pyautogui;import pytesseract;from PIL import Image;import time;import json;from dataclasses import dataclass; from typing import Optional, List;from operator import add, sub, mul, truediv;import ctypes;import subprocess;import os;import threading;from pynput import keyboard;import nltk;import wolframalpha
class Stop():
    def __init__(self):
        def on_press(key):
            
            if str(key).strip() == "Key.f12":
                print(key,"E")
                os._exit(1)

        def on_release(key):
            
            if str(key).strip() == "Key.f12":
                print(key,"k")
                os._exit(1)

        listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release)
        listener.start()

class File():
    
        
        def details_read(self):
            with open("storage.json") as file:
                contents = json.load(file)
                return contents
        
        def presets(self):
            return self.details_read()["presets"]

        def return_read(self):
            """returns a list with the items being, in order, school name, first name, last name, day of birth, month of birth, year of birth, and password."""
            contents = self.details_read()
            return [contents["login"]["schoolName"],contents["login"]["firstName"],contents["login"]["lastName"],contents["login"]["day"],contents["login"]["month"],contents["login"]["year"],contents["login"]["password"]]
        def image_find(string):
            #converts string into words
            words = nltk.word_tokenize(string)
            #finds words in image
            pass

class Ocr():
    def screenshot(self):
    
        # take screenshot using pyautogui
        image = pyautogui.screenshot()
        
        # since the pyautogui takes as a 
        # PIL(pillow) and in RGB we need to 
        # convert it to numpy array and BGR 
        # so we can write it to the disk
        image = cv2.cvtColor(np.array(image),
                            cv2.COLOR_RGB2BGR)
    
        # writing it to the disk using opencv
        cv2.imwrite("image1.png", image)
    
    def read_image(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        im = Image.open("image1.png")
        #convert into an array of sentences
        def remove_special_characters(char):
             if char.isalnum() or char == " " or char == "\n":
                  return True
             else:
                  return False
        text = ''.join(filter(remove_special_characters, pytesseract.image_to_string(im, lang = 'eng'))).lower()

        with open("storage.json") as file:
            json_file = json.load(file)
            text_array = nltk.line_tokenize(text)
           

            json_file["imageText"] = text_array
        with open("storage.json","w") as file:
            json.dump(json_file,file, indent=2)
    
    

    def words(self) -> list[str,str,str]:
        """returns every single word, with special characters removed, on the screen (that has been read)"""
        return_list = []
        for sentence in file.details_read()["imageText"]:
            sentence = nltk.word_tokenize(sentence)
            return_list.append(sentence)
        return return_list
    
    def find_words(self,words: list[str], same_line: bool) -> list[bool,list]:
        """enter a list of words to find out if and where they exist. same line: all words must be from the same, or multiple singular, lines. Returns as list[Bool(found?),list(sentences found in),list[word number in sentences]]. If any of these are not applicable, then None."""
        return_list = [False,[]]
        if len(words) == 0:
            return[True, None]

        if same_line:
            
            #check which sentence the first word is in 
            for sentence in enumerate(self.words()):
                if words[0].lower() in sentence[1]:
                    
                
                    word_not_found = False
                    for word in words:
                        if not word in sentence[1]:
                            word_not_found = True
                    if not word_not_found:
                        return_list[1].append(sentence[0])
                        return_list[0] = True
        else:
            
            word_not_found = False
            for word in words:
                found_word = False
                for sentence in enumerate(self.words()):
                    if word.lower() in sentence[1]:
                        found_word = True
                        return_list[1].append(sentence[0])
                if not found_word:
                    word_not_found = True
                    break
            if not word_not_found:
                return_list[0] = True
        if return_list == [False,[]]:
            return_list = [False,None]

        return return_list












    def start(self):
        
        self.screenshot()
        self.read_image()

file = File()
ocr = Ocr()
class Input():
    def string_to_list(self,input_str):
        # create an empty list to store the characters
        char_list = []

        # loop through the characters in the string
        i = 0
        while i < len(input_str):
            if input_str[i:i+7] == " ENTER ":
                # if the current and next 5 characters spell " enter", add "enter" to the list
                char_list.append("enter")
                i += 7  # skip over the next 5 characters
            elif input_str[i:i+5] == " TAB ":
                # if the current and next 3 characters spell " tab", add "tab" to the list
                char_list.append("tab")
                i += 5  # skip over the next 3 characters
            else:
                # otherwise, add the current character to the list
                char_list.append(input_str[i])
                i += 1  # move on to the next character
        
        return char_list
    def enter(self,input_str):
        time.sleep(0.5)
        for i in self.string_to_list(input_str):
            pyautogui.press(i)
        pyautogui.press("enter")
        pyautogui.press("enter")
    def eenter(self,input_str):
        time.sleep(0.5)
        for i in self.string_to_list(input_str):
            pyautogui.press(i)
        
    
input_obj = Input()
        
        
class login():

    def resize(self):
        pyautogui.hotkey("ctrl","0")
        for i in range(3):
            pyautogui.hotkey("ctrl","-")
    def dropdown(item,column):
        """enter the item number and the column"""
        
        size = pyautogui.size()
        if item < 1:
            raise ValueError(f"Item in Dropdown must not be smaller than one(input:{item})")
        if column == 1:
            day_width = (size[0]*18/50)
        elif column == 2:
            if item > 12:
                raise ValueError(f"Item in Dropdown must not be larger than twelve when entering the month(column two) (input:{item})")
            
            day_width = (size[0]*24/50)
        elif column == 3:
            item = (2023 - item + 1)
            day_width = (size[0]*3/5)
        
        pyautogui.moveTo(day_width,(size[1]*101/200))
        pyautogui.leftClick()
        if (item >= 1 and item <= 20):
            increment = (item - 1)*3.7
            pyautogui.moveTo(day_width,size[1]*(110+increment)/200)
            pyautogui.leftClick()
        else:
            #move to scroll down button
            pyautogui.moveTo(day_width+size[0]*19/500,size[1]*(19*3.7+110)/200)
            for i in range(10):
                pyautogui.leftClick()
            item -= 12
            increment = (item - 1)*3.7
            pyautogui.moveTo(day_width,size[1]*((110+increment)+3.7)/200)
            pyautogui.leftClick()
    def check_login(self) -> bool: 
        ocr.start()
        time.sleep(2)
        def majority(a,margin):
            
            
            for i in a:
                found = 0
                for e in i:
                    if ocr.find_words(a,True)[0]:
                        found += 1
                if (len(e) - found) <= margin:
                    return True
                else:
                    return False

        if majority(["1","january","v","2016"],1) or majority(["enter","your","details"],1) or majority(["logging","into","wyvern","college",2]) or ocr.find_words(["first","name"],True)[0] or ocr.find_words(["last","name"],True)[0]:
            #1 v january v 2016 v
            return True
        else:
            return False
    def __init__(self):
        data = file.return_read()
        size = pyautogui.size()
        #click position for school login
        click_position = ((size[0]/2),(size[1]*9/20))
        #do you need to reenter school?
        
        enter_school = file.details_read()["config"]["enterSchool"]
        #opens windows
        pyautogui.press("win")
        #opens hegarty maths
        time.sleep(1)
        input_obj.eenter("https://hegartymaths.com/login/learner ENTER ")
        time.sleep(1)
        #resizes screen
        self.resize()
        ocr.start()
        if self.check_login():
            print("E")
            if enter_school:
                #moves to school column
                pyautogui.moveTo((size[0]/2),(size[1]*35/100),0.5)
                pyautogui.leftClick()
                #searches up the school
                input_obj.enter(data[0])
                
                
                #clicks the correct school

                pyautogui.moveTo(click_position)
                
                pyautogui.leftClick()
            #goes to student rows; enters first and last names
            
            input_obj.eenter(f"{data[1]} TAB {data[2]}")
            #clears the field of any presaved data
            pyautogui.moveTo(size[0]*4/5,size[1]/2)
            pyautogui.leftClick()
            #enters the dropdown values
            for i in range(3):
                login.dropdown(data[i+3],i+1)
            #presses "next"
            pyautogui.moveTo(size[0]*24/50,size[1]*124.8/200)
            pyautogui.leftClick()
            #enters password
            input_obj.eenter(f"{data[6]} ENTER ")
            #Presses never if needed
            pyautogui.moveTo(size[0]*3/4,size[1]*115/300)
            pyautogui.leftClick()

class Maths():
    
    def preset(self):
        ocr = Ocr()
        file = File()
        ocr.start()
        for category in file.details_read()["presets"]:
            for preset in file.details_read()["presets"][category]:
                print(category)
                print(preset)
                array = file.details_read()["presets"][category][preset]["keywords"]["anyLine"]
                preset1 = file.details_read()["presets"][category][preset]
                if ocr.find_words( array, False) and ocr.find_words(file.details_read()["presets"][category][preset]["keywords"]["anyLine"],True):
                    word_not_found = False
                    for i in preset1["keywords"]["newLine"]:
                        for sentence in file.details_read()["imageText"]:
                            if not i.strip() == sentence.strip():
                                word_not_found = True
                    if not word_not_found:
                        input_obj.enter(preset1["answer"])
                        return True
                    else:
                        return False

    def wolfram(self,query):
        
        key = file.details_read()["config"]["wolframKey"]
        client = wolframalpha.Client(key)

        
        res = client.query(query)
        output = next(res.results).text
        return output
    
    def user_input(self):
        if file.details_read()["config"]["alertUser"]:
            raise NotImplementedError
        else:
            pyautogui.press("IDK")
            pyautogui.press("enter")
            while True:
                if ocr.find_words(["Uh","oh"], True)[0]:
                    pyautogui.press("enter")
                    pyautogui.press("IDK")
                    pyautogui.press("enter")
                    time.sleep()
                else:
                    break
            
            print("unable to resolve question, try again.")

    
    def main(self,memri:bool):
        size = pyautogui.size()
        if memri:
            #moves to revise button
            pyautogui.leftClick(size[0]*120/200,size[1]/8)
            #moves to memri button
            pyautogui.leftClick(size[0]*120/200,size[1]/5)
            time.sleep(0.5)
            #starts memri
            pyautogui.leftClick(size[0]*55/200,size[1]*10/35)
            if ocr.find_words(["you","already","earned"],False)[0]:
                pyautogui.press("enter")
            
        else:
            #move to my tasks button
            pyautogui.leftClick(size[0]*130/200,size[1]/8)
            #move to start button
            pyautogui.leftClick(size[0]*150/200,size[1]/4)
            #check with actual task
            raise NotImplementedError
            pyautogui.leftClick(size[0]*130/200,size[1]*10/23)
        while True:
            
            if not self.preset():
                lines = ocr.find_words(file.details_read()["wolframKeyWords"])[1]
                temparray = []
                for index in lines:
                    temparray.append(file.details_read()["imageText"][index])
                send = ""
                for sentance in temparray:
                    send += sentance
                    send += ". "

                try:
                    e = self.wolfram(send)
                    input_obj.enter(e)
                    print(e,"F")
                    
                except StopIteration:

                    self.user_input() 
            if ocr.find_words(["MemRi","Quiz","Complete"],True)[0]:
                input_obj.enter(" ENTER  ENTER")
                break

maths = Maths()  





class Main():
    def desktop(self):
        """returns to desktop screen"""
        size = pyautogui.size()
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(size[0],size[1])
        pyautogui.leftClick()
        pyautogui.moveTo(size[0]/2,size[1]/2)
        pyautogui.FAILSAFE = True
        time.sleep(1)
    def __init__(self):
        Stop()
        self.desktop()
        time.sleep(2)
        login()
        time.sleep(2)
        
        ocr.start()
        maths.main(file.details_read()["config"]["memri"])
        

Main()








