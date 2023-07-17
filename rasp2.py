from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
#driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[1])

# Abrir a segunda janela com o site bard.google.com
driver.execute_script("window.open('https://bard.google.com/', '_blank')")
print(driver.window_handles)
#driver.get('https://bard.google.com/')


# Obter o identificador das duas janelas
window_handles = driver.window_handles

time.sleep(15)

# Obter o identificador das duas janelas
window_handles = driver.window_handles

# Trocar para a primeira janela (ChatGPT)
driver.switch_to.window(driver.window_handles[0])
# Aguardar o carregamento da página
driver.implicitly_wait(15)  

# Aqui você pode interagir com a página aberta no ChatGPT
login_button = driver.find_element(By.XPATH, "//html/body/div[1]/div[1]/div[1]/div[4]/button[1]")
login_button.click()

# Trocar para a segunda janela (bard.google.com)
driver.switch_to.window(driver.window_handles[1])

# Aguardar o carregamento da página
driver.implicitly_wait(15)  # Espera implicitamente até 10 segundos (ajuste conforme necessário)

# Aqui você pode interagir com a página aberta no bard.google.com

# Encerrar o navegador
# driver.quit()