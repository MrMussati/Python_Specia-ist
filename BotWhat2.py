#import as bibliotecas
from selenium import webdriver
import time


#Navegar ate What web 
driver = webdriver.Chrome(executable_path=r'C:\Users\bruno\.cache\selenium\chromedriver\win32\108.0.5359.7\chromedriver')
driver.get('https://https://web.whatsapp.com//')
time.sleep(120)
#buscar contatos/ grupos
contatos = [Bot] 
#Enviar mensagens para o contato / grupo
