from selenium import webdriver
import speech_recognition
import pyttsx3
import os
from time import sleep

from urllib3.packages.six import b

chromedriver_linux = '/usr/bin/chromedriver'
chromedriver_window = 'C:\\Users\\Lorca\\AppData\\Local\\Google\\Chrome\\chromedriver.exe'
chromedriver_mac = '/usr/local/bin/chromedriver'

option = webdriver.ChromeOptions()
option.add_argument('headless')

microphone = speech_recognition.Recognizer()
program = pyttsx3.init()


def lyrics_search(lyrics, url):

    driver = webdriver.Chrome(chromedriver_mac, options=option)

    driver.get(url=url)

    search_box = driver.find_element_by_name("q")
    search_box.click()
    search_box.send_keys(lyrics)

    print("\nAnalyzing ...\n")

    sleep(3)

    song_title = driver.find_element_by_class_name("mini_card-title")
    singer = driver.find_element_by_class_name("mini_card-subtitle")

    print("-"*50)
    print()

    print("Song: {title}".format(title=song_title.text))
    print("Singer: {singer}".format(singer=singer.text))

    print()
    print("-"*50)


while True:

    os.system('clear')

    print("\nPress\n")
    print("1 - Analyze using text\n")
    print("2 - Analyze using voice\n")

    mode = int(input("-> Choose: "))

    print("\nPress:\n")
    print("1 - To analyze US-UK Songs\n")
    print("2 - To analyze VN songs\n")

    choose = int(input("-> Choose: "))
    print()

    if mode == 1:

        text = input("Enter text: ")

        lyrics = text + "\n"

        lyrics_search(lyrics=lyrics, url="https://genius.com/")

        break

    elif mode == 2:

        with speech_recognition.Microphone() as source:

            os.system('clear')

            record = input("\nPress [ENTER] to start recording.")

            if record == "":

                print("\nListening ...")

                audio = microphone.record(source=source, duration=5)

        try:

            if choose == 1:

                lyrics = microphone.recognize_google(audio, language="en-EN")

            elif choose == 2:

                lyrics = microphone.recognize_google(audio, language="vi-VN")

            # print("\nLyrics: {lyrics}".format(lyrics=lyrics))

            lyrics = lyrics + "\n"

        except Exception as errMsg:

            print("\n[ERROR]: {error}".format(error=errMsg))

            print("\nTrying again ...")

        else:

            lyrics_search(lyrics=lyrics, url="https://genius.com/")

            break

