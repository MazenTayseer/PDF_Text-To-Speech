import time

import fitz
import pyttsx3
import PyPDF2

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def highlightWords(words):
    for word in words:
        driver.find_element(By.XPATH, "//input[@type='search']").send_keys(word)
        driver.find_element(By.XPATH, "//input[@type='search']").send_keys(Keys.ENTER)
        driver.find_element(By.XPATH, "//input[@type='search']").clear()
        time.sleep(0.09)


def sayWords(text):
    engine.setProperty('rate', 150)

    engine.say(text)
    engine.runAndWait()


engine = pyttsx3.init()

pdf_file_path = 'pdf.pdf'
pdf_file = open(pdf_file_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

with fitz.open(pdf_file_path) as doc:
    text = ""
    for page in doc:
        text += page.get_text()

words = text.split("\n")

options = webdriver.ChromeOptions()
options.add_extension(
    "C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\efaidnbmnnnibpcajpcglclefindmkaj\\15.1.3.44_0.crx")

driver = webdriver.Chrome(options=options)

driver.get("file:///D:/Python/TTS/pdf.pdf")

time.sleep(7)

driver.switch_to.window(driver.window_handles[1])
driver.close()

driver.switch_to.window(driver.window_handles[0])

driver.refresh()
time.sleep(15)

frame = driver.find_elements(By.TAG_NAME, 'iframe')[0]
driver.switch_to.frame(frame)

try:
    close = driver.find_element(By.ID, 'guided-tour.initialcard.close')
    close.click()
except selenium.common.exceptions.NoSuchElementException:
    pass

search = driver.find_element(By.ID, 'documentSearch')
search.click()
time.sleep(2)

searchbar = driver.find_element(By.XPATH, "//input[@type='search']")
for word in words:
    line = ''
    sentence = word.split(" ")
    for ins in sentence:
        line += ins + " "

    searchbar.send_keys(line)
    searchbar.send_keys(Keys.ENTER)
    searchbar.clear()

    engine.say(word)
    engine.runAndWait()
