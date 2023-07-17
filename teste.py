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

driver.get("https://chat.openai.com")
driver.execute_script("window.open()")
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
driver.get("https://bard.google.com/")
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
login_button = driver.find_element(By.XPATH, "//html/body/div[1]/div[1]/div[1]/div[4]/button[1]")
login_button.click()
time.sleep(50)
driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td/div/div[1]/table/tbody/tr/td[1]/div[1]/div/label/span[1]").click()
while True:
    pass