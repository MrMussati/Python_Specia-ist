from selenium import webdriver
from selenium.webdriver.common import keys
import time


drive = webdriver.Chrome()
drive.get("https://google.com")
campo_pesquisa.click(1)
drive.find_element_by_name('q').send_keys('BMsupport')
time.sleep(120)