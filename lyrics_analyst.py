from selenium import webdriver
import speech_recognition
import pyttsx3
import os
from time import sleep

chromedriver_linux = '/usr/bin/chromedriver'
chromedriver_window = 'C:\\Users\\Lorca\\AppData\\Local\\Google\\Chrome\\chromedriver.exe'
chromedriver_mac = '/usr/local/bin/chromedriver'

option = webdriver.ChromeOptions()
option.add_argument('headless')

driver = webdriver.Chrome(chromedriver_linux, chrome_options=option)

microphone = speech_recognition.Recognizer()
program = pyttsx3.init()


def format(text, mode):

    if mode == 'genius':

        text = text.replace(" ","%20")
        text = text.replace("'","%27")

    elif mode == 'youtube':

        text = text.replace(" ", "+")
        text = text.replace("'","%27")
        text = text + "+"

    return text


def lyrics_search(lyrics, url):

    string = format(text=lyrics, mode='genius')

    link = "https://genius.com/search?q={formatted_search}".format(formatted_search=string)

    driver.get(url=link)

    print("\nAnalyzing ...")

    song_title = driver.find_element_by_class_name("mini_card-title")
    singer = driver.find_element_by_class_name("mini_card-subtitle")

    print("\nSong: {title}".format(title=song_title.text))
    print("Singer: {singer}".format(singer=singer.text))

    return song_title.text, singer.text


def song_lookup(title, singer):

    search = "{title} {singer}".format(title=title, singer=singer)

    string = format(text=search, mode='youtube')

    link = "https://www.youtube.com/results?search_query={query}".format(query=string)

    driver.get(url=link)

    # search_box = driver.find_element_by_id("search")
    # search_box.click()
    # search_box.send_keys("{song_name} {singer}\n".format(song_name = title, singer = singer))

    top_search = driver.find_element_by_id("video-title")
    top_search.click()

    print("\nLink: {url}".format(url=driver.current_url))


def text_search():
    
    os.system('clear')

    print("Enter lyrics:")

    lyrics = input("-> ")

    return lyrics


def voice_search():

    os.system('clear')

    print("\nPress:\n")
    print("1 - To analyze US-UK Songs\n")
    print("2 - To analyze VN songs\n")

    choose = int(input("-> Choose: "))
    print()

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

        return lyrics

    except Exception as errMsg:

            print("\n[ERROR]: {error}".format(error=errMsg))

            print("\nTrying again ...")



while True:

    os.system('clear')

    print("Choose mode:")
    print("1. Voice")
    print("2. Type\n")

    choice = input("-> ")

    if choice == '1':

        lyrics = voice_search()
        song_title, singer = lyrics_search(lyrics = lyrics, url = "https://genius.com/")
        song_lookup(title = song_title, singer = singer)

        break

    elif choice == '2':

        lyrics = text_search()
        song_title, singer = lyrics_search(lyrics = lyrics, url = "https://genius.com/")
        song_lookup(title = song_title, singer = singer)

        break
    
    else:

        print("\n[ERROR] Please try again!\n")

        sleep(2)

