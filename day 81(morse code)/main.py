## goal: make a text-based program that takes any string input and converts it into morse code
import os
## step 1: make a dictionary containing the letter as the key with the corresponding morse code as the value

morse_code_data = {
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
}

## step 2: create a function that takes a string and turn it into morse code

def encode(user_input):
    list_of_char = list(user_input)
    user_code = ""
    for letter in list_of_char:
        if letter != " ":
            code = morse_code_data[letter.upper()]
            user_code += f" {code}"
        else:
            pass

    return print(user_code)

## step 3: Create a Loop for the program and a way for user to input their text
is_on = True
while is_on:
    ## ask the user for the text he wants to encode
    user_text = input('What would you like to encode? ')
    print("your code is:")
    ## call the function passing on the user input
    encode(user_input=user_text)
    ## ask user if he wants to contiue using the app
    to_continue = input('Would you like to encode more? type y/n ' ).upper()
    if to_continue != 'Y':
        is_on = False
    os.system('cls')
    
"""
Thoughts: After 3 steps I made a text-based app that takes string inputs and turn it into morse code. Took about 20 minutes from start to finish. 
This is my first solo project given by my instructor Angelu from 100 days of coding python (a udemy course)
"""
