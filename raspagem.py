# passo 1 - fazer a automação para abrir o chat gpt e fazer a pergunta 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Configuração do ChromeDriver
chromedriver_path = "D:\PYThON PROJECTS\Scrapping chatgpt_bard" # Substitua pelo caminho correto para o seu ChromeDriver

# Inicialização do serviço do ChromeDriver
service = Service(chromedriver_path)

# Inicialização do navegador Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maximiza a janela do Chrome ao iniciar
driver = webdriver.Chrome(service=service, options=options)

# Navegação para o site do Chat GPT
driver.get("https://chat.openai.com")

time.sleep(15)
button_element = driver.find_element_by_xpath('//*[@id="blog-details-chatgpt"]/div[1]/div[2]/div/div/div/div[1]/ul/li[1]/a')
button_element.click()

################################
# Aguarda um tempo antes de fechar o navegador
#time.sleep(60)  

# Encerramento do navegador
#driver.quit()
while True:
    pass
 