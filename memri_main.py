import numpy as np
import cv2
import pyautogui
import pytesseract
from PIL import Image
import time
import json
from dataclasses import dataclass  # if python < 3.7
from typing import Optional, List
from operator import add, sub, mul, truediv
import ctypes
class Ocr():
    pass
class File():
    
        
        def details_read():
            with open("memri_storage.json") as file:
                contents = json.load(file)
                return contents
        def return_read():
            contents = File.details_read()
            return [contents["login"]["firstName"],contents["login"]["lastName"],contents["login"]["day"],contents["login"]["month"],contents["login"]["year"]]
        

class Input():
    def string_to_list(input_str):
        # create an empty list to store the characters
        char_list = []

        # loop through the characters in the string
        i = 0
        while i < len(input_str):
            if input_str[i:i+7] == " ENTER ":
                # if the current and next 5 characters spell " enter", add "enter" to the list
                char_list.append("enter")
                i += 6  # skip over the next 5 characters
            elif input_str[i:i+5] == " TAB ":
                # if the current and next 3 characters spell " tab", add "tab" to the list
                char_list.append("tab")
                i += 4  # skip over the next 3 characters
            else:
                # otherwise, add the current character to the list
                char_list.append(input_str[i])
                i += 1  # move on to the next character
        
        return char_list
    def enter(input_str):
        for i in Input.string_to_list(input_str):
            pyautogui.press(i)
         
        

def login():
    pass