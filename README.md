# Triva Cracked

Trivia Cracked is a program developed in python using Google's "Gemini' AI model to 
provide answers to Trivia Crack questions

## Technology

Trivia Cracked utilizes... 

- PyAutoGUI: to capture screenshots as well as click the correct answer
- Pytesseract: to extract the text from the screenshots taken
- Gemini Pro AI Model: to answer the extracted questions

## How it works

When you run the program, PyAutoGUI will take a screenshot of your Triva Crack window. Pytesseract then
extracts the text from the screenshot given, and then gives the text to the Gemini AI model to answer. Once
Gemini has the answer, the program will compare Gemini's answer to the text of the options and choose which
screenshot contains the right answer. Finally, PyAutoGUI will take the screenshot of the chosen answer, locate it
on the screen, and then click on it.

## Problems

This program is faulty at time. Sometimes because Gemini gets the question wrong, and other times because PyAutoGUI
is unable to locate the answer on the screen. This leads to either the program selecting the wrong option, or no options at all.


### Authors

- [@EthanOndreicka](https://github.com/EthanOndreicka)
