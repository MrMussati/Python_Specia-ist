#importar as biblioteca
from selenium import webdriver
import time
from selenium.webdriver.common import keys
 
 # navegar ate o whatsapp web
driver = webdriver.Chrome(executable_path=r'C:\Users\bruno\.cache\selenium\chromedriver\win32\108.0.5359.7\chromedriver') 
driver.get('https://web.whatsapp.com/')
time.sleep(120)

#defineir contato ou grupo
contatos = ['Bot']
mensagem = 'Teste de automocao'
 #buscar contattos/grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,“ copyable-text selectable-text”)]')
    time.sleep (3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_element_by_xpath('//div[contains(@class,“ copyable-text selectable-text”)]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem.send_keys[1](mensagem)
    campo_mensagem.send_keys[1](keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

    #campo de pesquisa copyable-text selectable-text"
    #campo para mensagem privada copyable-text selectable-text

    