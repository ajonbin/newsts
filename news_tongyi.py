from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import subprocess
import pyperclip
import os

def generate_news(prompt: str, news_file:str):
    # #google-chrome --remote-debugging-port=9222
    #os.system("google-chrome --remote-debugging-port=9222")
    print("google opened")
    print(prompt)
    options = Options()
    options.add_experimental_option('debuggerAddress', 'localhost:9222')
    driver_path = './chromedriver-linux64/chromedriver'
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://tongyi.aliyun.com/qianwen/')
    driver.implicitly_wait(3)
    sleep(3)

    dialog_input = driver.find_element(By.CLASS_NAME, 'ant-input')
    dialog_input.clear()
    dialog_input.send_keys(prompt)
    sleep(10)

    submit_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div/div[3]/div[3]/div[2]')
    submit_button.click()
    driver.implicitly_wait(30)

    print("Waiting response...")
    sleep(30)

    dialog_output = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[3]')
    dialog_output.click()
    driver.quit()

    text = pyperclip.paste()

    with open(news_file, 'a') as f:
        f.write(text)
        f.write('\n')
    print(text)
