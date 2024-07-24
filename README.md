# Jarvis-AI-Desktop-Voice-Assistant-Using-Python
Jarvis-AI-Desktop-Voice-Assistant-Using-Python is a Python-based application that emulates a sophisticated desktop voice assistant, inspired by the iconic character Jarvis from the Iron Man series. This project leverages advanced natural language processing and speech recognition capabilities to enable users to interact with their computers through voice commands.

Key functionalities include:

Voice recognition: Accurately converts spoken language into text for processing.
Text-to-speech: Provides clear and natural-sounding verbal responses.
Task execution: Performs various tasks based on user commands, such as opening applications, searching the web, playing music, setting alarms, and more.
Information retrieval: Accesses and delivers information from various sources like Wikipedia, news feeds, and weather updates.
Customizable interface: Offers a user-friendly interface with options for personalization.
This project demonstrates a strong foundation in Python programming, natural language processing, and speech recognition technologies. It serves as a valuable learning experience and showcases the potential of AI in enhancing user interactions with computers.
Imports:
pyttsx3: This library allows your program to convert text into speech and have it spoken aloud by your computer.
datetime: This library provides functions for working with dates and times.
speech_recognition: This library enables your program to recognize spoken language and convert it into text.
wikipedia: This library allows you to access and process information from Wikipedia.
webbrowser: This library helps your program open web pages in your default web browser.
os: This library provides functions for interacting with your computer's operating system, such as opening applications, managing files, and controlling the environment.
smtplib: This library allows your program to send emails.
Functions:
speak(audio): This function takes text as input and uses pyttsx3 to convert it into speech and play it through your speakers.
wishme(): This function greets you based on the current time of day (Good Morning, Afternoon, or Evening).
takeCommand(): This function uses speech_recognition to listen for your voice commands, convert them to text, and return the recognized text. It includes error handling for cases where the speech recognition fails.
sendEmail(to, content): This function takes the recipient's email address and the content of the email as input. It uses smtplib to connect to a mail server, authenticate with your email credentials (not shown in the code for security reasons), and send the email.
Main Program:
The code wrapped in the if __name__ == "__main__": block is the main part of your program.
The wishme() function is called first to greet you.
An infinite loop (while True) is used to continuously listen for your voice commands using the takeCommand() function.
Depending on the recognized keywords in your spoken command, the program performs different actions:
"wikipedia": Searches Wikipedia for the topic you specify and speaks the summary results.
"open youtube" or "open google": Opens the Youtube or Google website in your web browser.
"play music": Plays the first song found in a specified music directory.
"the time": Retrieves the current time and speaks it aloud.
"open code" or "open my documents": Opens the specified application or directory path.
"who are you": Identifies itself as Jarvis, your personal assistant.
"what can you do for me": Explains some of its capabilities.
"email to Mayur": Prompts you for the email content, sends the email to a specified address (replace with the actual recipient's email), and provides feedback on success or failure.
Additional Notes:
The code includes comments throughout to explain what different parts are doing.
You'll need to replace the email credentials in the sendEmail() function with your own valid email address and password to send emails.
The music directory path and code application path in the code might need to be adjusted based on your specific file system organization.
