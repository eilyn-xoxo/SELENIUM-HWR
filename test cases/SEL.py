from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

def initial_test():
    driver= webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://platzi.com")

    print("Application title is", driver.title)
    print("Application URL is", driver.current_url)
    time.sleep(20)
