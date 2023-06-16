from time import sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import csv
import random
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
 
driver_path = 'C:/Users/Admin/Desktop/Faucet-Tidefi/chromedriver.exe'
url = 'https://discord.com/channels/973057323805311026/979272741150687262' #Thay link kênh discord vào đây
options = webdriver.ChromeOptions()
service = ChromeService(executable_path=driver_path)
