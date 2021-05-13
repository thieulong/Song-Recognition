from selenium import webdriver
import speech_recognition
import pyttsx3

chromedriver_linux = '/usr/bin/chromedriver'
chromedriver_window = 'C:\\Users\\Lorca\\AppData\\Local\\Google\\Chrome\\chromedriver.exe'
chromedriver_mac = '/usr/local/bin/chromedriver'

option = webdriver.ChromeOptions()
option.add_argument('headless')

microphone = speech_recognition.Recognizer()
program = pyttsx3.init()


def lyrics_search(lyrics, url):

    driver = webdriver.Chrome(chromedriver_mac)

    driver.get(url=url)

    search_box = driver.find_element_by_name("q")
    search_box.click()
    search_box.send_keys(lyrics)

    song_title = driver.find_element_by_class_name("mini_card-title")
    singer = driver.find_element_by_class_name("mini_card-subtitle")

    print()

    print("Song: {title}".format(title=song_title.text))
    print("Singer: {singer}".format(singer=singer.text))


while True:

    with speech_recognition.Microphone() as source:

        print("Listening ...")

        audio = microphone.record(source=source, duration=5)

    try:

        lyrics = microphone.recognize_google(audio, language="vi-VN")

        print("Lyrics: {lyrics}".format(lyrics=lyrics))

    except Exception as errMsg:

        print("[ERROR]: {error}".format(error=errMsg))

    else:

        lyrics_search(lyrics=lyrics, url="https://genius.com/")
