from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import itertools, sys, requests, mechanize, os, re, email, smtplib, ssl, selenium
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium.webdriver.firefox.options import Options
import logging
import selenium.webdriver
import selenium.webdriver.firefox.service
import time

def check_active_friends(username, password):
    options = Options()
    options.add_argument("--headless")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    # or other browser driver
    driver.get("https://www.facebook.com/")

    # Login
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "pass")
    login_button = driver.find_element(By.NAME, "login")

    email_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    # Navigate to friends list
    wait = WebDriverWait(driver, 10)
    friends_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Friends']")))
    friends_link.click()

    # Scrape active friends
    time.sleep(5)  # Wait for content to load
    soup = BeautifulSoup(driver.page_source, "html.parser")
    active_friends = soup.find_all("div", class_="f8c07x6l e7dh9p6j") # This class might vary, inspect the page
    
    for friend in active_friends:
        name = friend.find("span", class_="a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7").text # This class might vary, inspect the page
        print(f"{name} is active!")
    
    driver.quit()

# Replace with your actual credentials
username = "Krarktel@yahoo.com"
password = "Yuka338"

check_active_friends(username, password)

# Replace with your Facebook credentials
