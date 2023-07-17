from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do ChromeDriver
chromedriver_path = "D:\PYThON PROJECTS\Scrapping chatgpt_bard\chromedriver"  # Substitua pelo caminho correto para o seu ChromeDriver

# Inicialização do serviço do ChromeDriver
service = Service(chromedriver_path)

# Inicialização do navegador Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maximiza a janela do Chrome ao iniciar
driver = webdriver.Chrome(service=service, options=options)

# Navegação para o site do Chat GPT
driver.get("https://chat.openai.com")
driver.switch_to.window(driver.window_handles[-1])

# Abrir a segunda janela com o site bard.google.com
driver.execute_script("window.open('https://bard.google.com/', '_blank')")

# Obter o identificador das duas janelas
window_handles = driver.window_handles

# Trocar para a primeira janela (ChatGPT)
driver.switch_to.window(window_handles[0])

# Aguardar o carregamento da página e localizar o botão de login
wait = WebDriverWait(driver, 15)
login_button = driver.find_element_by_xpath("//button[contains(text(), 'Log in')]")
driver.execute_script("arguments[0].click();", login_button)

# Trocar para a segunda janela (bard.google.com)
driver.switch_to.window(window_handles[1])

# Aguardar o carregamento da página

# Aqui você pode interagir com a página aberta no bard.google.com

# Encerrar o navegador
# driver.quit()
