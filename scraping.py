from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from anticaptchaofficial.recaptchav2proxyless import *
from dotenv import dotenv_values
from time import sleep
import pandas as pd

env = dotenv_values('.env')
browser = webdriver.Chrome()

browser.get("https://sia.estacio.br/sianet/logon/")

chave_captcha = 

solver = recaptchav2proxyless()
solver.set_verbose(1)
solver.set_key()
solver.set_website_url("https://sia.estacio.br/sianet/logon/")
solver.set_website_key(chave_captcha)

el = browser.find_element(By.XPATH, '//*[@id="Usuario"]').send_keys(env.get('LOGIN_ESTACIO'))

sleep(2)

browser.find_element(By.XPATH, '//*[@id="Senha"]').send_keys(env.get('PASSWORD_ESTACIO'))

sleep(2)

# antirecaptcha
el = browser.find_element(By.XPATH, '//*[@id="rc-anchor-container"]').get_attribute('innerHTML')
# el = browser.find_element(By.ID, 'rc-anchor-container').get_attribute('innerHTML')

print(el)
sleep(2)

browser.find_element(By.XPATH, '//*[@id="btnEntrar"]')

sleep(3)

'''el = browser.find_element('xpath', '//*[@id="Usuario"]').get_attribute("innerHTML")
print(el)'''

